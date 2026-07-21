# SetDecibelValue

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetDecibelValue(float in_decibel_value);
```

#### Return Value

Returns kern_return_t.

#### Discussion

Set the current decibel level value.

Changing the decibel level value will send a notification to the host to update the object state if successful. Setting the value will be synchronized using the work queue created by the object.

## Parameters

- `in_decibel_value`: Float decibel level value

## See Also

- [SetScalarValue](iouservideolevelcontrol/setscalarvalue.md)
- [GetScalarValue](iouservideolevelcontrol/getscalarvalue.md)
- [GetDecibelValue](iouservideolevelcontrol/getdecibelvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideolevelcontrol/setdecibelvalue)*