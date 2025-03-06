def generate_fibonacci_by_terms(n):
    if n <= 0:
        return []
    series = [0, 1]
    for _ in range(n - 2):
        series.append(series[-1] + series[-2])
    return series[:n]

def generate_fibonacci_by_value(max_value):
    if max_value < 0:
        return []
    series = [0, 1]
    while True:
        next_value = series[-1] + series[-2]
        if next_value > max_value:
            break
        series.append(next_value)
    return series

def main():
    while True:
        print("\nChoose an option:")
        print("1. Generate Fibonacci series by number of terms")
        print("2. Generate Fibonacci series by maximum value")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            try:
                n = int(input("Enter the number of terms: "))
                if n < 0:
                    print("Please enter a non-negative integer.")
                    continue
                series = generate_fibonacci_by_terms(n)
                print(f"Fibonacci series ({n} terms): {', '.join(map(str, series))}")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        
        elif choice == "2":
            try:
                max_value = int(input("Enter the maximum value: "))
                if max_value < 0:
                    print("Please enter a non-negative integer.")
                    continue
                series = generate_fibonacci_by_value(max_value)
                print(f"Fibonacci series (up to {max_value}): {', '.join(map(str, series))}")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
