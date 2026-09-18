# GetPanningChannels

**Framework**: VideoDriverKit  
**Kind**: method

Gets the current stereo panning channels.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
void GetPanningChannels(IOUserVideoObjectPropertyElement *out_left_channel, IOUserVideoObjectPropertyElement *out_right_channel);
```

#### Discussion

The object’s work queue synchronizes access to this value.

## Parameters

- `out_left_channel`: IOUserVideoObjectPropertyElement for the left channel.
- `out_right_channel`: IOUserVideoObjectPropertyElement for the right channel.

## See Also

- [SetControlValue](iouservideostereopancontrol/setcontrolvalue.md)
  Sets the current control value.
- [GetControlValue](iouservideostereopancontrol/getcontrolvalue.md)
  Gets the current value of the control.
- [SetPanningChannels](iouservideostereopancontrol/setpanningchannels.md)
  Sets the current stereo panning channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostereopancontrol/getpanningchannels)*