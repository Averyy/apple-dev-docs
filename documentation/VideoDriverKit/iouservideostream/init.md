# init

**Framework**: VideoDriverKit  
**Kind**: method

Initializes an video stream.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual bool init(IOUserVideoDriver *in_driver, OSString *in_stream_uid, IOUserVideoStreamDirection in_direction, OSArray *in_video_buffers);
```

#### Return Value

True on success.

## Parameters

- `in_driver`: The video driver that owns this object.
- `in_stream_uid`: The identifier for the stream. Create a new UUID for each video stream you initialize — for example, using the `genuuid` command in Terminal. Don’t initialize another instance with the same UUID unless you ensure the previous instance has been deallocated.
- `in_direction`: The stream’s direction.
- `in_video_buffers`: An array of video buffers.

## See Also

- [Create](iouservideostream/create.md)
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/init)*