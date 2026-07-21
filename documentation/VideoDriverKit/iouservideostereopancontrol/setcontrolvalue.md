# SetControlValue

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetControlValue(float in_control_value);
```

#### Return Value

Returns kern_return_t.

#### Discussion

Set the current control value.

Changing the control value will send a notification to the host to update the object state if successful. Setting the value will be synchronized using the work queue created by the object.

## Parameters

- `in_control_value`: Float stereo pan value.

## See Also

- [GetControlValue](iouservideostereopancontrol/getcontrolvalue.md)
- [SetPanningChannels](iouservideostereopancontrol/setpanningchannels.md)
- [GetPanningChannels](iouservideostereopancontrol/getpanningchannels.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostereopancontrol/setcontrolvalue)*