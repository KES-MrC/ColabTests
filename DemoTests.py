from unittest.mock import patch
from io import StringIO

passed_str = "\033[0;32mPassed\033[0;30m"
failed_str = "\033[0;31mFailed\033[0;30m"

test_cases = [
    [["Ada"], "Hello, Ada!"],
    [["Bob"], "Hello, Bob!"],
    [["Cat"], "Hello, Cat!"]
]

hidden_test_cases = [
    [["Dan"], "Hello, Dan!"],
    [[""], "Hello, !"],
    [["Rumpelstiltskin"], "Hello, Rumpelstiltskin!"]
]

def test_function_with_input(func, simulated_input, expected_output):
  """
  Tests a function that uses input() for name and checks printed output.

  Args:
    func: The function to test.
    simulated_input: A list of strings representing simulated user input.
    expected_output: The expected output of the function.

  Returns:
    True if the function's output matches the expected output, False otherwise.
  """
  with patch('builtins.input', side_effect=simulated_input), \
       patch('sys.stdout', new=StringIO()) as fake_out:
    func()
    printed_output = fake_out.getvalue().strip()
    return printed_output == expected_output

def run_tests():
  print("Don't forget to rerun the codeblock that defines your function each time you make changes...\n")
  function_name = "greeting"
  if not any([s == function_name for s in globals()]):
    print(f"Function {function_name} not found")
    print("Make sure you run the code block with your function and check the name")
  else:
    for i in range(len(test_cases)):
      print(f"Test case {i+1}, {test_cases[i][0][0]}: ", end="\t")
      if test_function_with_input(greeting, test_cases[i][0], test_cases[i][1]):
        print(passed_str)
      else:
        print(failed_str)

    for i in range(len(test_cases)):
      print(f"Hidden test case {i+1}: ", end="\t")
      if test_function_with_input(greeting, hidden_test_cases[i][0], hidden_test_cases[i][1]):
        print(passed_str)
      else:
        print(failed_str)
