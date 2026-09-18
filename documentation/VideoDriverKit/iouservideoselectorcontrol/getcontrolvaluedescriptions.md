# GetControlValueDescriptions

**Framework**: VideoDriverKit  
**Kind**: method

Gets the selector values for the control.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
size_t GetControlValueDescriptions(IOUserVideoSelectorValueDescription *out_control_value_descriptions, size_t in_num_value_descriptions);
```

#### Return Value

Size_t of number of values written to out_control_values.

#### Discussion

The object’s work queue synchronizes access to the selector control value description.

## Parameters

- `out_control_value_descriptions`: Pointer to an array of IOUserVideoSelectorValueDescriptions
- `in_num_value_descriptions`: Size_t for the number of values to store into out_control_values.

## See Also

- [SetCurrentSelectedValues](iouservideoselectorcontrol/setcurrentselectedvalues.md)
  Sets the current control value.
- [GetCurrentSelectedValues](iouservideoselectorcontrol/getcurrentselectedvalues.md)
  Gets the current selected values of the control.
- [IOUserVideoSelectorValue](iouservideoselectorvalue.md)
  Selector value for controls.
- [GetControlValuesCount](iouservideoselectorcontrol/getcontrolvaluescount.md)
  Gets the number of available selector control values.
- [AddControlValueDescriptions](iouservideoselectorcontrol/addcontrolvaluedescriptions.md)
  Adds control value descriptions to the selector control.
- [RemoveControlValueDescriptions](iouservideoselectorcontrol/removecontrolvaluedescriptions.md)
  Removes selector control values from the selector control.
- [IOUserVideoSelectorValueDescription](iouservideoselectorvaluedescription.md)
  A selector control’s value and name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoselectorcontrol/getcontrolvaluedescriptions)*