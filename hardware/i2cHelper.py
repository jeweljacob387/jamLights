
from smbus import SMBus

bus = SMBus(1)  # indicates /dev/ic2-1


def writeToDevice(addr, deviceIndex, state):
    try:
        bus.write_block_data(addr, deviceIndex, [state])  # replace with addr
    except:
        # print('IO ERROR')
        pass
