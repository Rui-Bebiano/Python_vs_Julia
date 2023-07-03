using DataFrames
using BenchmarkTools
using CSV

# Fibonacci function - iterative implementation
function fibonacci(n)
    a, b = 0, 1
    for _ in 1:n
        a, b = b, a + b
    end
    return a
end

# Initialize a DataFrame to store the results
df_julia = DataFrame(Run = Int[], Time = Float64[])

# Define the number of runs on each batch
num_runs = 100

# Warm up the JIT compiler
fibonacci(1_000_000)

# Loop over the number of runs
println("Go, Julia!")
for i in 1:num_runs
    run_time = @elapsed fibonacci(1_000_000)
    push!(df_julia, [i run_time])
	println("Run: $(i)")
end

#println(df_julia)
CSV.write("Output.csv", df_julia)
