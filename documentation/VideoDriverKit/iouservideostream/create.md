# Create

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Static Method

**Availability**:
- DriverKit 27.0+

## Declaration

```c
static OSSharedPtr<IOUserVideoStream> Create(IOUserVideoDriver *in_driver, OSString *in_stream_uid, IOUserVideoStreamDirection in_direction, OSArray *in_video_buffers);
```

## See Also

### Creating a video stream
- [init](./init.md)
  Initializes an video stream.
- [IOUserVideoDriver](../iouservideodriver.md)
  A video driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/create)*