from common.asci_utils import *


class PackageSequencePart:
    def __init__(self, package):
        self.__seq = package['_source']['layers']['tcp']['tcp.seq_raw']

    def get_ascii(self, candidate_indexes):
        ascii_candidate = "".join(
            [self.__seq[candidate_indexes[0]], self.__seq[candidate_indexes[1]], self.__seq[candidate_indexes[2]]])
        int_value = int(ascii_candidate)
        if is_ascii_letter(int_value) or is_enter(int_value) or is_space(int_value):
            return chr(int_value)
        else:
            return None
