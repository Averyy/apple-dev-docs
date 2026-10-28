# GetInputSafetyOffset

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the input safety offset of the device.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
uint32_t GetInputSafetyOffset();
```

## Return Value

The input safety offset.

## Discussion

A uint32_t whose value indicates the number for frames behind the current hardware position that is safe to do IO.

## See Also

### Working with safety offset behavior
- [SetInputSafetyOffset](./setinputsafetyoffset.md)
  Specifies the input safety offset of the device.
- [SetOutputSafetyOffset](./setoutputsafetyoffset.md)
  Specifies the output safety offset of the device.
- [GetOutputSafetyOffset](./getoutputsafetyoffset.md)
  Gets the output safety offset of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/getinputsafetyoffset)*