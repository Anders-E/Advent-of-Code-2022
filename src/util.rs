use std::io::{self, Read};

pub fn read_rows() -> Vec<String> {
    let mut buf= String::new();
    match io::stdin().read_to_string(&mut buf) {
        Err(e) => println!("{:?}", e),
        _ => (),
    };
    return buf.split("\n")
        .map(|s| s.to_string())
        .collect();
}