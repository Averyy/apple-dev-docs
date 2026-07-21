# CanBeDefaultInputDevice

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
uint32_t CanBeDefaultInputDevice();
```

#### Return Value

Returns bool, true if device can be used for default input.

#### Discussion

Get bool value indiciating if device can be used for default input.

Getting the value will be synchronized using the work queue created by the object.

## See Also

- [SetCanBeDefaultInputDevice](iouservideodevice/setcanbedefaultinputdevice.md)
- [SetCanBeDefaultOutputDevice](iouservideodevice/setcanbedefaultoutputdevice.md)
- [CanBeDefaultOutputDevice](iouservideodevice/canbedefaultoutputdevice.md)
- [SetCanBeDefaultSystemOutputDevice](iouservideodevice/setcanbedefaultsystemoutputdevice.md)
- [CanBeDefaultSystemOutputDevice](iouservideodevice/canbedefaultsystemoutputdevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/canbedefaultinputdevice)*