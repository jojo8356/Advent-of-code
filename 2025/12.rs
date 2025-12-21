use std::collections::HashSet;
use std::env;
use std::fs;
use std::io::{self, Read};

fn parse_shape(lines: &[&str]) -> Vec<(i32, i32)> {
    let mut cells = Vec::new();
    for (r, line) in lines.iter().enumerate() {
        for (c, ch) in line.chars().enumerate() {
            if ch == '#' {
                cells.push((r as i32, c as i32));
            }
        }
    }
    cells
}

fn normalize(cells: &[(i32, i32)]) -> Vec<(i32, i32)> {
    if cells.is_empty() {
        return Vec::new();
    }
    let min_r = cells.iter().map(|&(r, _)| r).min().unwrap();
    let min_c = cells.iter().map(|&(_, c)| c).min().unwrap();
    let mut normalized: Vec<(i32, i32)> = cells.iter().map(|&(r, c)| (r - min_r, c - min_c)).collect();
    normalized.sort();
    normalized
}

fn rotate_90(cells: &[(i32, i32)]) -> Vec<(i32, i32)> {
    cells.iter().map(|&(r, c)| (c, -r)).collect()
}

fn flip_h(cells: &[(i32, i32)]) -> Vec<(i32, i32)> {
    cells.iter().map(|&(r, c)| (r, -c)).collect()
}

fn get_variations(shape: &[(i32, i32)]) -> Vec<Vec<(i32, i32)>> {
    let mut variations: HashSet<Vec<(i32, i32)>> = HashSet::new();
    let mut current = shape.to_vec();

    for _ in 0..4 {
        variations.insert(normalize(&current));
        variations.insert(normalize(&flip_h(&current)));
        current = rotate_90(&current);
    }

    variations.into_iter().collect()
}

fn can_place(grid: &[Vec<bool>], shape: &[(i32, i32)], sr: i32, sc: i32, rows: i32, cols: i32) -> bool {
    for &(dr, dc) in shape {
        let r = sr + dr;
        let c = sc + dc;
        if r < 0 || r >= rows || c < 0 || c >= cols {
            return false;
        }
        if grid[r as usize][c as usize] {
            return false;
        }
    }
    true
}

fn place(grid: &mut [Vec<bool>], shape: &[(i32, i32)], sr: i32, sc: i32) {
    for &(dr, dc) in shape {
        grid[(sr + dr) as usize][(sc + dc) as usize] = true;
    }
}

fn unplace(grid: &mut [Vec<bool>], shape: &[(i32, i32)], sr: i32, sc: i32) {
    for &(dr, dc) in shape {
        grid[(sr + dr) as usize][(sc + dc) as usize] = false;
    }
}

fn solve_region(rows: usize, cols: usize, presents: &[(Vec<Vec<(i32, i32)>>, usize)]) -> bool {
    let mut grid = vec![vec![false; cols]; rows];

    // Flatten: list of shape variations for each piece to place
    let mut shapes_to_place: Vec<&Vec<Vec<(i32, i32)>>> = Vec::new();
    for (shape_vars, count) in presents {
        for _ in 0..*count {
            shapes_to_place.push(shape_vars);
        }
    }

    if shapes_to_place.is_empty() {
        return true;
    }

    // Sort by fewer variations first (harder to place)
    shapes_to_place.sort_by_key(|v| v.len());

    fn backtrack(
        grid: &mut [Vec<bool>],
        shapes: &[&Vec<Vec<(i32, i32)>>],
        idx: usize,
        rows: i32,
        cols: i32,
    ) -> bool {
        if idx == shapes.len() {
            return true;
        }

        for var in shapes[idx].iter() {
            let max_dr = var.iter().map(|&(dr, _)| dr).max().unwrap_or(0);
            let max_dc = var.iter().map(|&(_, dc)| dc).max().unwrap_or(0);

            for sr in 0..=(rows - 1 - max_dr) {
                for sc in 0..=(cols - 1 - max_dc) {
                    if can_place(grid, var, sr, sc, rows, cols) {
                        place(grid, var, sr, sc);
                        if backtrack(grid, shapes, idx + 1, rows, cols) {
                            return true;
                        }
                        unplace(grid, var, sr, sc);
                    }
                }
            }
        }

        false
    }

    backtrack(&mut grid, &shapes_to_place, 0, rows as i32, cols as i32)
}

fn solve(input: &str) -> i32 {
    let lines: Vec<&str> = input.lines().collect();
    let mut shapes: Vec<Vec<Vec<(i32, i32)>>> = Vec::new();
    let mut regions: Vec<(usize, usize, Vec<usize>)> = Vec::new();
    let mut shape_sizes: Vec<usize> = Vec::new();

    let mut i = 0;
    while i < lines.len() {
        let line = lines[i].trim();

        if line.is_empty() {
            i += 1;
            continue;
        }

        if line.ends_with(':') && line[..line.len()-1].parse::<usize>().is_ok() {
            i += 1;
            let mut shape_lines = Vec::new();
            while i < lines.len() {
                let l = lines[i];
                if l.trim().is_empty() || l.trim().ends_with(':') || l.contains('x') {
                    break;
                }
                shape_lines.push(l);
                i += 1;
            }
            let shape = parse_shape(&shape_lines);
            shape_sizes.push(shape.len());
            shapes.push(get_variations(&shape));
        } else if line.contains('x') {
            let parts: Vec<&str> = line.split(": ").collect();
            let dims: Vec<usize> = parts[0].split('x').map(|s| s.parse().unwrap()).collect();
            let counts: Vec<usize> = parts[1].split_whitespace().map(|s| s.parse().unwrap()).collect();
            regions.push((dims[0], dims[1], counts));
            i += 1;
        } else {
            i += 1;
        }
    }

    let mut fit_count = 0;

    for (width, height, counts) in &regions {
        let area = width * height;
        let total_cells: usize = counts.iter().enumerate().map(|(idx, &c)| c * shape_sizes[idx]).sum();

        // Quick check: not enough space
        if total_cells > area {
            continue;
        }

        // Build presents list
        let mut presents: Vec<(Vec<Vec<(i32, i32)>>, usize)> = Vec::new();
        for (idx, &count) in counts.iter().enumerate() {
            if count > 0 {
                presents.push((shapes[idx].clone(), count));
            }
        }

        if solve_region(*height, *width, &presents) {
            fit_count += 1;
        }
    }

    fit_count
}

fn main() {
    let input = if let Some(filename) = env::args().nth(1) {
        fs::read_to_string(filename).expect("Failed to read file")
    } else {
        let mut buffer = String::new();
        io::stdin().read_to_string(&mut buffer).expect("Failed to read stdin");
        buffer
    };

    let result = solve(&input);
    println!("{}", result);
}
