# HandleChangeControlValue

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t HandleChangeControlValue(bool in_control_value);
```

#### Return Value

Returns kIOReturnSuccess on sucess. Upon sucess the control’s value should be updated.

#### Discussion

Virtual method will be called when the controls value will be changed.

Default implementation will call SetControlValue() and return kIOReturnSuccess. Subclass and override this method to handle changes to this control value and return kIOReturnSucess upon success.

## Parameters

- `in_control_value`: The bool value attempting to be set on the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodirectioncontrol/handlechangecontrolvalue)*