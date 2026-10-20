# GetControlValuesCount

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the number of available selector control values.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
size_t GetControlValuesCount();
```

#### Discussion

The object’s work queue synchronizes access to the selector control value count.

## See Also

### Accessing the value
- [SetCurrentSelectedValues](./setcurrentselectedvalues.md)
  Sets the current control value.
- [GetCurrentSelectedValues](./getcurrentselectedvalues.md)
  Gets the current selected values of the control.
- [IOUserVideoSelectorValue](../iouservideoselectorvalue.md)
  Selector value for controls.
- [AddControlValueDescriptions](./addcontrolvaluedescriptions.md)
  Adds control value descriptions to the selector control.
- [RemoveControlValueDescriptions](./removecontrolvaluedescriptions.md)
  Removes selector control values from the selector control.
- [GetControlValueDescriptions](./getcontrolvaluedescriptions.md)
  Gets the selector values for the control.
- [IOUserVideoSelectorValueDescription](../iouservideoselectorvaluedescription.md)
  A selector control’s value and name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoselectorcontrol/getcontrolvaluescount)*