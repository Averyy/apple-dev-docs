# SetCanBeDefaultSystemOutputDevice

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetCanBeDefaultSystemOutputDevice(bool in_can_be_default);
```

#### Return Value

Returns kern_return_t

#### Discussion

Specify if device can be used as default system output device Setting the value will be synchronized using the work queue created by the object.

## Parameters

- `in_can_be_default`: True if device can be used as default system output device by the host.

## See Also

- [SetCanBeDefaultInputDevice](iouservideodevice/setcanbedefaultinputdevice.md)
- [CanBeDefaultInputDevice](iouservideodevice/canbedefaultinputdevice.md)
- [SetCanBeDefaultOutputDevice](iouservideodevice/setcanbedefaultoutputdevice.md)
- [CanBeDefaultOutputDevice](iouservideodevice/canbedefaultoutputdevice.md)
- [CanBeDefaultSystemOutputDevice](iouservideodevice/canbedefaultsystemoutputdevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/setcanbedefaultsystemoutputdevice)*