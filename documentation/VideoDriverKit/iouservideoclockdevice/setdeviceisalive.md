# SetDeviceIsAlive

**Framework**: VideoDriverKit  
**Kind**: method

Sets a Boolean value to indicate the device is alive.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetDeviceIsAlive(bool in_is_alive);
```

#### Discussion

A true  value means the device is ready and available and false means the device is unusable and will most likely go away shortly.

## Parameters

- `in_is_alive`: True if device is alive.

## See Also

- [GetDeviceIsRunning](iouservideoclockdevice/getdeviceisrunning.md)
  Gets bool value indicating if device is running.
- [GetDeviceIsAlive](iouservideoclockdevice/getdeviceisalive.md)
  Gets a Boolean value indicating if the device is alive.
- [SetIsHidden](iouservideoclockdevice/setishidden.md)
  Sets a Boolean value indicating if the device is hidden.
- [GetIsHidden](iouservideoclockdevice/getishidden.md)
  Gets a Boolean value indicating if the device is hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/setdeviceisalive)*