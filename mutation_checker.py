import logging
from Bio import SeqIO


class MutationChecker:
    def __init__(self, input_fasta: str):
        self.input_fasta = input_fasta

    def check_sequence_completeness(
        self, sequence: str, sequence_id: str
    ) -> (bool, str):
        mutation = str()
        stop_codons = {"taa", "tga", "tag"}
        complete = True
        if len(sequence) % 3 != 0:
            complete = False
        i = 0
        # -6 so you don't check the last codon (which should be a stop codon)
        while i <= len(sequence) - 6 and complete:
            codon = sequence[i : i + 3]
            if codon in stop_codons:
                mutation = (
                    f"stop codon {codon} at position {i + 1}-{i + 3} in {sequence_id}"
                )
                logging.info(f"{mutation}")
                complete = False
            i += 3
        return complete, mutation

    def find_mutations(self) -> list:
        disruptive_mutations_list = list()
        with open(f"{self.input_fasta}", "r") as seq:
            fasta_sequences = SeqIO.parse(seq, "fasta")
            for fasta in fasta_sequences:
                name = fasta.id
                sequence = str(fasta.seq).lower()
                disruptive_mutations = self.check_sequence_completeness(sequence, name)
                if disruptive_mutations[1]:
                    disruptive_mutations = disruptive_mutations[1].split(" ")
                    disruptive_mutations_dict = {
                        disruptive_mutations[-1]: disruptive_mutations[5]
                    }
                    disruptive_mutations_list.append(disruptive_mutations_dict)
        return disruptive_mutations_list

    def write_disruptive_mutations_file(self, mutations_file: str, mutations: list):
        with open(mutations_file, "w") as mut:
            mut.write("position,sequence\n")
            for i in range(0, len(mutations)):
                mutation_data = list(mutations[i].items())
                mut.write(f"{mutation_data[0][1]},{mutation_data[0][0]}\n")
