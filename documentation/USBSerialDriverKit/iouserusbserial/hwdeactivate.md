# HwDeactivate

**Framework**: Usbserialdriverkit  
**Kind**: method

Closes the communication channel to the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t HwDeactivate();
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Override this method and use it to close the connection to your device’s hardware. Always call the `super` version of the method at the end of your implementation.

## See Also

- [HwActivate](iouserusbserial/hwactivate.md)
  Opens the communication channel to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbserialdriverkit/iouserusbserial/hwdeactivate)*