# SetStreamIsActive

**Framework**: VideoDriverKit  
**Kind**: method

Sets whether that the stream is active and doing IO.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t SetStreamIsActive(bool in_is_active);
```

#### Discussion

Changing the stream active state will send a notification to the host to update the object state if successful. The object’s work queue synchronizes access to the stream active state.

## Parameters

- `in_is_active`: True if the stream is enabled and doing IO; otherwise, false.

## See Also

- [SetCurrentStreamFormat](iouservideostream/setcurrentstreamformat.md)
  Sets the current stream format.
- [GetCurrentStreamFormat](iouservideostream/getcurrentstreamformat.md)
  Gets the current basic description of the stream.
- [SetAvailableStreamFormats](iouservideostream/setavailablestreamformats.md)
  Sets the available descriptions for the stream.
- [GetAvailableStreamFormats](iouservideostream/getavailablestreamformats.md)
  Gets the available basic descriptions for the stream.
- [GetNumberAvailableStreamFormats](iouservideostream/getnumberavailablestreamformats.md)
  Gets the number of available description for the stream.
- [IOUserVideoStreamBasicDescription](videodriverkit/iouservideostreambasicdescription.md)
  A structure that encapsulates all the information for describing the basic format properties of a stream of audio data.
- [GetStreamDirection](iouservideostream/getstreamdirection.md)
  Gets the direction of the stream.
- [IOUserVideoStreamDirection](videodriverkit/iouservideostreamdirection.md)
  The direction of a video stream.
- [GetStreamIsActive](iouservideostream/getstreamisactive.md)
  Gets the stream activity state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/setstreamisactive)*