# Reset

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Terminates the device and attempts to reenumerate it.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t Reset();
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

This method resets and releases the current [`IOUSBHostDevice`](../iousbhostdevice.md) object and all of its children. If the reset and release of the device object are successful, this method creates a new [`IOUSBHostDevice`](../iousbhostdevice.md) object and registers it.

Don’t call this function from the port workloop thread.

## See Also

### Managing the Device Session
- [Open](./open.md)
  Opens a session to a host device.
- [Close](./close.md)
  Closes the session to the host device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice/reset)*