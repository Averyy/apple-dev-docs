# ClearStall

**Framework**: USBDriverKit  
**Kind**: method

Clears the halt condition of the pipe.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t ClearStall(bool withRequest);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

When a bulk or interrupt USB endpoint encounters an I/O error other than a timeout, it transitions to a halted state that you must clear if you want to perform additional I/O on the endpoint. Call this method to clear the halted condition for the endpoint. This method aborts all pending I/O on the endpoint and resets its data toggle.

If an intermediate hub is between the device and your driver, this method also sends a `CLEAR_TT_BUFFER` control request (USB 2.0, section 11.24.2.3) to the hub.

## Parameters

- `withRequest`: A Boolean indicating whether to send a   request to the device with the value  . To keep the device’s data toggle synchronized with the host’s data toggle, it’s recommended that you specify  , but you may safely specify   for control endpoints. For information about this request, see section 9.4.1 of the USB 2.0 specification.

## See Also

- [AdjustPipe](iousbhostpipe/adjustpipe.md)
  Adjusts the behavior of periodic endpoints to consume a different amount of bus bandwidth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/clearstall)*