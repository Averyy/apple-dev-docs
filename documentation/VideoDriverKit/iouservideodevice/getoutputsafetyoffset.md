# GetOutputSafetyOffset

**Framework**: VideoDriverKit  
**Kind**: method

Gets the output safety offset of the device.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
uint32_t GetOutputSafetyOffset();
```

#### Return Value

The output safety offset.

#### Discussion

A uint32_t whose value indicates the number of frames ahead of the current hardware position that is safe to do IO.

## See Also

- [SetInputSafetyOffset](iouservideodevice/setinputsafetyoffset.md)
  Specifies the input safety offset of the device.
- [GetInputSafetyOffset](iouservideodevice/getinputsafetyoffset.md)
  Gets the input safety offset of the device.
- [SetOutputSafetyOffset](iouservideodevice/setoutputsafetyoffset.md)
  Specifies the output safety offset of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/getoutputsafetyoffset)*