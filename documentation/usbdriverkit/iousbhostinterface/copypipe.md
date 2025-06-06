# CopyPipe

**Framework**: USBDriverKit  
**Kind**: method

Returns the pipe for the specified endpoint address.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t CopyPipe(uint8_t address, IOUSBHostPipe * * pipe);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If the specified pipe doesn’t exist yet, but is part of the interface, this method creates the pipe before returning it.

## Parameters

- `address`: The address of the pipe you want. Get the address for a specific pipe from the   field of the appropriate   structure.
- `pipe`: A variable in which to store the   object. It’s your responsibility to release this object when you finish using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/copypipe)*