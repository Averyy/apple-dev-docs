# GetPanningChannels

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
void GetPanningChannels(IOUserVideoObjectPropertyElement *out_left_channel, IOUserVideoObjectPropertyElement *out_right_channel);
```

#### Discussion

Get the current stereo panning channels.

Getting the value will be synchronized using the work queue created by the object.

## Parameters

- `out_left_channel`: IOUserVideoObjectPropertyElement for the left channel
- `out_right_channel`: IOUserVideoObjectPropertyElement for the right channel

## See Also

- [SetControlValue](iouservideostereopancontrol/setcontrolvalue.md)
- [GetControlValue](iouservideostereopancontrol/getcontrolvalue.md)
- [SetPanningChannels](iouservideostereopancontrol/setpanningchannels.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostereopancontrol/getpanningchannels)*