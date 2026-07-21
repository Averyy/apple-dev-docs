# init

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual bool init(IOUserVideoDriver *in_driver, OSString *in_stream_uid, IOUserVideoStreamDirection in_direction, OSArray *in_video_buffers);
```

#### Return Value

True on success.

#### Discussion

Initializes a IOUserVideoStream

## Parameters

- `in_driver`: The IOUserVideoDriver that owns this object.
- `in_direction`: A IOUserVideoStreamDirection for the stream’s direction
- `in_video_buffers`: A pointer to a an OSArray of IOUserVideoBuffers

## See Also

- [Create](iouservideostream/create.md)
- [IOUserVideoDriver](iouservideodriver.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/init)*