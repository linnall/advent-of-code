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

fn xmas_count(x: usize, y: usize, grid: &Vec<Vec<String>>) -> i32 {
    let rows = grid.len();
    let cols = grid[0].len();
    let mut total = 0;
    let directions: Vec<(i32, i32)> = Vec::from([(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]);
    let a = x;
    let b = y;
    for (row, col) in directions {
        let mut string = String::from(grid[x][y]);
        for _ in 0..3 {
            let _a = a as i32 + row;
            let _b = b as i32 + col;
            if _a < 0 || a > rows || b < 0 || b > cols {
                break;
            }
            let ch = grid[_a as usize][_b as usize];
            if string == "X" && ch == "M" {
                string.push('M');
            } else if string == "XM" && ch == "A" {
                string.push('A');
            } else if string == "XMA" && ch == "S" {
                total += 1;
            } else {
                break;
            }
        }
    }
    total
}

pub fn part_one() {
    let file_path = "4.in";
    let grid = build_grid(file_path);
    for row in &grid {
        for element in row {

        }
    }
}

