# HandleChangeScalarValue

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t HandleChangeScalarValue(float in_scalar_value);
```

#### Return Value

Returns kIOReturnSuccess on sucess. Upon sucess the control’s value should be updated.

#### Discussion

Virtual method will be called when the controls value will be changed.

Default implementation will call SetScalarValue() and return kIOReturnSuccess. Subclass and override this method to handle changes to this control value and return kIOReturnSucess upon success.

## Parameters

- `in_scalar_value`: The float scalar level value attempting to be set on the control.

## See Also

- [HandleChangeDecibelValue](iouservideolevelcontrol/handlechangedecibelvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideolevelcontrol/handlechangescalarvalue)*