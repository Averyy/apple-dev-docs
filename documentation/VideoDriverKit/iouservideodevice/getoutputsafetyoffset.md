# GetOutputSafetyOffset

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
uint32_t GetOutputSafetyOffset();
```

#### Return Value

Returns uint32_t output safety offset.

#### Discussion

Get the output safety offset of the device.

A uint32_t whose value indicates the number for frames ahead the current hardware position that is safe to do IO.

## See Also

- [SetInputSafetyOffset](iouservideodevice/setinputsafetyoffset.md)
- [GetInputSafetyOffset](iouservideodevice/getinputsafetyoffset.md)
- [SetOutputSafetyOffset](iouservideodevice/setoutputsafetyoffset.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/getoutputsafetyoffset)*