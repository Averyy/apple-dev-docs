# SetPreferredOutputChannelLayout

**Framework**: VideoDriverKit  
**Kind**: method

Sets the output channel layout.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t SetPreferredOutputChannelLayout(IOUserVideoChannelLabel *in_channel_labels, size_t in_num_channels);
```

## Parameters

- `in_channel_labels`: An array of channel labels.
- `in_num_channels`: The number of items in the array.

## See Also

- [SetPreferredChannelsForStereo](iouservideodevice/setpreferredchannelsforstereo.md)
  Sets the channel indices for the preferred stereo pair
- [GetPreferredChannelsForStereo](iouservideodevice/getpreferredchannelsforstereo.md)
  Gets the channel indices for the preferred stereo pair.
- [SetPreferredInputChannelLayout](iouservideodevice/setpreferredinputchannellayout.md)
  Sets the input channel layout with IOUserVideoChannelLabel values
- [IOUserVideoChannelLabel](videodriverkit/iouservideochannellabel.md)
  These constants are to set the preferred channel layout on video device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/setpreferredoutputchannellayout)*