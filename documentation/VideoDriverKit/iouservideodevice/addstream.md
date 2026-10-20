# AddStream

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Adds an video stream to the device.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t AddStream(IOUserVideoStream *in_stream);
```

#### Return Value

`kIOReturnSuccess` if stream was successfully added.

#### Discussion

The stream’s reference count will be incremented if it was successfully added.

## Parameters

- `in_stream`: IOUserVideoStream to add to the device.

## See Also

### Working with video streams
- [RemoveStream](./removestream.md)
  Removes a video stream from the device.
- [IOUserVideoStream](../iouservideostream.md)
  A video stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/addstream)*