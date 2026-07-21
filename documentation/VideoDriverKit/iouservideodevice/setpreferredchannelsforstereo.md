# SetPreferredChannelsForStereo

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetPreferredChannelsForStereo(uint32_t in_left_channel, uint32_t in_right_channel);
```

#### Return Value

Returns kern_return_t

#### Discussion

Set the channel indices for the prefered stereo pair

## Parameters

- `in_left_channel`: uint32_t channel index for the left channel.
- `in_right_channel`: uint32_t channel index for the right channel.

## See Also

- [GetPreferredChannelsForStereo](iouservideodevice/getpreferredchannelsforstereo.md)
- [SetPreferredInputChannelLayout](iouservideodevice/setpreferredinputchannellayout.md)
- [SetPreferredOutputChannelLayout](iouservideodevice/setpreferredoutputchannellayout.md)
- [IOUserVideoChannelLabel](videodriverkit/iouservideochannellabel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/setpreferredchannelsforstereo)*