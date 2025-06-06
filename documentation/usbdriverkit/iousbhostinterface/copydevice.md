# CopyDevice

**Framework**: USBDriverKit  
**Kind**: method

Returns the host device object that contains this interface.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t CopyDevice(IOUSBHostDevice * * device);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

## Parameters

- `device`: A variable in which to store the   object. It’s your responsibility to release this object when you finish using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/copydevice)*