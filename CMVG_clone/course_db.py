from private_pages.models import Courses

file = open("private_pages/courses.list","r")

for line in file:
    line = line[:-1]
    if(line==""):
        continue
    print(line)