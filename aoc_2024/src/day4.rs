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

fn xmas_count(row: usize, col: usize, grid: &Vec<Vec<String>>) -> i32 {
    let rows = grid.len();
    let cols = grid[0].len();
    let mut total = 0;
    let directions: Vec<(i32, i32)> = Vec::from([
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]);
    for (ud, lr) in directions {
        let mut _row: i32 = row as i32;
        let mut _col: i32 = col as i32;
        let mut string = String::from(&grid[_row as usize][_col as usize]);
        for _ in 0..3 {
            _row += ud;
            _col += lr;
            if _row < 0 || _row >= rows as i32 || _col < 0 || _col >= cols as i32 {
                break;
            }
            let ch = &grid[_row as usize][_col as usize];
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

fn x_mas_count(ud: usize, lr: usize, grid: &Vec<Vec<String>>) -> i32 {
    let mut total = 0;
    let rows = grid.len();
    let cols = grid[0].len();
    if &grid[ud][lr] == "A" && ud > 0 && ud < rows - 1 && lr > 0 && lr < cols - 1 {
        let cross1 = String::from_iter([
            &grid[ud - 1][lr - 1].chars().next().unwrap(),
            &grid[ud][lr].chars().next().unwrap(),
            &grid[ud + 1][lr + 1].chars().next().unwrap(),
        ]);
        let cross2 = String::from_iter([
            &grid[ud + 1][lr - 1].chars().next().unwrap(),
            &grid[ud][lr].chars().next().unwrap(),
            &grid[ud - 1][lr + 1].chars().next().unwrap(),
        ]);
        if (cross1 == "MAS" || cross1 == "SAM") && (cross2 == "MAS" || cross2 == "SAM") {
            total += 1;
        }
    }
    total
}

pub fn part_one() {
    let file_path = "4.in";
    let grid = build_grid(file_path);
    let mut total = 0;
    for row in 0..grid.len() {
        for col in 0..grid[row].len() {
            total += xmas_count(row, col, &grid);
        }
    }
    println!("{total}");
}

pub fn part_two() {
    let file_path = "4.in";
    let grid = build_grid(file_path);
    let mut total = 0;
    for row in 0..grid.len() {
        for col in 0..grid[row].len() {
            total += x_mas_count(row, col, &grid);
        }
    }
    println!("{total}");
}
