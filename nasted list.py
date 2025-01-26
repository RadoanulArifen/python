if __name__ == '__main__':
    students = [[input(), float(input())] for _ in range(int(input()))]  # Read input
    second_lowest = sorted(set(score for name, score in students))[1]  # Find second lowest grade
    names = sorted(name for name, score in students if score == second_lowest)  # Names with second lowest grade
    print("\n".join(names))  # Print names, one per line
