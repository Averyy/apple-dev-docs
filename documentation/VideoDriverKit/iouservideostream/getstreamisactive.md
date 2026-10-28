# GetStreamIsActive

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the stream activity state.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
bool GetStreamIsActive();
```

## Return Value

True if the stream is enabled and doing IO; otherwise false.

## See Also

### Working with stream formats
- [SetCurrentStreamFormat](./setcurrentstreamformat.md)
  Sets the current stream format.
- [GetCurrentStreamFormat](./getcurrentstreamformat.md)
  Gets the current basic description of the stream.
- [SetAvailableStreamFormats](./setavailablestreamformats.md)
  Sets the available descriptions for the stream.
- [GetAvailableStreamFormats](./getavailablestreamformats.md)
  Gets the available basic descriptions for the stream.
- [GetNumberAvailableStreamFormats](./getnumberavailablestreamformats.md)
  Gets the number of available description for the stream.
- [IOUserVideoStreamBasicDescription](../videodriverkit-page/iouservideostreambasicdescription.md)
  A structure that encapsulates all the information for describing the basic format properties of a stream of audio data.
- [GetStreamDirection](./getstreamdirection.md)
  Gets the direction of the stream.
- [IOUserVideoStreamDirection](../videodriverkit-page/iouservideostreamdirection.md)
  The direction of a video stream.
- [SetStreamIsActive](./setstreamisactive.md)
  Sets whether that the stream is active and doing IO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getstreamisactive)*