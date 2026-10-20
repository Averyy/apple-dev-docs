# HwActivate

**Framework**: USBSerialDriverKit  
**Kind**: method  
**Role**: Instance Method

Opens the communication channel to the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t HwActivate();
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

Override this method and use it to prepare your device’s hardware for serial communication. Always call the `super` version of the method at the beginning of your implementation.

## See Also

### Activating and Deactivating the Service
- [HwDeactivate](./hwdeactivate.md)
  Closes the communication channel to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbserialdriverkit/iouserusbserial/hwactivate)*