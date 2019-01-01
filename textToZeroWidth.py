def zeroPadding(n, paddingLen=8):
    return ('0' * paddingLen)[len(n):] + n


def textToBinary(text):
    def charToBinary(char):
        return zeroPadding(bin(ord(char[0]))[2:])  # remove the begging '0b'
    return ' '.join(map(charToBinary, text))


def binaryToZeroWidth(binary):
    def invisible(binaryChar):
        if binaryChar == '1':
            return chr(8203)  # invisible, 8203 zero-width space
        elif binaryChar == '0':
            return chr(8204)  # invisible, 8204 zero-width non-joiner
        else:
            return chr(8205)  # invisible, 8205 zero-width joiner
    return chr(65279).join(map(invisible, binary))  # invisible, 65279 zero-width no-break space


def putOnInvisibleCloak(wantToHide):
    return binaryToZeroWidth(textToBinary(wantToHide))
