// Opponent: A for Rock, B for Paper, and C for Scissors
// Your response: X for Rock, Y for Paper, and Z for Scissors
// Points: 1 for Rock, 2 for Paper, 3 for scissors, 6 for win, 3 for draw and 0 for win.
pub fn calculate_strategy_score(){
    println!("\nUsing function: calculate_strategy_score()");
    
    // Read data
    let data = std::fs::read_to_string("data/2.txt").expect("Couldn't read file");
    let mut total_score = 0;

    for row in data.split("\n"){
        let opponent = row.chars().nth(0).unwrap();
        let you = row.chars().nth(2).unwrap();

        // Outcome
        match opponent {
            'A' => {
                match you {
                    'Y' => total_score += 6,
                    'X' => total_score += 3,
                    _ => (),
                }
            }
            'B' => {
                match you {
                    'Z' => total_score += 6,
                    'Y' => total_score += 3,
                    _ => (),
                }
            }
            'C' => {
                match you {
                    'X' => total_score += 6,
                    'Z' => total_score += 3,
                    _ => (),
                }
            }
            _ => (),
        }
        
        // Points for chosen action
        match you {
            'X' => total_score += 1,
            'Y' => total_score += 2,
            'Z' => total_score += 3,
            _ => (),
        }
    }
    println!("Total score your own interpretation of strategy: {}", total_score)
}

// Opponent: A for Rock, B for Paper, and C for Scissors
// X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
// Points: 1 for Rock, 2 for Paper, 3 for scissors, 6 for win, 3 for draw and 0 for win.
pub fn calculate_strategy_score_corrected(){
    println!("\nUsing function: calculate_strategy_score_corrected()");
    
    // Read data
    let data = std::fs::read_to_string("data/2.txt").expect("Couldn't read file");
    let mut total_score = 0;

    for row in data.split("\n"){
        let opponent = row.chars().nth(0).unwrap();
        let outcome = row.chars().nth(2).unwrap();

        // Outcome
        match outcome {
            'X' => {
                match opponent {
                    'A' => total_score += 3, // You choose scissors
                    'B' => total_score += 1, // You choose rock
                    'C' => total_score += 2, // You choose paper
                    _ => (),
                }
            }
            'Y' => {
                match opponent {
                    'A' => total_score += 1, // You choose paper
                    'B' => total_score += 2, // You choose scissors
                    'C' => total_score += 3, // You choose rock
                    _ => (),
                }
                total_score += 3;
            }
            'Z' => {
                match opponent {
                    'A' => total_score += 2, // You choose paper
                    'B' => total_score += 3, // You choose scissors
                    'C' => total_score += 1, // You choose rock
                    _ => (),
                }
                total_score += 6;
            }
            _ => (),
        }
    }
    println!("Total score correct instructions: {}", total_score)
}