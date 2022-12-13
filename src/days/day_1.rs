use std::cmp;

use crate::util;

fn main() {
    let input = util::read_rows();
    println!("01_1: {}", star1(&input));
    println!("01_2: {}", star2(&input));
}

pub fn star1(input: &Vec<String>) -> u32 {
    return input.split(|x| x == "")
        .map(sum_inventory)
        .reduce(|accum, item| cmp::max(accum, item))
        .unwrap();
}

pub fn star2(input: &Vec<String>) -> u32 {
    let mut sums = input.split(|x| x == "")
        .map(sum_inventory).collect::<Vec<_>>();
    sums.sort();
    return sums.iter().rev().take(3).sum();
}

fn sum_inventory(inventory: &[String]) -> u32 {
    return inventory.iter()
        .map(|x| x.parse::<u32>()
        .expect("We know these are ints"))
        .reduce(|accum, item| accum + item).unwrap();
}
