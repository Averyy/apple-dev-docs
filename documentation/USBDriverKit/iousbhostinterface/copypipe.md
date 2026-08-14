# CopyPipe

**Framework**: USBDriverKit  
**Kind**: method

Returns the pipe for the specified endpoint address.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
virtual kern_return_t CopyPipe(uint8_t address, IOUSBHostPipe **pipe);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes).

#### Discussion

If the specified pipe doesn’t exist yet, but is part of the interface, this method creates the pipe before returning it.

## Parameters

- `address`: The address of the pipe you want. Get the address for a specific pipe from the [`bEndpointAddress`](iousbendpointdescriptor/bendpointaddress.md) field of the appropriate [`IOUSBEndpointDescriptor`](iousbendpointdescriptor.md) structure.
- `pipe`: A variable in which to store the [`IOUSBHostPipe`](iousbhostpipe.md) object. It’s your responsibility to release this object when you finish using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/copypipe)*