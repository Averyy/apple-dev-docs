# SetCurrentSelectedValues

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetCurrentSelectedValues(const IOUserVideoSelectorValue *in_values, size_t in_num_values);
```

#### Return Value

Returns kern_return_t.

#### Discussion

Set the current control value.

Changing the control value will send a notification to the host to update the object state if successful. Setting the value will be synchronized using the work queue created by the object.

## Parameters

- `in_values`: Pointer to an array of IOUserVideoSelectorValues
- `in_num_values`: Number of IOUserVideoSelectorValues in in_values

## See Also

- [GetCurrentSelectedValues](iouservideoselectorcontrol/getcurrentselectedvalues.md)
- [IOUserVideoSelectorValue](iouservideoselectorvalue.md)
- [GetControlValuesCount](iouservideoselectorcontrol/getcontrolvaluescount.md)
- [AddControlValueDescriptions](iouservideoselectorcontrol/addcontrolvaluedescriptions.md)
- [RemoveControlValueDescriptions](iouservideoselectorcontrol/removecontrolvaluedescriptions.md)
- [GetControlValueDescriptions](iouservideoselectorcontrol/getcontrolvaluedescriptions.md)
- [IOUserVideoSelectorValueDescription](iouservideoselectorvaluedescription.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoselectorcontrol/setcurrentselectedvalues)*