# wTransferSize

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

The maximum number of bytes that the device can accept per control-write transaction.

**Availability**:
- macOS 10.2+

## Declaration

```c
uint16_t wTransferSize;
```

## See Also

### Getting the Properties
- [bLength](./api-1546015-blength.md)
  The size of the descriptor.
- [bDescriptorType](./api-1546426-bdescriptortype.md)
  The type of the descriptor.
- [bmAttributes](./api-1546360-bmattributes.md)
  A bitmap encoding of supported device-level features.
- [wDetachTimeout](./api-1546084-wdetachtimeout.md)
  The time in milliseconds that the device waits after receipt of a detach request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdfudescriptor/1546379-wtransfersize)*