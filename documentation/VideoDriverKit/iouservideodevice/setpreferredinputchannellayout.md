# SetPreferredInputChannelLayout

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the input channel layout with IOUserVideoChannelLabel values

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t SetPreferredInputChannelLayout(IOUserVideoChannelLabel *in_channel_labels, size_t in_num_channels);
```

## Parameters

- `in_channel_labels`: An array channel labels.
- `in_num_channels`: The number of items in the array.

## See Also

### Working with channel layouts
- [SetPreferredChannelsForStereo](./setpreferredchannelsforstereo.md)
  Sets the channel indices for the preferred stereo pair
- [GetPreferredChannelsForStereo](./getpreferredchannelsforstereo.md)
  Gets the channel indices for the preferred stereo pair.
- [SetPreferredOutputChannelLayout](./setpreferredoutputchannellayout.md)
  Sets the output channel layout.
- [IOUserVideoChannelLabel](../videodriverkit-page/iouservideochannellabel.md)
  These constants are to set the preferred channel layout on video device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/setpreferredinputchannellayout)*