# SetDeviceIsAlive

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetDeviceIsAlive(bool in_is_alive);
```

#### Return Value

Returns kern_return_t

#### Discussion

Set bool to indicate the device is alive.

A bool where true means the device is ready and available and false means the device is unusable and will most likely go away shortly.

## Parameters

- `in_is_alive`: True if device is alive.

## See Also

- [GetDeviceIsRunning](iouservideoclockdevice/getdeviceisrunning.md)
- [GetDeviceIsAlive](iouservideoclockdevice/getdeviceisalive.md)
- [SetIsHidden](iouservideoclockdevice/setishidden.md)
- [GetIsHidden](iouservideoclockdevice/getishidden.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/setdeviceisalive)*