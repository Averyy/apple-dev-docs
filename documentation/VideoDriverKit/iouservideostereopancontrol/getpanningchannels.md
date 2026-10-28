# GetPanningChannels

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the current stereo panning channels.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
void GetPanningChannels(IOUserVideoObjectPropertyElement *out_left_channel, IOUserVideoObjectPropertyElement *out_right_channel);
```

## Discussion

The object’s work queue synchronizes access to this value.

## Parameters

- `out_left_channel`: IOUserVideoObjectPropertyElement for the left channel.
- `out_right_channel`: IOUserVideoObjectPropertyElement for the right channel.

## See Also

### Accessing the value
- [SetControlValue](./setcontrolvalue.md)
  Sets the current control value.
- [GetControlValue](./getcontrolvalue.md)
  Gets the current value of the control.
- [SetPanningChannels](./setpanningchannels.md)
  Sets the current stereo panning channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostereopancontrol/getpanningchannels)*