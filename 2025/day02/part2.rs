use std::collections::HashSet;
use std::env;
use std::fs;
use std::io::{self, Read};
use std::path::PathBuf;

fn find_invalid_in_range(start: u64, end: u64) -> HashSet<u64> {
    let mut invalid_ids = HashSet::new();

    let start_digits = start.to_string().len();
    let end_digits = end.to_string().len();

    // For each total digit count in range
    for total_digits in start_digits..=end_digits {
        // For each pattern length that divides total_digits
        for pattern_len in 1..=total_digits / 2 {
            if total_digits % pattern_len != 0 {
                continue;
            }

            let reps = total_digits / pattern_len;
            if reps < 2 {
                continue;
            }

            // Calculate the range of patterns to check
            let min_pattern = if pattern_len > 1 { 10_u64.pow((pattern_len - 1) as u32) } else { 1 };
            let max_pattern = 10_u64.pow(pattern_len as u32) - 1;

            // Narrow down the pattern range based on start/end
            for pattern in min_pattern..=max_pattern {
                let pattern_str = pattern.to_string();
                let repeated: String = pattern_str.repeat(reps);

                if let Ok(candidate) = repeated.parse::<u64>() {
                    if candidate > end {
                        break;
                    }
                    if candidate >= start {
                        invalid_ids.insert(candidate);
                    }
                }
            }
        }
    }

    invalid_ids
}

fn solve(input: &str) -> u64 {
    let line = input.trim().trim_end_matches(',');
    if line.is_empty() {
        return 0;
    }

    let mut total: u64 = 0;

    for range_str in line.split(',') {
        let range_str = range_str.trim();
        if range_str.is_empty() {
            continue;
        }

        let parts: Vec<&str> = range_str.split('-').collect();
        if parts.len() != 2 {
            continue;
        }

        let start: u64 = parts[0].parse().unwrap();
        let end: u64 = parts[1].parse().unwrap();

        let invalid_ids = find_invalid_in_range(start, end);
        total += invalid_ids.iter().sum::<u64>();
    }

    total
}

/// Entrée par défaut : <année>/inputs/<jour>.txt, déduite du chemin du fichier source.
fn default_input() -> PathBuf {
    let mut source = PathBuf::from(file!());
    if source.is_relative() {
        if let Ok(cwd) = std::env::current_dir() {
            source = cwd.join(source);
        }
    }
    source
        .parent()
        .and_then(|day| day.parent())
        .expect("chemin source inattendu")
        .join("inputs")
        .join("day02.txt")
}

fn main() {
    // Entrée : argument explicite, sinon l'entrée du puzzle versionnée, sinon stdin.
    let path = env::args().nth(1).map(PathBuf::from).unwrap_or_else(default_input);
    let input = if path.exists() {
        fs::read_to_string(&path).expect("Failed to read file")
    } else {
        let mut buffer = String::new();
        io::stdin().read_to_string(&mut buffer).expect("Failed to read stdin");
        buffer
    };

    let result = solve(&input);
    println!("{}", result);
}
