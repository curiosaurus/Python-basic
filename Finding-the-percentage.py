import statistics
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        #print(type(line))
        scores = list(map(float, line))
        #print(type(line))
        student_marks[name] = scores
    query_name = input()
    s=(statistics.mean(student_marks[query_name]))
    print("{:.2f}".format(s))
    #print(str(sum(student_marks[query_name])/3)+"0")
    #print()
    #d['key']=value
