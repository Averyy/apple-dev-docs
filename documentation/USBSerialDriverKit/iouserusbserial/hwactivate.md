# HwActivate

**Framework**: Usbserialdriverkit  
**Kind**: method

Opens the communication channel to the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t HwActivate();
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Override this method and use it to prepare your device’s hardware for serial communication. Always call the `super` version of the method at the beginning of your implementation.

## See Also

- [HwDeactivate](iouserusbserial/hwdeactivate.md)
  Closes the communication channel to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbserialdriverkit/iouserusbserial/hwactivate)*