use std::fs::File;
use std::io::{self, BufRead};

pub fn solution_one() -> io::Result<()> {
    // Define the file path
    let file_path = "2.in";

    // Open the file
    let file = File::open(file_path)?;
    let reader = io::BufReader::new(file);
    let mut safe_num: i32 = 0;

    // Iterate through each line
    for line in reader.lines() {
        // Read the line
        let line = line?;

        // Split the line into parts and parse into numbers
        let numbers: Vec<i32> = line
            .split_whitespace() // Split by whitespace
            .filter_map(|num| num.parse::<i32>().ok()) // Parse to i32, filter out errors
            .collect();

        // Process the vector of numbers (example: print them)
        let mut prev: i32 = numbers[0];
        let mut delta: i32 = 0;
        let mut is_safe: bool = true;
        for i in 1..numbers.len() {
            let diff = numbers[i] - prev;
            if delta == 0 {
                if diff.abs() > 3 || diff.abs() < 1 {
                    is_safe = false;
                    break;
                }
                delta = diff;
                prev = numbers[i];
            } else if delta < 0 {
                if diff >= 0 || diff.abs() > 3 {
                    is_safe = false;
                    break;
                }
                delta = diff;
                prev = numbers[i]
            } else {
                if diff <= 0 || diff.abs() > 3 {
                    is_safe = false;
                    break;
                }
                delta = diff;
                prev = numbers[i]
            }
        }
        if is_safe {
            safe_num += 1;
        }

    }

    println!("answer: {}", safe_num);

    Ok(())
}
