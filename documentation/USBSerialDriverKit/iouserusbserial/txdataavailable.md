# TxDataAvailable

**Framework**: USBSerialDriverKit  
**Kind**: method

Notifies your driver that the system has data for you to transmit to the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
void TxDataAvailable();
```

#### Discussion

The default implementation of this method initiates an asynchronous operation to transmit the buffered data to the device.

## See Also

- [handleRxPacket](iouserusbserial/handlerxpacket.md)
  Processes the data received from the USB device.
- [RxFreeSpaceAvailable](iouserusbserial/rxfreespaceavailable.md)
  Notifies your driver that buffer space is available for your device’s data.
- [handleInterruptPacket](iouserusbserial/handleinterruptpacket.md)
  Processes an interrupt packet that originated from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbserialdriverkit/iouserusbserial/txdataavailable)*