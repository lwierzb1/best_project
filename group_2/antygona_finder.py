import json

from package_sequence_part import PackageSequencePart


def find_available_candidates():
    # sequenceNumber is 10 digit number
    candidates = set()
    for i in range(3):
        for j in range(3, 6):
            for k in range(6, 9):
                candidates.add((i, j, k))

    return candidates


class AntygonaFinder:
    def __init__(self):
        file = open("syn_1_seq_9.json", "r")
        self.TCP_PACKAGES = json.load(file)

    def write_antygona_candidates(self):
        candidates = find_available_candidates()
        for candidate in candidates:
            self.__print_to_file(candidate)

    def __print_to_file(self, candidate_indexes):
        f = open(f'./output/{candidate_indexes[0]}_{candidate_indexes[1]}_{candidate_indexes[2]}.txt', "w")

        for package in self.TCP_PACKAGES:
            sequence_package = PackageSequencePart(package)
            letter = sequence_package.get_ascii(candidate_indexes)
            if letter is not None:
                f.write(letter)
        f.close()
