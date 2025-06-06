# SetIdlePolicy

**Framework**: USBDriverKit  
**Kind**: method

Sets the desired idle suspend timeout for the interface.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t SetIdlePolicy(uint32_t deviceIdleTimeout);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

An idle device defers electrical suspension for the specified duration. By default, [`IOUSBHostInterface`](iousbhostinterface.md) doesn’t enable an idle policy, letting the device remain in the active state as long as the host machine is awake. Call this method to enable an idle policy for your device.

When you enable an idle policy and no I/O requests are pending, the system waits for the specified amount of time before electrically suspending the device. For a device with multiple interfaces, the system uses the largest timeout value from among all the open interfaces. A new I/O request during the wait period, or after suspension occurs, cancels the suspension and resumes I/O operations.

If the parent [`IOUSBHostDevice`](iousbhostdevice.md) object does not allow low-power mode for the device, the system disables idle suspension altogether.

## Parameters

- `deviceIdleTimeout`: The amount of time, in milliseconds, to wait after all pipes are idle before suspending the device. It is recommended that you choose an idle timeout value of 50 milliseconds or larger.

## See Also

- [GetFrameNumber](iousbhostinterface/getframenumber.md)
  Gets the current frame number of the USB controller.
- [GetPortStatus](iousbhostinterface/getportstatus.md)
  Gets the current port status.
- [SelectAlternateSetting](iousbhostinterface/selectalternatesetting.md)
  Selects an alternative setting for this interface.
- [GetIdlePolicy](iousbhostinterface/getidlepolicy.md)
  Gets the current idle suspend timeout for the interface.
- [tIOUSBHostPortStatus](tiousbhostportstatus.md)
  Constants indicating the state of a port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/setidlepolicy)*