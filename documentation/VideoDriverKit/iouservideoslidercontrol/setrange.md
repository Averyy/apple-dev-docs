# SetRange

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetRange(IOUserVideoSliderRange in_range);
```

#### Return Value

Returns kern_return_t.

#### Discussion

Set the current range of the slider control.

Changing the range will send a notification to the host to update the object state if successful. Setting the value will be synchronized using the work queue created by the object.

## Parameters

- `in_range`: IOUserVideoSliderRange slider control range

## See Also

- [SetControlValue](iouservideoslidercontrol/setcontrolvalue.md)
- [GetControlValue](iouservideoslidercontrol/getcontrolvalue.md)
- [GetRange](iouservideoslidercontrol/getrange.md)
- [IOUserVideoSliderRange](iouservideosliderrange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoslidercontrol/setrange)*