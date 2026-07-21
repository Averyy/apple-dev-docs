# CanBeDefaultOutputDevice

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
uint32_t CanBeDefaultOutputDevice();
```

#### Return Value

Returns bool, true if device can be used for default output.

#### Discussion

Get bool value indiciating if device can be used for default output.

Getting the value will be synchronized using the work queue created by the object.

## See Also

- [SetCanBeDefaultInputDevice](iouservideodevice/setcanbedefaultinputdevice.md)
- [CanBeDefaultInputDevice](iouservideodevice/canbedefaultinputdevice.md)
- [SetCanBeDefaultOutputDevice](iouservideodevice/setcanbedefaultoutputdevice.md)
- [SetCanBeDefaultSystemOutputDevice](iouservideodevice/setcanbedefaultsystemoutputdevice.md)
- [CanBeDefaultSystemOutputDevice](iouservideodevice/canbedefaultsystemoutputdevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/canbedefaultoutputdevice)*