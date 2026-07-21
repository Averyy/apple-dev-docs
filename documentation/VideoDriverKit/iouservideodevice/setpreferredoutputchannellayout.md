# SetPreferredOutputChannelLayout

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetPreferredOutputChannelLayout(IOUserVideoChannelLabel *in_channel_labels, size_t in_num_channels);
```

#### Return Value

Returns kern_return_t

#### Discussion

Set the output channel layout with IOUserVideoChannelLabel values

## Parameters

- `in_channel_labels`: Array of IOUserVideoChannelLabel’s.
- `in_num_channels`: Number of items in in_channel_labels array

## See Also

- [SetPreferredChannelsForStereo](iouservideodevice/setpreferredchannelsforstereo.md)
- [GetPreferredChannelsForStereo](iouservideodevice/getpreferredchannelsforstereo.md)
- [SetPreferredInputChannelLayout](iouservideodevice/setpreferredinputchannellayout.md)
- [IOUserVideoChannelLabel](videodriverkit/iouservideochannellabel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/setpreferredoutputchannellayout)*