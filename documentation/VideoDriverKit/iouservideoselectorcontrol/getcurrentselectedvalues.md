# GetCurrentSelectedValues

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the current selected values of the control.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
size_t GetCurrentSelectedValues(IOUserVideoSelectorValue *out_values, size_t in_num_values);
```

## Return Value

Size_t indicating the number of values returning in out_values

## Discussion

The object’s work queue synchronizes access to the value.

## Parameters

- `out_values`: Pointer to an array of IOUserVideoSelectorValues that will be updated with the currently selected control values
- `in_num_values`: The number of IOUserVideoSelectorValues in the out_values array

## See Also

### Accessing the value
- [SetCurrentSelectedValues](./setcurrentselectedvalues.md)
  Sets the current control value.
- [IOUserVideoSelectorValue](../iouservideoselectorvalue.md)
  Selector value for controls.
- [GetControlValuesCount](./getcontrolvaluescount.md)
  Gets the number of available selector control values.
- [AddControlValueDescriptions](./addcontrolvaluedescriptions.md)
  Adds control value descriptions to the selector control.
- [RemoveControlValueDescriptions](./removecontrolvaluedescriptions.md)
  Removes selector control values from the selector control.
- [GetControlValueDescriptions](./getcontrolvaluedescriptions.md)
  Gets the selector values for the control.
- [IOUserVideoSelectorValueDescription](../iouservideoselectorvaluedescription.md)
  A selector control’s value and name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoselectorcontrol/getcurrentselectedvalues)*