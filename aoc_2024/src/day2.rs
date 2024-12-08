use std::fs::File;
use std::io::{self, BufRead};

pub fn part_one() -> io::Result<()> {
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

pub fn part_two() -> io::Result<()>{
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

        // try removing each element in vector
        for j in 0..numbers.len() {
            let mut numbers_temp: Vec<i32> = Vec::new();
            for k in 0..numbers.len() {
                if k != j {numbers_temp.push(numbers[k])};
            }
            // Process the vector of numbers (example: print them)
            let mut prev: i32 = numbers_temp[0];
            let mut delta: i32 = 0;
            let mut is_safe: bool = true;
            println!("{:?}", numbers_temp);
            for i in 1..numbers_temp.len() {
                let diff = numbers_temp[i] - prev;
                if delta == 0 {
                    if diff.abs() > 3 || diff.abs() < 1 {
                        is_safe = false;
                        break;
                    }
                    delta = diff;
                    prev = numbers_temp[i];
                } else if delta < 0 {
                    if diff >= 0 || diff.abs() > 3 {
                        is_safe = false;
                        break;
                    }
                    delta = diff;
                    prev = numbers_temp[i]
                } else {
                    if diff <= 0 || diff.abs() > 3 {
                        is_safe = false;
                        break;
                    }
                    delta = diff;
                    prev = numbers_temp[i]
                }
            }
            if is_safe {
                safe_num += 1;
                break;
            }
        }

    }

    println!("answer: {}", safe_num);

    Ok(())
}
