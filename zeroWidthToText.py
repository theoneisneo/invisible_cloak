def zeroWidthToBinary(invisible):
    def reveal(invisibleChar):
        if invisibleChar == chr(8203):  # invisible, 8203 zero-width space
            return '1'
        elif invisibleChar == chr(8204):  # invisible, 8204 zero-width non-joiner
            return '0'
        elif invisibleChar == chr(8205):  # invisible, 8205 zero-width joiner
            return ' '
        else:  # infact, this part should only have invisible, 65279 zero-width no-break space
            return ''
    return ''.join(map(reveal, invisible))


def binaryToText(binary):
    def binaryToChar(binaryChar):
        return chr(int(binaryChar, 2))
    return ''.join(map(binaryToChar, binary.split(' ')))


def takeOffInvisibleCloak(wantToSee):
    return binaryToText(zeroWidthToBinary(wantToSee))
