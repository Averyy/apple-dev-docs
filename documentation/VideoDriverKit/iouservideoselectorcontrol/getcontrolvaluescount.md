# GetControlValuesCount

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
size_t GetControlValuesCount();
```

#### Return Value

Returns size_t.

#### Discussion

Get the number of available selector control values.

Getting the selector control value count will be synchronized using the work queue created by the object.

## See Also

- [SetCurrentSelectedValues](iouservideoselectorcontrol/setcurrentselectedvalues.md)
- [GetCurrentSelectedValues](iouservideoselectorcontrol/getcurrentselectedvalues.md)
- [IOUserVideoSelectorValue](iouservideoselectorvalue.md)
- [AddControlValueDescriptions](iouservideoselectorcontrol/addcontrolvaluedescriptions.md)
- [RemoveControlValueDescriptions](iouservideoselectorcontrol/removecontrolvaluedescriptions.md)
- [GetControlValueDescriptions](iouservideoselectorcontrol/getcontrolvaluedescriptions.md)
- [IOUserVideoSelectorValueDescription](iouservideoselectorvaluedescription.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoselectorcontrol/getcontrolvaluescount)*