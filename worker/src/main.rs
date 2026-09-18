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

#[derive(Serialize)]
struct ErrorOutput {
    error: String
}

fn calculate_sum(numbers: &[i32]) -> i32 {
    numbers.iter().sum()
}

fn calculate_average(numbers: &[i32]) -> Result<f64, String> {
    let sum = calculate_sum(numbers);

    if numbers.is_empty() {
        return Err("Cannot calculate average of empty numbers".to_string());
    }

    let average: f64 = sum as f64 / numbers.len() as f64;

    Ok(average)
}

fn process(data: &Input) -> Result<Output, String> {
    let sum = calculate_sum(&data.numbers);

    let average = calculate_average(&data.numbers)?;

    let result = Output {
      average,
      sum,
    };

    Ok(result)
}

fn main() -> Result<(), String> {
    let mut input = String::new();
    
    io::stdin()
      .read_to_string(&mut input)
      .map_err(|error| error.to_string())?;
    
    let data: Input = serde_json::from_str(&input)
      .map_err(|error| error.to_string())?;

    let result = process(&data)?;

    let output = serde_json::to_string(&result)
      .map_err(|error| error.to_string())?;

    println!("{}", output);

    Ok(())
}