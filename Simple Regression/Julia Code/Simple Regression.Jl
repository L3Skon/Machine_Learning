using Markdown

md"Import Librairies"
using CSV, DataFrames, Dates
using MLJ

md"Read data using .csv file, covert it to DataFrame object"
df = CSV.read("GlobalLandTemperaturesByCity.csv", DataFrame)
schema(df)


md"Filter the data for a specifio region and select eh Year and temperature columns"
region = df[df[!, "City"].== "Århus", ["dt", "AverageTemperature"]]

