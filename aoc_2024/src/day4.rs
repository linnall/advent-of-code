use std::fs;

fn build_grid(file_path: &str) -> Vec<Vec<String>> {
    let mut grid: Vec<Vec<String>> = Vec::new();

    match fs::read_to_string(file_path) {
        Ok(contents) => {
            grid = contents
            .lines()
            .map(|line| line.chars().map(|ch| ch.to_string()).collect())
            .collect();
        }
        Err(e) => {
            eprintln!("Error reading file: {}", e);
        }
    }

    // for row in &grid {
    //     println!("{:?}", row);
    // }
    grid
}

pub fn part_one() {
    let file_path = "4.in";
    let grid = build_grid(file_path);
}

