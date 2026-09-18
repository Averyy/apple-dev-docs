# SetIsHidden

**Framework**: VideoDriverKit  
**Kind**: method

Sets a Boolean value indicating if the device is hidden.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetIsHidden(bool in_is_hidden);
```

#### Discussion

A bool value where true indicates that the device is not included in the normal list of devices provided and cannot be the default device. Hidden devices can only be discovered by it’s unique identifier

## Parameters

- `in_is_hidden`: True if device is hidden.

## See Also

- [GetDeviceIsRunning](iouservideoclockdevice/getdeviceisrunning.md)
  Gets bool value indicating if device is running.
- [SetDeviceIsAlive](iouservideoclockdevice/setdeviceisalive.md)
  Sets a Boolean value to indicate the device is alive.
- [GetDeviceIsAlive](iouservideoclockdevice/getdeviceisalive.md)
  Gets a Boolean value indicating if the device is alive.
- [GetIsHidden](iouservideoclockdevice/getishidden.md)
  Gets a Boolean value indicating if the device is hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/setishidden)*