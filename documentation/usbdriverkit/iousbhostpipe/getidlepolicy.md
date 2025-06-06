# GetIdlePolicy

**Framework**: USBDriverKit  
**Kind**: method

Retrieves the pipe’s current idle timeout.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t GetIdlePolicy(uint32_t * idleTimeoutMS);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

## Parameters

- `idleTimeoutMS`: A pointer to store the current idle timeout in milliseconds.

## See Also

- [SetIdlePolicy](iousbhostpipe/setidlepolicy.md)
  Sets the pipe’s desired idle timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/getidlepolicy)*