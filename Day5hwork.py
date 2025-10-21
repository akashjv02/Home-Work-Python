Front_end = {"Akash", "Shuttumani", "Vijay Sethupathi", "Gayathri Reddy"}
Back_end = {"Rony", "Ramani", "Ajith", "Lekshmi", "Shuttumani", "Gayathri Reddy"}

Back_end.add("Sumi")
Front_end.remove("Vijay Sethupathi")

#list students who are in both front-end and back-end

print(Front_end & Back_end)

#  list of students who are enrolled only in Backend, but not in Frontend
print(Front_end - Back_end)

#Display the total number of unique students
print( Front_end ^ Back_end)

#create dictionary
course = {
    "Frontend" : 3,
    "Backend" : 7
}
for x, y in course.items():
    print(x, y)

fullstack = {
    "Fullstack" : course["Frontend"] + course["Backend"]
}
print(fullstack)
