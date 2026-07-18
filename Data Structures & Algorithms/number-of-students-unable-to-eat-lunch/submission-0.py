class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        r=0
        while sandwiches:
            if sandwiches[0]==students[0]:
                sandwiches.pop(0)
                students.pop(0)
                r=0
            else:
                students.append(students.pop(0))
                r+=1
            if len(sandwiches)==r:
                return len(students)