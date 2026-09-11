# SetScalarValue

**Framework**: VideoDriverKit  
**Kind**: method

Sets the current scalar level value.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t SetScalarValue(float in_scalar);
```

#### Discussion

Changing the scalar level value will send a notification to the host to update the object state if successful. The object’s work queue synchronizes access to the value.

## See Also

- [SetDecibelValue](iouservideolevelcontrol/setdecibelvalue.md)
  Sets the current decibel level value.
- [GetScalarValue](iouservideolevelcontrol/getscalarvalue.md)
  Gets the scalar level value for the control.
- [GetDecibelValue](iouservideolevelcontrol/getdecibelvalue.md)
  Gets the decibel level value for the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideolevelcontrol/setscalarvalue)*