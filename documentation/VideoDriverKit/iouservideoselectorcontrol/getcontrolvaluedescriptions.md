# GetControlValueDescriptions

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
size_t GetControlValueDescriptions(IOUserVideoSelectorValueDescription *out_control_value_descriptions, size_t in_num_value_descriptions);
```

#### Return Value

Returns size_t of number of values written to out_control_values.

#### Discussion

Get the selector values for the control

Getting the selector control value description will be synchronized using the work queue created by the object.

## Parameters

- `out_control_value_descriptions`: Pointer to an array of IOUserVideoSelectorValueDescriptions
- `in_num_value_descriptions`: Size_t for the number of values to store into out_control_values.

## See Also

- [SetCurrentSelectedValues](iouservideoselectorcontrol/setcurrentselectedvalues.md)
- [GetCurrentSelectedValues](iouservideoselectorcontrol/getcurrentselectedvalues.md)
- [IOUserVideoSelectorValue](iouservideoselectorvalue.md)
- [GetControlValuesCount](iouservideoselectorcontrol/getcontrolvaluescount.md)
- [AddControlValueDescriptions](iouservideoselectorcontrol/addcontrolvaluedescriptions.md)
- [RemoveControlValueDescriptions](iouservideoselectorcontrol/removecontrolvaluedescriptions.md)
- [IOUserVideoSelectorValueDescription](iouservideoselectorvaluedescription.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoselectorcontrol/getcontrolvaluedescriptions)*