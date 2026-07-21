# SetPanningChannels

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetPanningChannels(IOUserVideoObjectPropertyElement in_left_channel, IOUserVideoObjectPropertyElement in_right_channel);
```

#### Return Value

Returns kern_return_t.

#### Discussion

Set the current stereo panning channels.

Changing the panning channels will send a notification to the host to update the object state if successful. Setting the value will be synchronized using the work queue created by the object.

## Parameters

- `in_left_channel`: IOUserVideoObjectPropertyElement for the left channel
- `in_right_channel`: IOUserVideoObjectPropertyElement for the right channel

## See Also

- [SetControlValue](iouservideostereopancontrol/setcontrolvalue.md)
- [GetControlValue](iouservideostereopancontrol/getcontrolvalue.md)
- [GetPanningChannels](iouservideostereopancontrol/getpanningchannels.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostereopancontrol/setpanningchannels)*