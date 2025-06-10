# handleRxPacket

**Framework**: USBSerialDriverKit  
**Kind**: method

Processes the data received from the USB device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
void handleRxPacket(uint8_t * & packet, uint32_t & size);
```

#### Discussion

The system calls this method after it receives raw data from the USB device, and before it moves that data to the read buffer. The default implementation of this method does nothing. You can override it, as needed, to modify the packet data or report any errors.

## Parameters

- `packet`: A pointer to a buffer that contains the raw packets received from the device.
- `size`: A pointer to the number of bytes in the   buffer.

## See Also

- [RxFreeSpaceAvailable](iouserusbserial/rxfreespaceavailable.md)
  Notifies your driver that buffer space is available for your device’s data.
- [TxDataAvailable](iouserusbserial/txdataavailable.md)
  Notifies your driver that the system has data for you to transmit to the device.
- [handleInterruptPacket](iouserusbserial/handleinterruptpacket.md)
  Processes an interrupt packet that originated from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbserialdriverkit/iouserusbserial/handlerxpacket)*