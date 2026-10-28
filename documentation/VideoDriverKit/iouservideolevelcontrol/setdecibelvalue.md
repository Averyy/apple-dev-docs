# SetDecibelValue

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the current decibel level value.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t SetDecibelValue(float in_decibel_value);
```

## Discussion

Changing the decibel level value will send a notification to the host to update the object state if successful. The object’s work queue synchronizes access to the value.

## Parameters

- `in_decibel_value`: Float decibel level value

## See Also

### Accessing the value
- [SetScalarValue](./setscalarvalue.md)
  Sets the current scalar level value.
- [GetScalarValue](./getscalarvalue.md)
  Gets the scalar level value for the control.
- [GetDecibelValue](./getdecibelvalue.md)
  Gets the decibel level value for the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideolevelcontrol/setdecibelvalue)*