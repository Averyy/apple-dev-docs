# AddStream

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t AddStream(IOUserVideoStream *in_stream);
```

#### Return Value

Returns kIOReturnSuccess if stream was successfully added.

#### Discussion

Add a IOUserVideoStream to the device.

The stream’s reference count will be incremented if it was successfully added.

## Parameters

- `in_stream`: IOUserVideoStream to add to the device.

## See Also

- [RemoveStream](iouservideodevice/removestream.md)
- [IOUserVideoStream](iouservideostream.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/addstream)*