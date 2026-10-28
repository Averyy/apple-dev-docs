# GetControlValue

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the current value of the control.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
uint32_t GetControlValue();
```

## Discussion

The object’s work queue synchronizes access to the value.

## See Also

### Accessing the value
- [SetControlValue](./setcontrolvalue.md)
  Sets the current control value.
- [SetRange](./setrange.md)
  Sets the current range of the slider control.
- [GetRange](./getrange.md)
  Gets the current range of the slider control.
- [IOUserVideoSliderRange](../iouservideosliderrange.md)
  The minimum and maximum range for the slider value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoslidercontrol/getcontrolvalue)*