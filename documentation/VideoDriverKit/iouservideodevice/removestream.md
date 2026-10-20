# RemoveStream

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Removes a video stream from the device.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t RemoveStream(IOUserVideoStream *in_stream);
```

#### Return Value

`kIOReturnSuccess` if stream was successfully removed.

#### Discussion

The stream’s reference count will be decremented if it was successfully removed.

## Parameters

- `in_stream`: IOUserVideoStream to remove from the device.

## See Also

### Working with video streams
- [AddStream](./addstream.md)
  Adds an video stream to the device.
- [IOUserVideoStream](../iouservideostream.md)
  A video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/removestream)*