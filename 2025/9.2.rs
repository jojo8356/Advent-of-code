use std::env;
use std::fs;
use std::io::{self, Read};

// Check if a point is inside or on the boundary of the polygon using ray casting
fn point_in_polygon(x: i64, y: i64, vertices: &[(i64, i64)]) -> bool {
    let n = vertices.len();
    let mut inside = false;

    let mut j = n - 1;
    for i in 0..n {
        let (xi, yi) = vertices[i];
        let (xj, yj) = vertices[j];

        // Check if point is on a horizontal edge
        if yi == yj && yi == y && x >= xi.min(xj) && x <= xi.max(xj) {
            return true;
        }

        // Check if point is on a vertical edge
        if xi == xj && xi == x && y >= yi.min(yj) && y <= yi.max(yj) {
            return true;
        }

        if (yi > y) != (yj > y) {
            let x_intersect = (xj - xi) * (y - yi) / (yj - yi) + xi;
            if x < x_intersect {
                inside = !inside;
            }
        }
        j = i;
    }
    inside
}

// Check if entire rectangle is inside polygon
fn rectangle_in_polygon(rx_min: i64, ry_min: i64, rx_max: i64, ry_max: i64,
                         vertices: &[(i64, i64)]) -> bool {
    // Check all 4 corners are inside
    let corners = [
        (rx_min, ry_min),
        (rx_min, ry_max),
        (rx_max, ry_min),
        (rx_max, ry_max),
    ];

    for &(cx, cy) in &corners {
        if !point_in_polygon(cx, cy, vertices) {
            return false;
        }
    }

    // For a rectilinear polygon, check if any edge crosses the rectangle interior
    let n = vertices.len();
    for i in 0..n {
        let (x1, y1) = vertices[i];
        let (x2, y2) = vertices[(i + 1) % n];

        if x1 == x2 {
            // Vertical edge
            let x = x1;
            let (ey_min, ey_max) = if y1 < y2 { (y1, y2) } else { (y2, y1) };

            // Edge crosses rectangle interior if:
            // - x is strictly between rx_min and rx_max
            // - edge y-range overlaps with rectangle y-range interior
            if x > rx_min && x < rx_max {
                if ey_min < ry_max && ey_max > ry_min {
                    return false;
                }
            }
        } else {
            // Horizontal edge
            let y = y1;
            let (ex_min, ex_max) = if x1 < x2 { (x1, x2) } else { (x2, x1) };

            // Edge crosses rectangle interior if:
            // - y is strictly between ry_min and ry_max
            // - edge x-range overlaps with rectangle x-range interior
            if y > ry_min && y < ry_max {
                if ex_min < rx_max && ex_max > rx_min {
                    return false;
                }
            }
        }
    }

    true
}

fn solve(input: &str) -> i64 {
    let mut tiles: Vec<(i64, i64)> = Vec::new();

    for line in input.lines() {
        let line = line.trim();
        if line.is_empty() {
            continue;
        }
        let parts: Vec<i64> = line.split(',').map(|s| s.parse().unwrap()).collect();
        tiles.push((parts[0], parts[1]));
    }

    if tiles.len() < 2 {
        return 0;
    }

    // Sort pairs by area (largest first) for early termination
    let mut pairs: Vec<(i64, usize, usize)> = Vec::new();
    for i in 0..tiles.len() {
        for j in (i + 1)..tiles.len() {
            let (x1, y1) = tiles[i];
            let (x2, y2) = tiles[j];
            let area = ((x1 - x2).abs() + 1) * ((y1 - y2).abs() + 1);
            pairs.push((area, i, j));
        }
    }
    pairs.sort_by(|a, b| b.0.cmp(&a.0));

    let mut max_area: i64 = 0;

    for (area, i, j) in pairs {
        if area <= max_area {
            break;
        }

        let (x1, y1) = tiles[i];
        let (x2, y2) = tiles[j];

        let rx_min = x1.min(x2);
        let rx_max = x1.max(x2);
        let ry_min = y1.min(y2);
        let ry_max = y1.max(y2);

        if rectangle_in_polygon(rx_min, ry_min, rx_max, ry_max, &tiles) {
            max_area = area;
        }
    }

    max_area
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
