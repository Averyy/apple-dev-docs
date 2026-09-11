# SetPreferredChannelsForStereo

**Framework**: VideoDriverKit  
**Kind**: method

Sets the channel indices for the preferred stereo pair

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t SetPreferredChannelsForStereo(uint32_t in_left_channel, uint32_t in_right_channel);
```

## Parameters

- `in_left_channel`: The channel index for the left channel.
- `in_right_channel`: The channel index for the right channel.

## See Also

- [GetPreferredChannelsForStereo](iouservideodevice/getpreferredchannelsforstereo.md)
  Gets the channel indices for the preferred stereo pair.
- [SetPreferredInputChannelLayout](iouservideodevice/setpreferredinputchannellayout.md)
  Sets the input channel layout with IOUserVideoChannelLabel values
- [SetPreferredOutputChannelLayout](iouservideodevice/setpreferredoutputchannellayout.md)
  Sets the output channel layout.
- [IOUserVideoChannelLabel](videodriverkit/iouservideochannellabel.md)
  These constants are to set the preferred channel layout on video device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/setpreferredchannelsforstereo)*