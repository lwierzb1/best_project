from common.asci_utils import *


class PackageRequestParamPart:
    def __init__(self, package):
        self.__DF_FLAG = package['_source']['layers']['ip']['ip.flags_tree']['ip.flags.df']
        self.__CWR_FLAG = package['_source']['layers']['tcp']['tcp.flags_tree']['tcp.flags.cwr']
        uri = package['_source']['layers']['http']['http.request.full_uri']
        self.__SECRET = get_request_param(uri)

    def get_ascii(self):
        ascii_byte = self.__secret_to_byte()
        int_value = int(ascii_byte)
        if is_letter(int_value) or is_enter(int_value) or is_space(int_value):
            return chr(int_value)
        else:
            return None

    def __secret_to_byte(self):
        byte = ""
        for x in self.__SECRET:
            if x.islower():
                byte = byte + "0"
            elif x.isupper():
                byte = byte + "1"
        return byte


def get_request_param(uri):
    uri_parts = uri.split('=')
    return uri_parts[1].replace('#', '')
