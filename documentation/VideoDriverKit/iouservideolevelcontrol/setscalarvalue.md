# SetScalarValue

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetScalarValue(float in_scalar);
```

#### Return Value

Returns kern_return_t.

#### Discussion

Set the current scalar level value.

Changing the scalar level value will send a notification to the host to update the object state if successful. Setting the value will be synchronized using the work queue created by the object.

## See Also

- [SetDecibelValue](iouservideolevelcontrol/setdecibelvalue.md)
- [GetScalarValue](iouservideolevelcontrol/getscalarvalue.md)
- [GetDecibelValue](iouservideolevelcontrol/getdecibelvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideolevelcontrol/setscalarvalue)*