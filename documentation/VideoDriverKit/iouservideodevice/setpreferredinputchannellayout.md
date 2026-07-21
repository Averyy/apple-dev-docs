# SetPreferredInputChannelLayout

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetPreferredInputChannelLayout(IOUserVideoChannelLabel *in_channel_labels, size_t in_num_channels);
```

#### Return Value

Returns kern_return_t

#### Discussion

Set the input channel layout with IOUserVideoChannelLabel values

## Parameters

- `in_channel_labels`: Array of IOUserVideoChannelLabel’s.
- `in_num_channels`: Number of items in in_channel_labels array

## See Also

- [SetPreferredChannelsForStereo](iouservideodevice/setpreferredchannelsforstereo.md)
- [GetPreferredChannelsForStereo](iouservideodevice/getpreferredchannelsforstereo.md)
- [SetPreferredOutputChannelLayout](iouservideodevice/setpreferredoutputchannellayout.md)
- [IOUserVideoChannelLabel](videodriverkit/iouservideochannellabel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/setpreferredinputchannellayout)*