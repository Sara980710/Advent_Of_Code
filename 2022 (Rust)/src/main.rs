mod day_1;



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
        _ => println!("Day {} is not implemented yet", day),
    }
}


