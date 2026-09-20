use std::io::{self, BufRead, Write};
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

    if let Err(error) = io::stdin().read_to_string(&mut input) {
      let output = ErrorOutput {
        error: format!("Failed to read input: {}", error),
      };

      println!(
        "{}",
        serde_json::to_string(&output)
          .expect("Failed to serialize error")
      );

      return Ok(());
    }

    let data: Input = match serde_json::from_str(&input) {
      Ok(data) => data,

      Err(error) => {
        let output = ErrorOutput {
          error: format!("Invalid JSON: {}", error),
        };

        println!(
          "{}",
          serde_json::to_string(&output)
            .expect("Failed to serialize error")
        );

        return Ok(());
      }
    };

    match process(&data) {
        Ok(result) => {
          let output = serde_json::to_string(&result)
              .expect("Failed to serialize output");

          println!("{}", output);
        }

        Err(error) => {
            let error_output = ErrorOutput {
                error,
            };

            let output = serde_json::to_string(&error_output)
              .expect("Failed to serialize error");         

            println!(
              "{}",
              output
            );
        }
    }

    Ok(())
}