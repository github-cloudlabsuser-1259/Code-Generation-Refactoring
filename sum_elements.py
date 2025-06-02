#A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases

MAX = 100

def calculate_sum(arr: list) -> float:
   """
   Calculate the sum of all numeric elements in a list.

   Args:
      arr (list): A list containing numeric elements (integers or floats).

   Returns:
      float: The sum of all elements in the list.

   Raises:
      TypeError: If the input is not a list.
      ValueError: If any element in the list is not an integer or float.
   """
   if not isinstance(arr, list):
      raise TypeError("Input is not a list.")
   result = 0
   for num in arr:
      if not isinstance(num, (int, float)):
         raise ValueError("All elements must be integers or floats.")
      result += num
   return result

def main():
   try:
      user_input = input("Enter the number of elements (1-100): ")
      if not user_input.isdigit():
            raise ValueError("Invalid input. Please provide a digit ranging from 1 to 100.")
      n = int(user_input)
      if not 1 <= n <= MAX:
            print("Invalid input. Please provide a digit ranging from 1 to 100.")
            exit(1)

      arr = []

      print(f"Enter {n} integers:")
      for _ in range(n):
            while True:
               try:
                  arr.append(int(input()))
                  break
               except ValueError:
                  print("Invalid input. Please enter a valid integer.")
      if not arr:
         print("The list of numbers is empty. Cannot calculate the sum.")
         exit(1)

      total = calculate_sum(arr)

      print("The total sum of the entered numbers is:", total)

   except KeyboardInterrupt:
      print("\nProgram terminated by user.")
      exit(1)

if __name__ == "__main__":
   main()
