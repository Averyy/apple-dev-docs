# IOUserUSBSerial

**Framework**: Usbserialdriverkit  
**Kind**: class

A service that manages a serial connection to a USB device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
class IOUserUSBSerial;
```

#### Overview

Subclass `IOUserUSBSerial` to implement a driver that communicates with a USB device serially. After matching your driver to the appropriate device, the system starts your driver and calls its [`HwActivate`](iouserusbserial/hwactivate.md) method, which you use to open and configure the communications channel for your device. Configure other hardware-related settings by overriding the appropriate methods defined in the [`IOUserSerial`](https://developer.apple.com/documentation/SerialDriverKit/IOUserSerial) parent class.

This class automatically manages the serial communications with the device, buffering data received from it. The class creates the buffers for holding data, and initiates asynchronous operations to the USB device to transmit and receive data. Use the methods of this class to modify the data, as needed.

## Topics

### Configuring the Service
- [init](iouserusbserial/init.md)
  Handles the basic initialization of the service.
- [Start](iouserusbserial/start.md)
  Starts the service for the specified provider.
- [Stop](iouserusbserial/stop.md)
  Stops the service that matches the specified provider.
- [free](iouserusbserial/free.md)
  Performs any final cleanup for the service.
- [initWith](iouserusbserial/initwith.md)
  Initializes the private data structures associated with this class.
### Activating and Deactivating the Service
- [HwActivate](iouserusbserial/hwactivate.md)
  Opens the communication channel to the device.
- [HwDeactivate](iouserusbserial/hwdeactivate.md)
  Closes the communication channel to the device.
### Transmitting and Receiving Data
- [handleRxPacket](iouserusbserial/handlerxpacket.md)
  Processes the data received from the USB device.
- [RxFreeSpaceAvailable](iouserusbserial/rxfreespaceavailable.md)
  Notifies your driver that buffer space is available for your device’s data.
- [TxDataAvailable](iouserusbserial/txdataavailable.md)
  Notifies your driver that the system has data for you to transmit to the device.
- [handleInterruptPacket](iouserusbserial/handleinterruptpacket.md)
  Processes an interrupt packet that originated from the device.
### Configuring the Serial Data Queues
- [ConnectQueues](iouserusbserial/connectqueues.md)
  Creates and configures the buffers that store the data moving to and from the device.
- [DisconnectQueues](iouserusbserial/disconnectqueues.md)
  Releases the buffers that manage data moving to and from the device.

## See Also

- [com.apple.developer.driverkit.family.serial](../BundleResources/Entitlements/com.apple.developer.driverkit.family.serial.md)
  A Boolean value that indicates whether to match the driver against devices with serial communication interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbserialdriverkit/iouserusbserial)*