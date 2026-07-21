# GetDeviceIsAlive

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
bool GetDeviceIsAlive();
```

#### Return Value

Returns bool

#### Discussion

Get bool value indicating if the device is alive

Getting the value will be synchronized using the work queue created by the object. Default value with be true when the device is created.

## See Also

- [GetDeviceIsRunning](iouservideoclockdevice/getdeviceisrunning.md)
- [SetDeviceIsAlive](iouservideoclockdevice/setdeviceisalive.md)
- [SetIsHidden](iouservideoclockdevice/setishidden.md)
- [GetIsHidden](iouservideoclockdevice/getishidden.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getdeviceisalive)*