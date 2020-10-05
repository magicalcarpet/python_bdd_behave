# Python BDD using Behave

This is going to an example of BDD using the Behave tool.

# Motivation

I like to use BDD and this is a Python version.

# Demo

TODO

# Libraries Used

*Behave* Is a BDD testing tool inspired Cucumber.

*Invoke* Is a taskrunner. A taskrunner may be thought of as a tool to automate common taks for the sake of efficiency.

# Prerequisites

For this project we're gonna use Pipenv if you don't have installed follow 
the instructions here:

```http
https://pipenv-fork.readthedocs.io/en/latest/#install-pipenv-today
```

# Setup locally

Change into the virtual envirnment and then install dependencies and finally
we execute the behave tests.

Step 1. 
Change into the virtual environment by typing:

```console
pipenv shell
```
Step 2. 

```console
Pipenv install -r requirements.txt
```
Step 3.
Execute the tests:

```console
behave
```

# Run tests with invoke

Check if invoke is installed by typing the following into terminal (within the pipenv environment):

```console
invoke --version
```
You should see something like this:

```console
Invoke 1.4.1
```
To list the invoke tasks into terminal:

```console
invoke -l
```

And see something like this:

```console
Available tasks:

  list-file-in-directory
  run-all-tests
  run-test-with-tag        In order to run this task from command line we can for example
```

To run a specific task type the following into terminal:

```console
TAGGED_TEST=@add invoke run-test-with-tag
```

The TAGGED_TEST is an environment variable which maps into a tag. The name
was my choice rather than necessary code.

```console
Feature: Calculator Functions # features/calculator.feature:1

  @add
  Scenario: Addition                      # features/calculator.feature:4
    Given the first number is inputted    # features/steps/addition_steps.py:1
hello first number
    And the addition button is pressed    # features/steps/addition_steps.py:5
We pressed the addition button
    And the second number is inputted     # features/steps/addition_steps_two.py:1
The second number is now inputted
    When the equals button is pressed     # features/steps/addition_steps_two.py:5
The equals button is pressed
    Then we should see the correct result # features/steps/addition_steps_two.py:10
Correct result

  @division
  Scenario: Division                   # features/calculator.feature:12
    Given the numerator is inputted    # None
    And the division button is pressed # None
    And the denominator is inputted    # None
    And the equals sign is pressed     # None
    Then the dividend is displayed     # None

  Scenario: Multiplication  # features/calculator.feature:20

  Scenario: Subtraction  # features/calculator.feature:23

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 3 skipped
5 steps passed, 0 failed, 5 skipped, 0 undefined
Took 0m0.001s
```

