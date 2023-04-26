using Markdown

md"Import Librairies"
using CSV, DataFrames
using MLJ

md"Read data using .csv file, covert it to DataFrame object"
df = CSV.read("GlobalLandTemperaturesByCity.csv", DataFrame)
schema(df)


