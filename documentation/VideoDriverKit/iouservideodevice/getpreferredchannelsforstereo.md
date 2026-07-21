# GetPreferredChannelsForStereo

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
void GetPreferredChannelsForStereo(uint32_t *out_left_channel, uint32_t *out_right_channel);
```

#### Discussion

Get the channel indices for the prefered stereo pair

## Parameters

- `out_left_channel`: Pointer to a uint32_t channel index for the preferred stereo left channel.
- `out_right_channel`: Pointer to a uint32_t channel index for the preferred stereo right channel.

## See Also

- [SetPreferredChannelsForStereo](iouservideodevice/setpreferredchannelsforstereo.md)
- [SetPreferredInputChannelLayout](iouservideodevice/setpreferredinputchannellayout.md)
- [SetPreferredOutputChannelLayout](iouservideodevice/setpreferredoutputchannellayout.md)
- [IOUserVideoChannelLabel](videodriverkit/iouservideochannellabel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/getpreferredchannelsforstereo)*