# SetCanBeDefaultInputDevice

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetCanBeDefaultInputDevice(bool in_can_be_default);
```

#### Return Value

Returns kern_return_t

#### Discussion

Specify if device can be used as default input device.

Setting the value will be synchronized using the work queue created by the object.

## Parameters

- `in_can_be_default`: True if device can be used as default input device by the host.

## See Also

- [CanBeDefaultInputDevice](iouservideodevice/canbedefaultinputdevice.md)
- [SetCanBeDefaultOutputDevice](iouservideodevice/setcanbedefaultoutputdevice.md)
- [CanBeDefaultOutputDevice](iouservideodevice/canbedefaultoutputdevice.md)
- [SetCanBeDefaultSystemOutputDevice](iouservideodevice/setcanbedefaultsystemoutputdevice.md)
- [CanBeDefaultSystemOutputDevice](iouservideodevice/canbedefaultsystemoutputdevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/setcanbedefaultinputdevice)*