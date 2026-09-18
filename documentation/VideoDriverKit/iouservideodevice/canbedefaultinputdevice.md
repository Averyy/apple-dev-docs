# CanBeDefaultInputDevice

**Framework**: VideoDriverKit  
**Kind**: method

Returns a Boolean value indicating if device can be used for default input.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
uint32_t CanBeDefaultInputDevice();
```

#### Return Value

True if device can be used for default input.

#### Discussion

The object’s work queue synchronizes access to the value.

## See Also

- [SetCanBeDefaultInputDevice](iouservideodevice/setcanbedefaultinputdevice.md)
  Specify if device can be used as default input device.
- [SetCanBeDefaultOutputDevice](iouservideodevice/setcanbedefaultoutputdevice.md)
  Specifies if device can be used as default output device.
- [CanBeDefaultOutputDevice](iouservideodevice/canbedefaultoutputdevice.md)
  Returns a Boolean value indicating if device can be used for default output.
- [SetCanBeDefaultSystemOutputDevice](iouservideodevice/setcanbedefaultsystemoutputdevice.md)
  Specifies if device can be used as default system output device
- [CanBeDefaultSystemOutputDevice](iouservideodevice/canbedefaultsystemoutputdevice.md)
  Returns a Boolean value indicating if device can be used for default system output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/canbedefaultinputdevice)*