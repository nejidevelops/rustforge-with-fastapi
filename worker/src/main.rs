use std::io::{self, Read};
use serde::Deserialize;


#[derive(Deserialize)]
struct Input {
    numbers: Vec<i32>,
}

fn calculate_average(numbers: &[i32]) -> Option<f64> {
    let sum: i32 = numbers.iter().sum();

    if numbers.len() == 0 {
        return None
    }

    let average: f64 = sum as f64 / numbers.len() as f64;

    Some(average)
}

fn main() {
    let mut input = String::new();
    
    io::stdin()
    .read_to_string(&mut input)
    .expect("Failed to read input");
    
    let data: Input = serde_json::from_str(&input)
    .expect("Failed to parse json");

    let average = calculate_average(&data.numbers);

    match average {
        Some(value) => println!("{}", value),
        None => println!("There are no numbers to calculate average"),
    }
}