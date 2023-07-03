# Python_vs_Julia
A test to compare the speed of Python and Julia

This repository contains code used in a project to compare the performance of Python and Julia languages, by means of the iterative implementation of the Fibonacci function.

![DALL·E 2023-07-03 01 37 34 - A rabbit speeds to win a race against a turtle](https://github.com/Rui-Bebiano/Python_vs_Julia/assets/124524010/8d71f53e-4472-466e-bc5f-da864141711f)

## Objective
The aim of this project was to compare the execution times of Python and Julia when running the Fibonacci function with a large input size, under controlled and repeatable conditions. This comparison can help understand the performance characteristics of these two popular programming languages - namely, to confirm that while having a similar syntax to Python, Julia can be a few orders of magnitude faster.

## Methodology
The Fibonacci function was implemented using an identical simple iterative approach in both Python and Julia. Each implementation was run multiple times (in batches of 10), for n=1.000.000, and the execution time was recorded for each run. The results were stored in dataframes, which contents where then saved on a csv file.
All tests were conducted on the same machine under similar load conditions to ensure a fair comparison.

## Contents
fibonacci_python.py: This file contains the Python implementation of the Fibonacci function and the code to measure its execution time.

fibonacci_julia.jl: This file contains the Julia implementation of the Fibonacci function and the code to measure its execution time.

Comparison.xlsx: An Excel file containing the analysis of the results obtained from the Python and Julia runs.

## How to Run
You'll need Python and Julia installed on your machine to run the code.

Run the Python code: python fibonacci_python.py

Run the Julia code: julia fibonacci_julia.jl


## Results
The detailed results and analysis are provided in the Comparison.xlsx file. In summary, the results indicated that Julia performed the Fibonacci iterative calculation significantly faster than Python on average - in this case, about 7300 times faster. Nevertheless, Julia's recorded times exhibited about twice the dispersion and 10 times the (positive) skew of those of Python.

## Contributions
Your feedback is welcome! Feel free to open an issue.
