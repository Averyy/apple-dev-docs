# HandleChangeSelectedValues

**Framework**: VideoDriverKit  
**Kind**: method

The system calls this virtual method when the control’s selected values change.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
virtual kern_return_t HandleChangeSelectedValues(const IOUserVideoSelectorValue *in_control_values, size_t in_num_values);
```

#### Return Value

`kIOReturnSuccess` on success. Upon success, the control’s value should be updated.

#### Discussion

The default implementation calls SetCurrentSelectedValues() and returns `kIOReturnSuccess`. Subclass and override this method to handle changes to this control and return `kIOReturnSuccess` upon success.

## Parameters

- `in_control_values`: Pointer to an array of IOUserVideoSelectorValues to set on the control.
- `in_num_values`: The number of IOUserVideoSelectorValues in in_control_values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoselectorcontrol/handlechangeselectedvalues)*