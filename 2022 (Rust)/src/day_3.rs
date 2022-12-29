
fn add_priority(sum: &mut i32, letter:char){
    let letters_small: Vec<char> = ('a'..='z').collect();
    let letters_large: Vec<char> = ('A'..='Z').collect();
    if letter.is_uppercase() {
        *sum = *sum + 26;
        *sum = *sum + letters_large.iter().position(|&r| r == letter).unwrap() as i32 + 1;
    } else {
        *sum = *sum + letters_small.iter().position(|&r| r == letter).unwrap() as i32 + 1;
    }
}


pub fn sum_priorities_in_rucksack(){
    println!("\nUsing function: sum_priorities_in_rucksack()");
    
    // Read data
    let data = std::fs::read_to_string("data/3.txt").expect("Couldn't read file");
    let mut sum_of_priorities = 0;
    

    for row in data.split("\n"){
        let string_len = row.chars().count();
        let mut found = false;
        for i_1 in 0..string_len/2 {
            for i_2 in string_len/2..string_len {

                let item_comp_1 = row.chars().nth(i_1).unwrap();
                let item_comp_2 = row.chars().nth(i_2).unwrap();

                if item_comp_1 == item_comp_2{
                    add_priority(&mut sum_of_priorities, item_comp_1);
                    found = true;
                    break;
                }   
            }
            if found {
                break;
            }
        }
    }
    println!("Sum of priorities of all rucksacks: {}", sum_of_priorities);
}

fn find_same_of_3(elves: &Vec<String>) -> char {
    for item_1 in elves[0].chars(){
        for item_2 in elves[1].chars(){
            if item_1 == item_2 {
                for item_3 in elves[2].chars(){
                    if item_1 == item_3 {
                        return item_1;
                    }
                }
            }
        }
    }
    return '.'
}

pub fn sum_grouped_priorities_in_rucksack(){
    println!("\nUsing function: sum_grouped_priorities_in_rucksack()");
    
    // Read data
    let data = std::fs::read_to_string("data/3.txt").expect("Couldn't read file");
    let mut sum_of_priorities = 0;
    let mut elves: Vec<String> = Vec::new();

    for row in data.split("\n"){
        elves.push(row.to_string());

        if elves.len() == 3 {
            let item: char = find_same_of_3(&elves);
            add_priority(&mut sum_of_priorities, item);
            elves.clear();
        }
    }
    println!("Sum of grouped priorities of all rucksacks: {}", sum_of_priorities);
}