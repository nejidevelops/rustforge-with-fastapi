use std::io::{self, Read};
use serde::Deserialize;


#[derive(Deserialize)]
struct Input {
    numbers: Vec<i32>,
}
fn main() {
    let mut input = String::new();

    io::stdin()
        .read_to_string(&mut input)
        .expect("Failed to read input");

    println!("Rust received: {}", input);

    let data: Input = serde_json::from_str(&input)
        .expect("Failed to parse json");

    println!("{:?}", data.numbers);
}