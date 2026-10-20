# SetCurrentSelectedValues

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the current control value.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t SetCurrentSelectedValues(const IOUserVideoSelectorValue *in_values, size_t in_num_values);
```

#### Discussion

Changing the control value will send a notification to the host to update the object state if successful. The object’s work queue synchronizes access to the value.

## Parameters

- `in_values`: Pointer to an array of IOUserVideoSelectorValues
- `in_num_values`: Number of IOUserVideoSelectorValues in in_values

## See Also

### Accessing the value
- [GetCurrentSelectedValues](./getcurrentselectedvalues.md)
  Gets the current selected values of the control.
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

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoselectorcontrol/setcurrentselectedvalues)*