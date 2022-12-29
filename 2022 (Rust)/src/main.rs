mod day_1;
mod day_2;
mod day_3;
mod day_4;

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let day:i8 = match args[1].parse() {
        Ok(val) => {val},
        Err(e) => {
            println!("Please give a day to run: {}", e);
            return;
        }
    };
    println!("Running day {}",day);

    match day {
        1 => day_1::get_elf_with_most_calories(),
        2 => {
            day_2::calculate_strategy_score();
            day_2::calculate_strategy_score_corrected();
        },
        3 => {
            day_3::sum_priorities_in_rucksack();
            day_3::sum_grouped_priorities_in_rucksack();
        },
        4 => day_4::get_nr_of_overlapping_pairs(),
        _ => println!("Day {} is not implemented yet", day),
    }
}


