# GetCurrentSelectedValues

**Framework**: VideoDriverKit  
**Kind**: method

Gets the current selected values of the control.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
size_t GetCurrentSelectedValues(IOUserVideoSelectorValue *out_values, size_t in_num_values);
```

#### Return Value

Size_t indicating the number of values returning in out_values

#### Discussion

The object’s work queue synchronizes access to the value.

## Parameters

- `out_values`: Pointer to an array of IOUserVideoSelectorValues that will be updated with the currently selected control values
- `in_num_values`: The number of IOUserVideoSelectorValues in the out_values array

## See Also

- [SetCurrentSelectedValues](iouservideoselectorcontrol/setcurrentselectedvalues.md)
  Sets the current control value.
- [IOUserVideoSelectorValue](iouservideoselectorvalue.md)
  Selector value for controls.
- [GetControlValuesCount](iouservideoselectorcontrol/getcontrolvaluescount.md)
  Gets the number of available selector control values.
- [AddControlValueDescriptions](iouservideoselectorcontrol/addcontrolvaluedescriptions.md)
  Adds control value descriptions to the selector control.
- [RemoveControlValueDescriptions](iouservideoselectorcontrol/removecontrolvaluedescriptions.md)
  Removes selector control values from the selector control.
- [GetControlValueDescriptions](iouservideoselectorcontrol/getcontrolvaluedescriptions.md)
  Gets the selector values for the control.
- [IOUserVideoSelectorValueDescription](iouservideoselectorvaluedescription.md)
  A selector control’s value and name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoselectorcontrol/getcurrentselectedvalues)*