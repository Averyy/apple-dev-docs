# CanBeDefaultOutputDevice

**Framework**: VideoDriverKit  
**Kind**: method

Returns a Boolean value indicating if device can be used for default output.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
uint32_t CanBeDefaultOutputDevice();
```

#### Return Value

True if device can be used for default output.

#### Discussion

The object’s work queue synchronizes access to the value.

## See Also

- [SetCanBeDefaultInputDevice](iouservideodevice/setcanbedefaultinputdevice.md)
  Specify if device can be used as default input device.
- [CanBeDefaultInputDevice](iouservideodevice/canbedefaultinputdevice.md)
  Returns a Boolean value indicating if device can be used for default input.
- [SetCanBeDefaultOutputDevice](iouservideodevice/setcanbedefaultoutputdevice.md)
  Specifies if device can be used as default output device.
- [SetCanBeDefaultSystemOutputDevice](iouservideodevice/setcanbedefaultsystemoutputdevice.md)
  Specifies if device can be used as default system output device
- [CanBeDefaultSystemOutputDevice](iouservideodevice/canbedefaultsystemoutputdevice.md)
  Returns a Boolean value indicating if device can be used for default system output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/canbedefaultoutputdevice)*