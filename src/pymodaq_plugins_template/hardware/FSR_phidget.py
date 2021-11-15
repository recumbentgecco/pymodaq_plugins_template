from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
import time


class FSR():

    def __init__(self):
        self.voltageRatioInput0 = VoltageRatioInput()
        self.voltageRatioInput0.setIsHubPortDevice(True)
        self.voltageRatioInput0.setHubPort(0)
        self.voltageRatioInput0.setDeviceSerialNumber(606461)
        self.voltageRatioInput0.openWaitForAttachment(5000)

    # def onSensorChange(self, sensorValue, sensorUnit):
    # 	print("SensorValue: " + str(sensorValue))
    # 	print("SensorUnit: " + str(sensorUnit.symbol))
    # 	print("----------")

    def get_Voltage(self):
        voltage = self.voltageRatioInput0.getVoltage()
        return (voltage)

    def close(self):
        self.voltageRatioInput0.close()

    def close_all():
        pass
