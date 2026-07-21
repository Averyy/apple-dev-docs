# GetInputSafetyOffset

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
uint32_t GetInputSafetyOffset();
```

#### Return Value

Returns uint32_t input safety offset.

#### Discussion

Get the input safety offset of the device.

A uint32_t whose value indicates the number for frames behind the current hardware position that is safe to do IO.

## See Also

- [SetInputSafetyOffset](iouservideodevice/setinputsafetyoffset.md)
- [SetOutputSafetyOffset](iouservideodevice/setoutputsafetyoffset.md)
- [GetOutputSafetyOffset](iouservideodevice/getoutputsafetyoffset.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/getinputsafetyoffset)*