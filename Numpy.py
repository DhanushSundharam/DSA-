def vagaigalin_vilakkam_generator():
    for i, j in pos["Noun"]["Types Explaination"].items():
        print( f"{i} ---> {j}")
        print("example")
        for x in pos["Noun"]["example"][i]:
            print(x)
        yield ""  # Empty line after each type

# Assuming pos is your dataset
pos = {
    "Noun": {
        "Types Explaination": {
            "Type1": "Explanation 1",
            "Type2": "Explanation 2",
            # ...
        },
        "example": {
            "Type1": ["Example 1", "Example 2"],
            "Type2": ["Example 3", "Example 4"],
            # ...
        }
    }
}

# Create the generator
gen = vagaigalin_vilakkam_generator()

# Interactive loop to use next() function
while True:
    try:
        user_input = input("Press Enter to see the next item or type 'exit' to quit: ")
        if user_input.lower() == "exit":
            break
        item = next(gen)
        print(item)
    except StopIteration:
        print("End of data.")
        break
