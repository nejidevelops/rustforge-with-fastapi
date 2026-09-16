use std::io::{self, Read};
use serde::{Deserialize, Serialize};


#[derive(Deserialize)]
struct Input {
    numbers: Vec<i32>,
}

#[derive(Serialize)]
struct Output {
    sum: i32,
    average: f64,
}

fn calculate_average(numbers: &[i32]) -> Option<f64> {
    let sum: i32 = numbers.iter().sum();

    if numbers.is_empty() {
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

    let sum: i32 = data.numbers.iter().sum();

    let average = calculate_average(&data.numbers)
        .expect("Cannot calculate average for empty numbers");

    let result = Output {
        sum,
        average,
    };

    let output = serde_json::to_string(&result)
        .expect("Failed to serialize output");

    println!("{}", output)
}