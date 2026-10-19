# HandleChangeControlValue

**Framework**: VideoDriverKit  
**Kind**: method

The system calls this virtual method when the control’s value changes.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
virtual kern_return_t HandleChangeControlValue(float in_control_value);
```

#### Return Value

`kIOReturnSuccess` on success. Upon success, the control’s value should be updated.

#### Discussion

The default implementation calls SetControlValue() and returns `kIOReturnSuccess`. Subclass and override this method to handle changes to this control value and return `kIOReturnSuccess` upon success.

## Parameters

- `in_control_value`: The float value to set on the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostereopancontrol/handlechangecontrolvalue)*