# GetCurrentSelectedValues

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
size_t GetCurrentSelectedValues(IOUserVideoSelectorValue *out_values, size_t in_num_values);
```

#### Return Value

Returns size_t indicating the number of values returning in out_values

#### Discussion

Get the current selected values of the control.

Getting the value will be synchronized using the work queue created by the object.

## Parameters

- `out_values`: Pointer to an array of IOUserVideoSelectorValues that will be updated with the currently selected control values
- `in_num_values`: The number of IOUserVideoSelectorValues in the out_values array

## See Also

- [SetCurrentSelectedValues](iouservideoselectorcontrol/setcurrentselectedvalues.md)
- [IOUserVideoSelectorValue](iouservideoselectorvalue.md)
- [GetControlValuesCount](iouservideoselectorcontrol/getcontrolvaluescount.md)
- [AddControlValueDescriptions](iouservideoselectorcontrol/addcontrolvaluedescriptions.md)
- [RemoveControlValueDescriptions](iouservideoselectorcontrol/removecontrolvaluedescriptions.md)
- [GetControlValueDescriptions](iouservideoselectorcontrol/getcontrolvaluedescriptions.md)
- [IOUserVideoSelectorValueDescription](iouservideoselectorvaluedescription.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoselectorcontrol/getcurrentselectedvalues)*