import json

from package_request_param_part import PackageRequestParamPart

class AntygonaFinder:
    def __init__(self):
        file = open("covert", "r")
        self.TCP_PACKAGES = json.load(file)

    def write_antygona_candidates(self):
        f = open('./output/candidate.txt', "w")

        for package in self.TCP_PACKAGES:
            request_param_package = PackageRequestParamPart(package)
            letter = request_param_package.get_ascii()
            if letter is not None:
                f.write(letter)
