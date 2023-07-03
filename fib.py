import pandas as pd
import timeit

#Fibonacci function - iterative implementation
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Initialize a DataFrame to store the results
df_python = pd.DataFrame(columns=['Run', 'Time'])

# Define the number of runs on each batch
num_runs = 10

# Loop over the number of runs
print("Go Python!")
for i in range(num_runs):
    start_time = timeit.default_timer()
    fibonacci(1_000_000)
    end_time = timeit.default_timer()
    run_time = end_time - start_time
    df_python = df_python.append({'Run': i+1, 'Time': run_time}, ignore_index=True)
    print(f'Run: {i+1}', end='\r')

print(df_python)
df_python.to_csv('Outputs.csv', index=False)