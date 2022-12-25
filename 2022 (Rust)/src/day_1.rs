

pub fn get_elf_with_most_calories(){
    println!("\nUsing function: get_elf_with_most_calories()");
    
    let data = std::fs::read_to_string("data/1.txt").expect("Couldn't read file");
    let mut calories_elves: Vec<u32> = Vec::new();

    for elf_data in data.split("\n\n"){
        let mut sum_calories = 0;
        for calories in elf_data.split("\n") {
            sum_calories += calories.parse::<u32>().unwrap();
        }
        calories_elves.push(sum_calories);
    }
    calories_elves.sort_by(|a, b| b.cmp(a)); // Descending

    // Part 1
    println!("Elf with the most number of calories: {}", &calories_elves[0]);

    // Part 2
    let three_largest_calories = &calories_elves[..3];
    let sum_of_three: u32 = three_largest_calories.iter().sum();
    println!("Top 3 elves with the most number of calories: {:?}", three_largest_calories);
    println!("Elf with the most number of calories: {}", sum_of_three);
}