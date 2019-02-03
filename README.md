# cs325-assignment1
### By: Drew Ortega, Taylor Griffin
closest pair of points implementation

The three closest pair algorithms can be run by executing the following commands on a machine with python3 installed.

## Brute Force
```bash
$ python3 brute_force.py path_to_input_file
```
Results are written to output_files/output_brute_force.txt

## Naive Divide & Conquer
```bash
$ python3 naive_dc.py path_to_input_file
```
Results are written to output_files/output_naive_dc.txt

## Enhanced Divide & Conquer
```bash
$ python3 enhanced_dc.py path_to_input_file
```
Results are written to output_files/output_enhanced_dc.txt

## Timing Analysis
To run any of the implementations with a timing printed to the standard output,
run as the following with the -v flag, after the specified input file:
```bash
$ python3 [IMPLEMENTATION_FILE].py path_to_input_file -v
```

## Generating input files
To generate a set of 10^2, 10^3, 10^4, 10^5, and 10^6 sized input files, do the following:
1) Ensure you are in the directory of the project in the terminal
2) Open the python3 interpreter
```bash
    $ python3
```
3) Import the helper file
```python
    import helper
```
4) run the generator function (create_samples)
```python
    helper.create_samples()
```
5) Wait for the generator to complete. Exit the python interpreter.
```python
    quit()
```
6) A new directory, 'randomly_generated_points/` will be in the project folder. Files are accurately named to represent input size. Use them with the algorithms in the syntax form specified earlier in the README.