# SetRange

**Framework**: VideoDriverKit  
**Kind**: method

Sets the current range of the slider control.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetRange(IOUserVideoSliderRange in_range);
```

#### Discussion

Changing the range will send a notification to the host to update the object state if successful. The object’s work queue synchronizes access to the value.

## Parameters

- `in_range`: IOUserVideoSliderRange slider control range

## See Also

- [SetControlValue](iouservideoslidercontrol/setcontrolvalue.md)
  Sets the current control value.
- [GetControlValue](iouservideoslidercontrol/getcontrolvalue.md)
  Gets the current value of the control.
- [GetRange](iouservideoslidercontrol/getrange.md)
  Gets the current range of the slider control.
- [IOUserVideoSliderRange](iouservideosliderrange.md)
  The minimum and maximum range for the slider value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoslidercontrol/setrange)*