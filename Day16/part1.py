
from solver import Solver


class Part1(Solver):
    def __init__(self):
        self.bits = ''

    def _get_bits_str(self, count: int) -> str:
        if len(self.bits) < count:
            return None

        value = self.bits[:count]
        self.bits = self.bits[count:]
        return value

    def _get_bits_int(self, count: int) -> int:
        if len(self.bits) < count:
            return None

        value = int(self.bits[:count], 2)
        self.bits = self.bits[count:]
        return value

    def process(self, input: str) -> None:
        for ch in input:
            self.bits += f'{int(ch, 16):04b}'

    def finish(self) -> int:
        version_sum = 0
        while len(self.bits) > 6:
            version = self._get_bits_int(3)
            type_id = self._get_bits_int(3)

            version_sum += version

            if type_id == 4:
                value = 0
                prefix = '1'
                while prefix == '1':
                    prefix = self._get_bits_str(1)
                    nibble = self._get_bits_int(4)
                    value <<= 4
                    value += nibble
            else:
                length_type_id = self._get_bits_str(1)
                if length_type_id == '1':
                    num_sub_packets = self._get_bits_int(11)
                else:
                    total_length_bits = self._get_bits_int(15)

        return version_sum
