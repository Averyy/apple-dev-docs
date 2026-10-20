# GetPreferredChannelsForStereo

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the channel indices for the preferred stereo pair.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
void GetPreferredChannelsForStereo(uint32_t *out_left_channel, uint32_t *out_right_channel);
```

## Parameters

- `out_left_channel`: Pointer to a uint32_t channel index for the preferred stereo left channel.
- `out_right_channel`: Pointer to a uint32_t channel index for the preferred stereo right channel.

## See Also

### Working with channel layouts
- [SetPreferredChannelsForStereo](./setpreferredchannelsforstereo.md)
  Sets the channel indices for the preferred stereo pair
- [SetPreferredInputChannelLayout](./setpreferredinputchannellayout.md)
  Sets the input channel layout with IOUserVideoChannelLabel values
- [SetPreferredOutputChannelLayout](./setpreferredoutputchannellayout.md)
  Sets the output channel layout.
- [IOUserVideoChannelLabel](../videodriverkit-page/iouservideochannellabel.md)
  These constants are to set the preferred channel layout on video device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/getpreferredchannelsforstereo)*