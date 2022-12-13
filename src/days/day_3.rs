pub fn main() {
    let input = util::read_rows();
    println!("01_1: {}", star1(&input));
    println!("01_2: {}", star2(&input));
}

fn star1(input: &Vec<String>) -> u32 {
    let rounds = input.iter().map(|x| x.split(" "));
    let mut total_score = 0;
    for round in rounds {
        let hands = round.map(string_to_hand).collect::<Vec<_>>();
        let (opponent, me) = (hands[0], hands[1]);
        total_score += score(opponent, me);
    }
    total_score
}

fn star2(input: &Vec<String>) -> u32 {
    let rounds = input.iter().map(|x| x.split(" "));
    let mut total_score = 0;
    for round in rounds {
        let row = round.collect::<Vec<_>>();
        let opponent = string_to_hand(row[0]);
        let expected_result = row[1];
        let me = string_to_expected_hand(expected_result, opponent);
        println!("{me}");
        total_score += score(opponent, me);
    }
    total_score
}

fn string_to_hand(s: &str) -> i8 {
    if s == "A" || s == "X" {
        return 0;
    } else if s == "B" || s == "Y" {
        return 1;
    }
    2
}

fn string_to_expected_hand(expected_result: &str, opponent: i8) -> i8 {
    match expected_result {
        "X" => (opponent - 1).rem_euclid(3),
        "Y" => opponent,
        _   => (opponent + 1).rem_euclid(3),
    }
}

fn score(opponent: i8, me: i8) -> u32 {
    let win_score = match opponent - me {
        -1 | 2 => 6,
        0 => 3,
        _ => 0,
    };
    let hand_score = me + 1;
    return (hand_score + win_score) as u32;
}
