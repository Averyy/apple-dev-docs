# SetOutputSafetyOffset

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetOutputSafetyOffset(uint32_t in_safety_offset);
```

#### Return Value

Returns kern_return_t

#### Discussion

Specify the output safety offset of the device.

A uint32_t whose value indicates the number for frames ahead the current hardware position that is safe to do IO.

## Parameters

- `in_safety_offset`: uint32_t output safety offset value.

## See Also

- [SetInputSafetyOffset](iouservideodevice/setinputsafetyoffset.md)
- [GetInputSafetyOffset](iouservideodevice/getinputsafetyoffset.md)
- [GetOutputSafetyOffset](iouservideodevice/getoutputsafetyoffset.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/setoutputsafetyoffset)*