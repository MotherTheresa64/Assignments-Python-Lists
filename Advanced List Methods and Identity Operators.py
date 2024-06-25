#Task 1: Given the two lists:
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
#Below is the simple for commented
# if "Alice" in submitted and "Alice" in attended:
#     print("Alice submitted her assignment and attended class")
# else:
#     print("Alice did not both submit her assignment and attend class")

if "Alice" in submitted and "Alice" in attended:
    print("Alice submitted her assignment and attended class")
elif "Alice" not in submitted and "Alice" in attended:
    print("At least she went to class")
elif "Alice" in submitted and "Alice" not in attended:
    print("Well. At least she showed up to class")
else:
    print("I'm disappointed that she did neither!")