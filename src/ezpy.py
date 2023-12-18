FAK3 = "YPCTF{Really?_You're_just_gonna_read_the_source?_That's_it?_That's_the_flag?}"

F1Ag = [0x4a, 0x43, 0x50, 0x47, 0x55, 0x68, 0x44, 0x76, 0x70, 0x23, 0x7e, 0x76, 0x4c, 0x67, 0x23, 0x4c, 0x67, 0x7b, 0x20, 0x4c, 0x64, 0x23, 0x61, 0x7f, 0x77, 0x4c, 0x23, 0x75, 0x4c, 0x63, 0x6a, 0x67, 0x5b, 0x23, 0x7d, 0x6e]

def check_flag(flag: str):
    buf = bytearray(flag.encode())
    if len(buf) != 36:
        return False
    for i in range(36):
        buf[i] ^= 0x13

    for i in range(36):
        if buf[i] != F1Ag[i]:
            return False
    return True


if __name__ == '__main__':
    flag = input('Wecloem to the world of Python, please input the flag: ')
    if check_flag(flag):
        print('Congrats! You got it!')
    else:
        print('Sorry, try again!')
