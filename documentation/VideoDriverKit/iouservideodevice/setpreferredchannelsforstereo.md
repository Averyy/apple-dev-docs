# SetPreferredChannelsForStereo

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the channel indices for the preferred stereo pair

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t SetPreferredChannelsForStereo(uint32_t in_left_channel, uint32_t in_right_channel);
```

## Parameters

- `in_left_channel`: The channel index for the left channel.
- `in_right_channel`: The channel index for the right channel.

## See Also

### Working with channel layouts
- [GetPreferredChannelsForStereo](./getpreferredchannelsforstereo.md)
  Gets the channel indices for the preferred stereo pair.
- [SetPreferredInputChannelLayout](./setpreferredinputchannellayout.md)
  Sets the input channel layout with IOUserVideoChannelLabel values
- [SetPreferredOutputChannelLayout](./setpreferredoutputchannellayout.md)
  Sets the output channel layout.
- [IOUserVideoChannelLabel](../videodriverkit-page/iouservideochannellabel.md)
  These constants are to set the preferred channel layout on video device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/setpreferredchannelsforstereo)*