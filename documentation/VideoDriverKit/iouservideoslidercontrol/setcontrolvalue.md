# SetControlValue

**Framework**: VideoDriverKit  
**Kind**: method

Sets the current control value.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t SetControlValue(uint32_t in_control_value);
```

#### Discussion

Changing the control value will send a notification to the host to update the object state if successful. The object’s work queue synchronizes access to the value.

## Parameters

- `in_control_value`: uint32_t slider control value

## See Also

- [GetControlValue](iouservideoslidercontrol/getcontrolvalue.md)
  Gets the current value of the control.
- [SetRange](iouservideoslidercontrol/setrange.md)
  Sets the current range of the slider control.
- [GetRange](iouservideoslidercontrol/getrange.md)
  Gets the current range of the slider control.
- [IOUserVideoSliderRange](iouservideosliderrange.md)
  The minimum and maximum range for the slider value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoslidercontrol/setcontrolvalue)*