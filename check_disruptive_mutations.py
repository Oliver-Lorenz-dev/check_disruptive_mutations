#!/usr/bin/env python3

from argparser import MutationCheckerParser
from mutation_checker import MutationChecker


def main(args):
    mutation_check = MutationChecker(args.input)

    mutations = mutation_check.find_mutations()

    mutation_check.write_disruptive_mutations_file(args.output, mutations)


if __name__ == "__main__":
    args = MutationCheckerParser.parse_args(vargs=None)
    main(args)
