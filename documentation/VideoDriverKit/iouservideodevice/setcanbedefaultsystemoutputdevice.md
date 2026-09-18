# SetCanBeDefaultSystemOutputDevice

**Framework**: VideoDriverKit  
**Kind**: method

Specifies if device can be used as default system output device

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetCanBeDefaultSystemOutputDevice(bool in_can_be_default);
```

#### Discussion

The object’s work queue synchronizes access to the value.

## Parameters

- `in_can_be_default`: True if device can be used as default system output device by the host.

## See Also

- [SetCanBeDefaultInputDevice](iouservideodevice/setcanbedefaultinputdevice.md)
  Specify if device can be used as default input device.
- [CanBeDefaultInputDevice](iouservideodevice/canbedefaultinputdevice.md)
  Returns a Boolean value indicating if device can be used for default input.
- [SetCanBeDefaultOutputDevice](iouservideodevice/setcanbedefaultoutputdevice.md)
  Specifies if device can be used as default output device.
- [CanBeDefaultOutputDevice](iouservideodevice/canbedefaultoutputdevice.md)
  Returns a Boolean value indicating if device can be used for default output.
- [CanBeDefaultSystemOutputDevice](iouservideodevice/canbedefaultsystemoutputdevice.md)
  Returns a Boolean value indicating if device can be used for default system output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/setcanbedefaultsystemoutputdevice)*