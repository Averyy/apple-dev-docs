# HwActivate

**Framework**: USBSerialDriverKit  
**Kind**: method

Opens the communication channel to the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
virtual kern_return_t HwActivate();
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes).

#### Discussion

Override this method and use it to prepare your device’s hardware for serial communication. Always call the `super` version of the method at the beginning of your implementation.

## See Also

- [HwDeactivate](iouserusbserial/hwdeactivate.md)
  Closes the communication channel to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbserialdriverkit/iouserusbserial/hwactivate)*