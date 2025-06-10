# handleInterruptPacket

**Framework**: USBSerialDriverKit  
**Kind**: method

Processes an interrupt packet that originated from the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
void handleInterruptPacket(const uint8_t * packet, uint32_t size);
```

#### Discussion

Override this method if you want to process interrupt packets sent by the device. The default implementation of this method does nothing.

## Parameters

- `packet`: A buffer containing the interrupt-related data.
- `size`: The number of bytes in the   buffer.

## See Also

- [handleRxPacket](iouserusbserial/handlerxpacket.md)
  Processes the data received from the USB device.
- [RxFreeSpaceAvailable](iouserusbserial/rxfreespaceavailable.md)
  Notifies your driver that buffer space is available for your device’s data.
- [TxDataAvailable](iouserusbserial/txdataavailable.md)
  Notifies your driver that the system has data for you to transmit to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbserialdriverkit/iouserusbserial/handleinterruptpacket)*