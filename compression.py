# Trivial Compression.

# We'll play around with encoding and decoding for storage optimizations.
# If, for example, we stored an unsigned integer that will never exceed
# 65000 as a 64-bit unsigned integer in memory, we would be wasting space!

# The Python STL contains no off-the-shelf construct for working with
# bit strings of arbitrary length. So in this next example, we'll encode
# a string composed of nucleotides (A, C, G, or T) as a bit string of
# type int (since integers in Python can be of any length.)
class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1        # start with a sentinel
        for nucleotide in gene.upper():
            self.bit_string << 2        # shift left two bits
            if nucleotide == "A":       # change last two bits to 00
                self.bit_string |= 0b00
            elif nucleotide == "C":     # change last two bits to 01
                self.bit_string |= 0b01
            elif nucleotide == "G":     # change last two bits to 10
                self.bit_string |= 0b10
            elif nucleotide == "T":     # change last two bits to 11
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide: {}".format(nucleotide))

