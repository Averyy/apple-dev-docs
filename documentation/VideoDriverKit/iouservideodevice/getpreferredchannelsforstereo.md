# GetPreferredChannelsForStereo

**Framework**: VideoDriverKit  
**Kind**: method

Gets the channel indices for the preferred stereo pair.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
void GetPreferredChannelsForStereo(uint32_t *out_left_channel, uint32_t *out_right_channel);
```

## Parameters

- `out_left_channel`: Pointer to a uint32_t channel index for the preferred stereo left channel.
- `out_right_channel`: Pointer to a uint32_t channel index for the preferred stereo right channel.

## See Also

- [SetPreferredChannelsForStereo](iouservideodevice/setpreferredchannelsforstereo.md)
  Sets the channel indices for the preferred stereo pair
- [SetPreferredInputChannelLayout](iouservideodevice/setpreferredinputchannellayout.md)
  Sets the input channel layout with IOUserVideoChannelLabel values
- [SetPreferredOutputChannelLayout](iouservideodevice/setpreferredoutputchannellayout.md)
  Sets the output channel layout.
- [IOUserVideoChannelLabel](videodriverkit/iouservideochannellabel.md)
  These constants are to set the preferred channel layout on video device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/getpreferredchannelsforstereo)*