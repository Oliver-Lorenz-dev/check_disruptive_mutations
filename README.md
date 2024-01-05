# check_disruptive_mutations
Python script which checks DNA sequences for disruptive mutations

## Description
This script checks sequences for disruptive mutations. It takes a FASTA file as input,
this can contain a single sequence or multiple sequences.

The script will output a file called `mutations.csv` which will contain information about any mutations that were found.
If a mutation is found, it will be included in the mutations file. Otherwise there will be no information about the sequence in the mutations file.

The mutations file follows the below format:
```csv
position,sequence
7-9,sequence_id
```

## Setup
Clone the repository:
```shell
git clone https://github.com/Oliver-Lorenz-dev/check_disruptive_mutations.git
cd check_disruptive_mutations
```

If you are using the Sanger farm5 server, load in the latest python module (ignore if you are not on the Sanger server):
```shell
module load ISG/python/3.11.2
```

Create a python virtual environment:
```shell
python3 -m venv venv
source venv/bin/activate
```

Install the required dependencies:
```shell
pip install -r requirements.txt
```

Run the example to check the installation was successful:
```shell
./check_disruptive_mutations.py -i example.fa
```

Check the output file contains the correct mutation:
```shell
cat mutations.csv
```

```shell
position,sequence
7-9,has_a_mutation
```

## Usage
```shell
usage: ./check_disruptive_mutations.py [-h] -i INPUT [-o OUTPUT]

options:
  -h, --help            show this help message and exit

required:
  -i INPUT, --input INPUT
                        Path to input fasta file (default: None)
  -o OUTPUT, --output OUTPUT
                        Path to output file (default: mutations.csv) (default: mutations.csv)
```
