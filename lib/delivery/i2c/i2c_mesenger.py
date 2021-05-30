import smbus


class I2cMessenger:
    def __init__(self, device_addr):
        self.device_addr = device_addr
        self.bus = smbus.SMBus(1)

    @staticmethod
    def convert_strings_to_bytes(src):
        converted = []
        for b in src:
            converted.append(ord(b))

        return converted

    def send(self, cmd):
        bytes_to_send = self.convert_strings_to_bytes(cmd)

        self.bus.write_i2c_block_data(self.device_addr, 0x00, bytes_to_send)