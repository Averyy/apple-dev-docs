# HandleChangeSelectedValues

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t HandleChangeSelectedValues(const IOUserVideoSelectorValue *in_control_values, size_t in_num_values);
```

#### Return Value

Returns kIOReturnSuccess on sucess. Upon sucess the control’s value should be updated.

#### Discussion

Virtual method will be called when the controls selected values will be changed.

Default implementation will call SetCurrentSelectedValues() and return kIOReturnSuccess. Subclass and override this method to handle changes to this control and return kIOReturnSucess upon success.

## Parameters

- `in_control_values`: Pointer to an array of IOUserVideoSelectorValues attempting to be set on the control.
- `in_num_values`: The number of IOUserVideoSelectorValues in in_control_values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoselectorcontrol/handlechangeselectedvalues)*