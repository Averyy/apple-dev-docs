# SetInputSafetyOffset

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetInputSafetyOffset(uint32_t in_safety_offset);
```

#### Return Value

Returns kern_return_t

#### Discussion

Specify the input safety offset of the device.

A uint32_t whose value indicates the number for frames behind the current hardware position that is safe to do IO.

## Parameters

- `in_safety_offset`: uint32_t input safety offset value.

## See Also

- [GetInputSafetyOffset](iouservideodevice/getinputsafetyoffset.md)
- [SetOutputSafetyOffset](iouservideodevice/setoutputsafetyoffset.md)
- [GetOutputSafetyOffset](iouservideodevice/getoutputsafetyoffset.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/setinputsafetyoffset)*