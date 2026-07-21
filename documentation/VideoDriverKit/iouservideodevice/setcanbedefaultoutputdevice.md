# SetCanBeDefaultOutputDevice

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetCanBeDefaultOutputDevice(bool in_can_be_default);
```

#### Return Value

Returns kern_return_t

#### Discussion

Specify if device can be used as default output device.

Setting the value will be synchronized using the work queue created by the object.

## Parameters

- `in_can_be_default`: True if device can be used as default output device by the host.

## See Also

- [SetCanBeDefaultInputDevice](iouservideodevice/setcanbedefaultinputdevice.md)
- [CanBeDefaultInputDevice](iouservideodevice/canbedefaultinputdevice.md)
- [CanBeDefaultOutputDevice](iouservideodevice/canbedefaultoutputdevice.md)
- [SetCanBeDefaultSystemOutputDevice](iouservideodevice/setcanbedefaultsystemoutputdevice.md)
- [CanBeDefaultSystemOutputDevice](iouservideodevice/canbedefaultsystemoutputdevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/setcanbedefaultoutputdevice)*