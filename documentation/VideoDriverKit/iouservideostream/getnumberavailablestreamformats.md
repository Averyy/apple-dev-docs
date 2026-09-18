# GetNumberAvailableStreamFormats

**Framework**: VideoDriverKit  
**Kind**: method

Gets the number of available description for the stream.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
size_t GetNumberAvailableStreamFormats();
```

#### Discussion

The object’s work queue synchronizes access to the value.

## See Also

- [SetCurrentStreamFormat](iouservideostream/setcurrentstreamformat.md)
  Sets the current stream format.
- [GetCurrentStreamFormat](iouservideostream/getcurrentstreamformat.md)
  Gets the current basic description of the stream.
- [SetAvailableStreamFormats](iouservideostream/setavailablestreamformats.md)
  Sets the available descriptions for the stream.
- [GetAvailableStreamFormats](iouservideostream/getavailablestreamformats.md)
  Gets the available basic descriptions for the stream.
- [IOUserVideoStreamBasicDescription](videodriverkit/iouservideostreambasicdescription.md)
  A structure that encapsulates all the information for describing the basic format properties of a stream of audio data.
- [GetStreamDirection](iouservideostream/getstreamdirection.md)
  Gets the direction of the stream.
- [IOUserVideoStreamDirection](videodriverkit/iouservideostreamdirection.md)
  The direction of a video stream.
- [SetStreamIsActive](iouservideostream/setstreamisactive.md)
  Sets whether that the stream is active and doing IO.
- [GetStreamIsActive](iouservideostream/getstreamisactive.md)
  Gets the stream activity state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getnumberavailablestreamformats)*