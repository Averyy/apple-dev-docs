# SetControlValue

**Framework**: VideoDriverKit  
**Kind**: method

Sets the current control value.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetControlValue(float in_control_value);
```

#### Discussion

Changing the control value will send a notification to the host to update the object state if successful. The object’s work queue synchronizes access to the value.

## Parameters

- `in_control_value`: Float stereo pan value.

## See Also

- [GetControlValue](iouservideostereopancontrol/getcontrolvalue.md)
  Gets the current value of the control.
- [SetPanningChannels](iouservideostereopancontrol/setpanningchannels.md)
  Sets the current stereo panning channels.
- [GetPanningChannels](iouservideostereopancontrol/getpanningchannels.md)
  Gets the current stereo panning channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostereopancontrol/setcontrolvalue)*