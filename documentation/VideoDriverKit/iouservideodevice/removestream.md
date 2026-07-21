# RemoveStream

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t RemoveStream(IOUserVideoStream *in_stream);
```

#### Return Value

Returns kIOReturnSuccess if stream was successfully removed.

#### Discussion

Remove a IOUserVideoStream from the device.

The stream’s reference count will be decremented if it was successfully removed.

## Parameters

- `in_stream`: IOUserVideoStream to remove from the device.

## See Also

- [AddStream](iouservideodevice/addstream.md)
- [IOUserVideoStream](iouservideostream.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/removestream)*