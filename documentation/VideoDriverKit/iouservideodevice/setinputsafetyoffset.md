# SetInputSafetyOffset

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Specifies the input safety offset of the device.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t SetInputSafetyOffset(uint32_t in_safety_offset);
```

#### Discussion

A uint32_t whose value indicates the number for frames behind the current hardware position that is safe to do IO.

## Parameters

- `in_safety_offset`: uint32_t input safety offset value.

## See Also

### Working with safety offset behavior
- [GetInputSafetyOffset](./getinputsafetyoffset.md)
  Gets the input safety offset of the device.
- [SetOutputSafetyOffset](./setoutputsafetyoffset.md)
  Specifies the output safety offset of the device.
- [GetOutputSafetyOffset](./getoutputsafetyoffset.md)
  Gets the output safety offset of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/setinputsafetyoffset)*