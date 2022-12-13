pub mod util;
mod days;

fn main() {
    let input = util::read_rows();
    // let star1_answer = day_1::star1(&input);
    // let star2_answer = day_1::star2(&input);
    let star1_answer = days::day_2::star1(&input);
    let star2_answer = days::day_2::star2(&input);
    println!("01_1: {star1_answer}");
    println!("01_2: {star2_answer}");
}
