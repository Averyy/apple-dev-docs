# GetControlValue

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
uint32_t GetControlValue();
```

#### Return Value

Returns uint32_t

#### Discussion

Get the current value of the control.

Getting the value will be synchronized using the work queue created by the object.

## See Also

- [SetControlValue](iouservideoslidercontrol/setcontrolvalue.md)
- [SetRange](iouservideoslidercontrol/setrange.md)
- [GetRange](iouservideoslidercontrol/getrange.md)
- [IOUserVideoSliderRange](iouservideosliderrange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoslidercontrol/getcontrolvalue)*