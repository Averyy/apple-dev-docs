# GetAvailableStreamFormats

**Framework**: VideoDriverKit  
**Kind**: method

Gets the available basic descriptions for the stream.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
size_t GetAvailableStreamFormats(IOUserVideoStreamBasicDescription *out_formats, size_t in_num_formats);
```

#### Return Value

The number of formats were set in the `out_formats` buffer.

#### Discussion

The object’s work queue synchronizes access to the value.

## Parameters

- `out_formats`: Pointer to a buffer of `IOUserVideoStreamBasicDescription` objects with size corresponding to `in_num_formats`.
- `in_num_formats`: The number of formats in `out_formats `buffer.

## See Also

- [SetCurrentStreamFormat](iouservideostream/setcurrentstreamformat.md)
  Sets the current stream format.
- [GetCurrentStreamFormat](iouservideostream/getcurrentstreamformat.md)
  Gets the current basic description of the stream.
- [SetAvailableStreamFormats](iouservideostream/setavailablestreamformats.md)
  Sets the available descriptions for the stream.
- [GetNumberAvailableStreamFormats](iouservideostream/getnumberavailablestreamformats.md)
  Gets the number of available description for the stream.
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

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getavailablestreamformats)*