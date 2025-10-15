para = """The Python Programming course provides a comprehensive introduction to one of the most popular and versatile programming languages in the world.
It covers the fundamentals of Python, including data types, variables, operators, control structures, functions, and object-oriented programming.
Students also learn about file handling, libraries, and modules that make Python powerful for real-world applications. 
The course emphasizes hands-on learning through coding exercises and practical projects, helping learners develop problem-solving and logical thinking skills. 
Python’s simplicity and readability make it ideal for beginners, while its vast ecosystem supports advanced topics like 
web development, data analysis, and artificial intelligence, preparing students for diverse career paths in technology."""

print(para)

print("Paraqgraph Legth is = ", len(para))

print("Only 50 character = ",para[:51])

print(para.replace("Python", "PYTHON"))

print(para.lower())

print(para.strip())

split = para.split(" ")
print(split)

print("The course in the paragraph = ","course" in para)

final_msg = "The course description is {} characters long and has {} words"

print(final_msg.format(len(para), len(split)))