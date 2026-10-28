# SetPanningChannels

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the current stereo panning channels.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t SetPanningChannels(IOUserVideoObjectPropertyElement in_left_channel, IOUserVideoObjectPropertyElement in_right_channel);
```

## Discussion

Changing the panning channels will send a notification to the host to update the object state if successful. The object’s work queue synchronizes access to the value.

## Parameters

- `in_left_channel`: IOUserVideoObjectPropertyElement for the left channel
- `in_right_channel`: IOUserVideoObjectPropertyElement for the right channel

## See Also

### Accessing the value
- [SetControlValue](./setcontrolvalue.md)
  Sets the current control value.
- [GetControlValue](./getcontrolvalue.md)
  Gets the current value of the control.
- [GetPanningChannels](./getpanningchannels.md)
  Gets the current stereo panning channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostereopancontrol/setpanningchannels)*