# SetIdlePolicy

**Framework**: USBDriverKit  
**Kind**: method

Sets the pipe’s desired idle timeout.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t SetIdlePolicy(uint32_t idleTimeoutMs);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

When a bulk or interrupt pipe is actively servicing an I/O request, it’s considered “busy” for the idle timeout value. For a more complete discussion of idle policies, refer to “Pausing IO” in `IOUSBHostFamily.h`.

## Parameters

- `idleTimeoutMs`: The amount of time, in milliseconds, before an active transfer is considered idle. If 0, the pipe isn’t considered idle if there’s an I/O request enqueued.

## See Also

- [GetIdlePolicy](iousbhostpipe/getidlepolicy.md)
  Retrieves the pipe’s current idle timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/setidlepolicy)*