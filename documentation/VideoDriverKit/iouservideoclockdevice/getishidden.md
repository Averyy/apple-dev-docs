# GetIsHidden

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
bool GetIsHidden();
```

#### Return Value

Returns bool

#### Discussion

Get bool value indicating if the device is hidden

Getting the value will be synchronized using the work queue created by the object. Default value with be false when the device is created.

## See Also

- [GetDeviceIsRunning](iouservideoclockdevice/getdeviceisrunning.md)
- [SetDeviceIsAlive](iouservideoclockdevice/setdeviceisalive.md)
- [GetDeviceIsAlive](iouservideoclockdevice/getdeviceisalive.md)
- [SetIsHidden](iouservideoclockdevice/setishidden.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getishidden)*