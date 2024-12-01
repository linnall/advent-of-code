use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn one() -> io::Result<()> {
    // Open the file
    let path = Path::new("1.in"); // Replace with your file path
    let file = File::open(path)?;

    // Create a buffered reader
    let reader = std::io::BufReader::new(file);

    // Iterate over each line
    let mut total: i32 = 0;
    let mut v1: Vec<i32> = Vec::new();
    let mut v2: Vec<i32> = Vec::new();
    for line in reader.lines() {
        let line = line?; // Unwrap the result of reading the line

        // Split the line by whitespace and attempt to parse two numbers
        let parts: Vec<&str> = line.split_whitespace().collect();
        if parts.len() == 2 {
            // Parse the two numbers (you can handle the parsing result as needed)
            if let (Ok(num1), Ok(num2)) = (parts[0].parse::<i32>(), parts[1].parse::<i32>()) {
                // println!("Parsed numbers: {} and {}", num1, num2);
                v1.push(num1);
                v2.push(num2);
            } else {
                eprintln!("Error: Could not parse numbers from line: {}", line);
            }
        } else {
            eprintln!("Error: Line does not contain exactly two numbers: {}", line);
        }
    }

    v1.sort();
    v2.sort();

    for i in 0..v1.len() {
        let value: i32 = &v1[i] - &v2[i];
        total += value.abs();
    }
    println!("answer: {}", total);

    Ok(())
}

fn two() -> io::Result<()> {
    // Open the file
    let path = Path::new("1.in"); // Replace with your file path
    let file = File::open(path)?;

    // Create a buffered reader
    let reader = std::io::BufReader::new(file);

    // Iterate over each line
    let mut total: i32 = 0;
    let mut v1: Vec<i32> = Vec::new();
    let mut v2: Vec<i32> = Vec::new();
    let mut map = HashMap::new();
    for line in reader.lines() {
        let line = line?; // Unwrap the result of reading the line

        // Split the line by whitespace and attempt to parse two numbers
        let parts: Vec<&str> = line.split_whitespace().collect();
        if parts.len() == 2 {
            // Parse the two numbers (you can handle the parsing result as needed)
            if let (Ok(num1), Ok(num2)) = (parts[0].parse::<i32>(), parts[1].parse::<i32>()) {
                // println!("Parsed numbers: {} and {}", num1, num2);
                v1.push(num1);
                v2.push(num2);
            } else {
                eprintln!("Error: Could not parse numbers from line: {}", line);
            }
        } else {
            eprintln!("Error: Line does not contain exactly two numbers: {}", line);
        }
    }

    for i in 0..v1.len() {
        map.insert(v1[i], 0);
    }
    for i in 0..v2.len() {
        if map.contains_key(&v2[i]) {
            map.insert(v2[i], map[&v2[i]] + 1);
        }
    }
    for (key, val) in &map {
        total += key * val;
    }
    println!("answer: {}", total);

    Ok(())
}

fn main() -> io::Result<()> {
    two();
    Ok(())
}
