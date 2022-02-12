from solver import Solver


class Part2(Solver):
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

    def _parse_packet(self) -> dict:
        if len(self.bits) <= 6:
            return None

        version = self._get_bits_int(3)
        type_id = self._get_bits_int(3)
        length = 6
        value = 0
        sub_packets = []

        if type_id == 4:
            value = 0
            prefix = '1'
            while prefix == '1':
                prefix = self._get_bits_str(1)
                nibble = self._get_bits_int(4)
                value <<= 4
                value += nibble
                length += 5
        else:
            length_type_id = self._get_bits_str(1)
            length += 1
            if length_type_id == '1':
                sub_packets_count = self._get_bits_int(11)
                length += 11
                for _ in range(sub_packets_count):
                    sub_packet = self._parse_packet()
                    length += sub_packet['length']
                    sub_packets.append(sub_packet)
            else:
                sub_packets_total_length = self._get_bits_int(15)
                sub_packets_length = 0
                length += 15
                while sub_packets_length < sub_packets_total_length:
                    sub_packet = self._parse_packet()
                    length += sub_packet['length']
                    sub_packets_length += sub_packet['length']
                    sub_packets.append(sub_packet)

            if type_id == 0:
                value = 0
                for sub_packet in sub_packets:
                    value += sub_packet['value']
            elif type_id == 1:
                value = 1
                for sub_packet in sub_packets:
                    value *= sub_packet['value']
            elif type_id == 2:
                value = None
                for sub_packet in sub_packets:
                    if value is None:
                        value = sub_packet['value']
                    else:
                        value = min(value, sub_packet['value'])
            elif type_id == 3:
                value = None
                for sub_packet in sub_packets:
                    if value is None:
                        value = sub_packet['value']
                    else:
                        value = max(value, sub_packet['value'])
            elif type_id == 5:
                if len(sub_packets) != 2:
                    raise Exception('Invalid number of sub-packets')
                else:
                    if sub_packets[0]['value'] > sub_packets[1]['value']:
                        value = 1
                    else:
                        value = 0
            elif type_id == 6:
                if len(sub_packets) != 2:
                    raise Exception('Invalid number of sub-packets')
                else:
                    if sub_packets[0]['value'] < sub_packets[1]['value']:
                        value = 1
                    else:
                        value = 0
            elif type_id == 7:
                if len(sub_packets) != 2:
                    raise Exception('Invalid number of sub-packets')
                else:
                    if sub_packets[0]['value'] == sub_packets[1]['value']:
                        value = 1
                    else:
                        value = 0

        packet = {
            'version': version,
            'type_id': type_id,
            'length': length,
            'value': value,
        }

        if len(sub_packets):
            packet['sub_packets'] = sub_packets

        return packet

    def process(self, input: str) -> None:
        for ch in input:
            self.bits += f'{int(ch, 16):04b}'

    def finish(self) -> int:
        packet = self._parse_packet()
        return packet['value']
