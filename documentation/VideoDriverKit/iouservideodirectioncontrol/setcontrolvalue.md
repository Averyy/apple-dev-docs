# SetControlValue

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the current control value.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t SetControlValue(bool in_control_value);
```

## Discussion

Changing the control value will send a notification to the host to update the object state if successful. The object’s work queue synchronizes access to the value.

## Parameters

- `in_control_value`: Bool control value.

## See Also

### Accessing the value
- [GetControlValue](./getcontrolvalue.md)
  Gets the current value of the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodirectioncontrol/setcontrolvalue)*