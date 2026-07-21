# AddControlValueDescriptions

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t AddControlValueDescriptions(const IOUserVideoSelectorValueDescription *in_value_descriptions, size_t in_num_value_descriptions);
```

#### Return Value

Returns kIOReturnSuccess if selector control value descriptions were successfully added.

#### Discussion

Add control value descriptions to the selector control.

## Parameters

- `in_value_descriptions`: Pointer to an array of IOUserVideoSelectorValueDescriptions.
- `in_num_value_descriptions`: Size_t of number of items in the in_value_descriptions parameter.

## See Also

- [SetCurrentSelectedValues](iouservideoselectorcontrol/setcurrentselectedvalues.md)
- [GetCurrentSelectedValues](iouservideoselectorcontrol/getcurrentselectedvalues.md)
- [IOUserVideoSelectorValue](iouservideoselectorvalue.md)
- [GetControlValuesCount](iouservideoselectorcontrol/getcontrolvaluescount.md)
- [RemoveControlValueDescriptions](iouservideoselectorcontrol/removecontrolvaluedescriptions.md)
- [GetControlValueDescriptions](iouservideoselectorcontrol/getcontrolvaluedescriptions.md)
- [IOUserVideoSelectorValueDescription](iouservideoselectorvaluedescription.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoselectorcontrol/addcontrolvaluedescriptions)*