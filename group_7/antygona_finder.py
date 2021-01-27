import json

from urgent_pointer_part import UrgentPointerPart


class AntygonaFinder:
    def __init__(self):
        file = open("tcp_urgent_non_zero.json", "r")
        self.TCP_PACKAGES = json.load(file)

    def write_antygona_candidates(self):
        f = open('./output/antygona_decoded.txt', "w")

        for package in self.TCP_PACKAGES:
            request_param_package = UrgentPointerPart(package)
            text = request_param_package.get_text()
            if text is not None:
                f.write(text)
        f.close()
