import argparse


class MutationCheckerParser:
    @classmethod
    def parse_args(cls, vargs=None):
        parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        )
        required = parser.add_argument_group("required")
        required.add_argument(
            "-i",
            "--input",
            required=True,
            help="Path to input fasta file",
        )
        required.add_argument(
            "-o",
            "--output",
            required=False,
            help="Path to output file (default: mutations.csv)",
            default="mutations.csv",
        )

        args = parser.parse_args(vargs)

        return args
