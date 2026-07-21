# HandleChangeDecibelValue

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t HandleChangeDecibelValue(float in_decibel_value);
```

#### Return Value

Returns kIOReturnSuccess on sucess. Upon sucess the control’s value should be updated.

#### Discussion

Virtual method will be called when the controls value will be changed.

Default implementation will call SetDecibelValue() and return kIOReturnSuccess Subclass and override this method to handle changes to this control value and return kIOReturnSucess upon success.

## Parameters

- `in_decibel_value`: The float decibel level value attempting to be set on the control.

## See Also

- [HandleChangeScalarValue](iouservideolevelcontrol/handlechangescalarvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideolevelcontrol/handlechangedecibelvalue)*