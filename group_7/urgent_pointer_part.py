class UrgentPointerPart:
    def __init__(self, package):
        self.__URGENT_POINTER = package['_source']['layers']['tcp']['tcp.urgent_pointer']

    def get_text(self):
        try:
            byte_array = self.__convert_urgent_pointer_to_byte_array()
            return byte_array.decode('ASCII')
        except UnicodeDecodeError:
            return None

    def __convert_urgent_pointer_to_byte_array(self):
        int_value = int(self.__URGENT_POINTER)
        hex_value = hex(int_value)[2:]
        if len(hex_value) % 2 != 0:
            hex_value = hex_value[:-1] + "0" + hex_value[-1:]
        return bytearray.fromhex(hex_value)
