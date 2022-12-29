

pub fn get_nr_of_overlapping_pairs(){
    println!("\nUsing function: get_nr_of_overlapping_pairs()");
    
    // Read data
    let data = std::fs::read_to_string("data/4.txt").expect("Couldn't read file");
    let mut nr_of_overlapping_pairs = 0;

    for row in data.split("\n"){
        let (elf_1,elf_2) = row.split(",");
        println!("{}", elf_1);
    }
    println!("Number of overlapping pairs: {}", nr_of_overlapping_pairs);
}