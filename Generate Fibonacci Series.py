def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

def main():
    try:
        n = int(input("Enter the number of terms for the Fibonacci sequence: "))
        if n <= 0:
            print("Please enter a positive integer for the number of terms.")
        else:
            result = generate_fibonacci(n)
            print(f"Fibonacci Sequence up to {n} terms: {result}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
