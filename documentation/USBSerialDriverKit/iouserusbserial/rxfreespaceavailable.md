# RxFreeSpaceAvailable

**Framework**: USBSerialDriverKit  
**Kind**: method  
**Role**: Instance Method

Notifies your driver that buffer space is available for your device’s data.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual void RxFreeSpaceAvailable();
```

## Discussion

The default implementation of this method initiates an asynchronous operation to read data from the USB device.

## See Also

### Transmitting and Receiving Data
- [handleRxPacket](./handlerxpacket.md)
  Processes the data received from the USB device.
- [TxDataAvailable](./txdataavailable.md)
  Notifies your driver that the system has data for you to transmit to the device.
- [handleInterruptPacket](./handleinterruptpacket.md)
  Processes an interrupt packet that originated from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbserialdriverkit/iouserusbserial/rxfreespaceavailable)*