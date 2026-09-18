# SetPanningChannels

**Framework**: VideoDriverKit  
**Kind**: method

Sets the current stereo panning channels.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetPanningChannels(IOUserVideoObjectPropertyElement in_left_channel, IOUserVideoObjectPropertyElement in_right_channel);
```

#### Discussion

Changing the panning channels will send a notification to the host to update the object state if successful. The object’s work queue synchronizes access to the value.

## Parameters

- `in_left_channel`: IOUserVideoObjectPropertyElement for the left channel
- `in_right_channel`: IOUserVideoObjectPropertyElement for the right channel

## See Also

- [SetControlValue](iouservideostereopancontrol/setcontrolvalue.md)
  Sets the current control value.
- [GetControlValue](iouservideostereopancontrol/getcontrolvalue.md)
  Gets the current value of the control.
- [GetPanningChannels](iouservideostereopancontrol/getpanningchannels.md)
  Gets the current stereo panning channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostereopancontrol/setpanningchannels)*