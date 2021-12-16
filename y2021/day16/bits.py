# Coded in case day 17 needs the compiler again
import numpy
from typing import List


class BinString:
    def __init__(self, bs):
        self.bs = bs
        self.idx = 0

    def pop(self, n_bits, to_int=True):
        res = self.bs[self.idx: self.idx + n_bits]

        self.idx += n_bits

        if to_int:
            return int(res, base=2)

        return res

    def look(self, n_bits, to_int=True):
        res = self.bs[self.idx: self.idx + n_bits]


        if to_int:
            return int(res, base=2)

        return res

    def __bool__(self):
        return self.idx < len(self.bs)


class Packet:
    def __init__(self, v, t, r):
        self.v = v
        self.t = t
        self.r = r

    @staticmethod
    def parse(bs: BinString):
        v = bs.pop(3)
        t = bs.pop(3)

        match t:
            case 4:
                return LiteralPacket.parse_from_bin_str(v, t, bs)

            case _:
                return OperatorPacket.parse_from_bin_str(v, t, bs)


class LiteralPacket(Packet):
    def __init__(self, v, t, r: int):
        super().__init__(v, t, r)

    @classmethod
    def parse_from_bin_str(cls, v, t, bs: BinString):
        r = ''
        flag = 1
        while flag:
            flag = bs.pop(1)
            r += bs.pop(4, False)

        return cls(v, t, int(r, base=2))

    def eval(self):
        return self.r

    def __repr__(self):
        return f"Literal({self.v}: {self.r})"


class OperatorPacket(Packet):
    def __init__(self, v, t, r: List[Packet]):
        super().__init__(v, t, r)

    @classmethod
    def parse_from_bin_str(cls, v, t, bs: BinString):
        packets = []
        match bs.pop(1):
            case 0:
                length = bs.pop(15)
                sub_bs = BinString(bs.pop(length, False))

                while sub_bs:
                    packets.append(Packet.parse(sub_bs))

            case 1:
                n_packets = bs.pop(11)

                for _ in range(n_packets):
                    packets.append(Packet.parse(bs))

        return cls(v, t, packets)

    def eval(self):
        r = [p.eval() for p in self.r]
        match self.t:
            case 0:
                return sum(r)

            case 1:
                return numpy.prod(r)

            case 2:
                return min(r)

            case 3:
                return max(r)

            case 5:
                left, right = r
                return 1 if left > right else 0

            case 6:
                left, right = r
                return 1 if left < right else 0

            case 7:
                left, right = r
                return 1 if left == right else 0

    def __repr__(self):
        return f"Operator({self.v}, {self.t}: {self.r})"



def hex_to_bin(h):
    b = ''.join(f'{int(i, base=16):04b}' for i in h)
    return b


def read_input(filename):
    with open(filename, 'r') as f:
        line = next(f).strip()
        res = BinString(hex_to_bin(line))

    return res


if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    bin_str = read_input(input_file)

    packet = Packet.parse(bin_str)

    result = packet.eval()

    print(result)
