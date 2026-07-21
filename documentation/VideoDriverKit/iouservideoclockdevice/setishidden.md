# SetIsHidden

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetIsHidden(bool in_is_hidden);
```

#### Return Value

Returns kern_return_t

#### Discussion

Set bool value indicating if the device is hidden

A bool value where true indicates that the device is not included in the normal list of devices provided and cannot be the default device. Hidden devices can only be discovered by it’s unique identifier

## Parameters

- `in_is_hidden`: True if device is hidden.

## See Also

- [GetDeviceIsRunning](iouservideoclockdevice/getdeviceisrunning.md)
- [SetDeviceIsAlive](iouservideoclockdevice/setdeviceisalive.md)
- [GetDeviceIsAlive](iouservideoclockdevice/getdeviceisalive.md)
- [GetIsHidden](iouservideoclockdevice/getishidden.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/setishidden)*