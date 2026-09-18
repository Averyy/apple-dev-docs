# HandleChangeDecibelValue

**Framework**: VideoDriverKit  
**Kind**: method

The system calls this virtual method when the control’s value changes.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t HandleChangeDecibelValue(float in_decibel_value);
```

#### Return Value

`kIOReturnSuccess` on success. Upon success the control’s value should be updated.

#### Discussion

The default implementation calls SetDecibelValue() and returns `kIOReturnSuccess`. Subclass and override this method to handle changes to this control value and return `kIOReturnSuccess` upon success.

## Parameters

- `in_decibel_value`: The float decibel level value attempting to be set on the control.

## See Also

- [HandleChangeScalarValue](iouservideolevelcontrol/handlechangescalarvalue.md)
  The system calls this virtual method when the control’s value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideolevelcontrol/handlechangedecibelvalue)*