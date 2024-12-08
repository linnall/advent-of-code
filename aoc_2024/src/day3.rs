use std::fs::File;
use std::io::{self, BufReader, Read};

pub fn part_one() -> io::Result<()> {
    // Open the file
    let file = File::open("3.in")?;
    
    // Wrap the file in a buffered reader
    let mut reader = BufReader::new(file);

    // Buffer to hold one byte at a time
    let mut buffer = [0; 1];
    let mut term1 = String::new();
    let mut term2 = String::new();
    let mut op = String::new();
    let mut ans = 0;

    // Read the file character by character
    while let Ok(bytes_read) = reader.read(&mut buffer) {
        if bytes_read == 0 {
            break; // EOF reached
        }

        // Convert the byte to a character
        if let Ok(character) = std::str::from_utf8(&buffer) {
            let c = character.chars().next();

            match c {
                Some(c) => {
                    if c == 'm' && op.is_empty() {
                    op.push(c);
                    } else if c == 'm' && !op.is_empty() {
                        op = String::from('m');
                        term1 = String::from("");
                        term2 = String::from("");
                    } else if c == 'u' && op == "m" {
                        op.push(c);
                    } else if c == 'l' && op == "mu" {
                        op.push(c);
                    } else if c == '(' && op == "mul" {
                        op.push(c);
                    } else if c.is_numeric() && op == "mul(" {
                        term1.push(c);
                    } else if c == ',' && !term1.is_empty() && op == "mul(" {
                        op.push(c);
                    } else if c.is_numeric() && !term1.is_empty() && op == "mul(," {
                        term2.push(c);
                    } else if c == ')' && !term1.is_empty() && !term2.is_empty() && op == "mul(," {
                        let t1: i32 = term1.parse().unwrap();
                        let t2: i32 = term2.parse().unwrap();
                        ans += t1 * t2;
                        op = String::from("");
                        term1 = String::from("");
                        term2 = String::from("");
                    } else {
                        op = String::from("");
                        term1 = String::from("");
                        term2 = String::from("");
                    }
                },
                None => println!("The &str is empty!"),
            }

        } else {
            eprintln!("Invalid UTF-8 sequence encountered.");
        }
    }
    println!("answer: {}", ans);

    Ok(())
}

pub fn part_two() -> io::Result<()> {
    // Open the file
    let file = File::open("3.in")?;
    
    // Wrap the file in a buffered reader
    let mut reader = BufReader::new(file);

    // Buffer to hold one byte at a time
    let mut buffer = [0; 1];
    let mut term1 = String::new();
    let mut term2 = String::new();
    let mut op = String::new();
    let mut _do = String::new();
    let mut _do_not = String::new();
    let mut ignore = false;
    let mut ans = 0;

    // Read the file character by character
    while let Ok(bytes_read) = reader.read(&mut buffer) {
        if bytes_read == 0 {
            break; // EOF reached
        }

        // Convert the byte to a character
        if let Ok(character) = std::str::from_utf8(&buffer) {
            let c = character.chars().next();

            match c {
                Some(c) => {
                    if c == 'd' && _do.is_empty() && _do_not.is_empty() {
                        _do.push(c);
                        _do_not.push(c);
                    } else if c == 'o' && _do == "d" {
                        _do.push(c);
                        _do_not.push(c);
                    } else if c == '(' && _do == "do" {
                        _do.push(c);
                        _do_not = String::from(""); 
                    } else if c == ')' && _do == "do(" {
                        ignore = false;
                        _do = String::from("");
                        _do_not = String::from("");
                    } else if c == 'n' && _do_not == "do" {
                        _do_not.push(c);
                        _do = String::from("");
                    } else if c == '\'' && _do_not == "don" {
                        _do_not.push(c); 
                    } else if c == 't' && _do_not == "don'" {
                        _do_not.push(c); 
                    } else if c == '(' && _do_not == "don't" {
                        _do_not.push(c);  
                    } else if c == ')' && _do_not == "don't(" {
                        ignore = true;
                        _do = String::from("");
                        _do_not = String::from(""); 
                    }
                    else if c == 'm' && op.is_empty() {
                    op.push(c);
                    } else if c == 'm' && !op.is_empty() {
                        op = String::from('m');
                        term1 = String::from("");
                        term2 = String::from("");
                    } else if c == 'u' && op == "m" {
                        op.push(c);
                    } else if c == 'l' && op == "mu" {
                        op.push(c);
                    } else if c == '(' && op == "mul" {
                        op.push(c);
                    } else if c.is_numeric() && op == "mul(" {
                        term1.push(c);
                    } else if c == ',' && !term1.is_empty() && op == "mul(" {
                        op.push(c);
                    } else if c.is_numeric() && !term1.is_empty() && op == "mul(," {
                        term2.push(c);
                    } else if c == ')' && !term1.is_empty() && !term2.is_empty() && op == "mul(," {
                        if !ignore {
                            let t1: i32 = term1.parse().unwrap();
                            let t2: i32 = term2.parse().unwrap();
                            ans += t1 * t2;
                        }
                        op = String::from("");
                        term1 = String::from("");
                        term2 = String::from("");
                    } else {
                        op = String::from("");
                        term1 = String::from("");
                        term2 = String::from("");
                        _do = String::from("");
                        _do_not = String::from(""); 
                    }
                },
                None => println!("The &str is empty!"),
            }

        } else {
            eprintln!("Invalid UTF-8 sequence encountered.");
        }
    }
    println!("answer: {}", ans);

    Ok(())
}
