from lib.delivery.i2c.i2c_mesenger import I2cMessenger


class TerrariumI2cMessenger(I2cMessenger):
    I2C_DEVICE_ADDR = 11

    SET_TARGET_TEMP_MESSAGE = 10000
    SET_TEMP_OFFSET_MESSAGE = 11000
    SET_TEM_LOCK_MESSAGE = 12000
    TOGGLE_THERMOSTAT_MESSAGE = 13000
    THERMOSTAT_STATUS_MESSAGE = 14000

    def __init__(self):
        super().__init__(self.I2C_DEVICE_ADDR)

    def create_message_from_input(self, message_ref, param, value):
        message = message_ref + param * 1000 + value

        return message

    def set_target_temp(self, section, target_temp):
        return self.send(
            self.create_message_from_input(self.SET_TARGET_TEMP_MESSAGE, section, target_temp)
        )

    def set_temp_offset(self, section, temp_offset):
        return self.send(
            self.create_message_from_input(self.SET_TEMP_OFFSET_MESSAGE, section, temp_offset)
        )

    def set_temp_lock(self, section, temp_lock):
        return self.send(
            self.create_message_from_input(self.SET_TEM_LOCK_MESSAGE, section, temp_lock)
        )

    def thermostat_status(self, section):
        # return self.send(
        #     self.create_message_from_input(self.THERMOSTAT_STATUS_MESSAGE, section, 0)
        # )
        pass

    def toggle_thermostat(self, section):
        return self.send(
            self.create_message_from_input(self.TOGGLE_THERMOSTAT_MESSAGE, section, 0)
        )
