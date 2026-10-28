# CanBeDefaultInputDevice

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating if device can be used for default input.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
uint32_t CanBeDefaultInputDevice();
```

## Return Value

True if device can be used for default input.

## Discussion

The object’s work queue synchronizes access to the value.

## See Also

### Working with default device behavior
- [SetCanBeDefaultInputDevice](./setcanbedefaultinputdevice.md)
  Specify if device can be used as default input device.
- [SetCanBeDefaultOutputDevice](./setcanbedefaultoutputdevice.md)
  Specifies if device can be used as default output device.
- [CanBeDefaultOutputDevice](./canbedefaultoutputdevice.md)
  Returns a Boolean value indicating if device can be used for default output.
- [SetCanBeDefaultSystemOutputDevice](./setcanbedefaultsystemoutputdevice.md)
  Specifies if device can be used as default system output device
- [CanBeDefaultSystemOutputDevice](./canbedefaultsystemoutputdevice.md)
  Returns a Boolean value indicating if device can be used for default system output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/canbedefaultinputdevice)*