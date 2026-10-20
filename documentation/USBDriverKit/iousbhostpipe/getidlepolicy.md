# GetIdlePolicy

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Retrieves the pipe’s current idle timeout.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t GetIdlePolicy(uint32_t *idleTimeoutMS);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Parameters

- `idleTimeoutMS`: A pointer to store the current idle timeout in milliseconds.

## See Also

### Managing the Pipe’s Idle Policy
- [SetIdlePolicy](./setidlepolicy.md)
  Sets the pipe’s desired idle timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/getidlepolicy)*