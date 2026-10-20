# SetCurrentStreamFormat

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the current stream format.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t SetCurrentStreamFormat(const IOUserVideoStreamBasicDescription *in_format);
```

#### Discussion

Changing the format send sa notification to the host to update the object state if successful. The object’s work queue synchronizes access to the stream format.

## Parameters

- `in_format`: Pointer to a description.

## See Also

### Working with stream formats
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
- [GetStreamIsActive](./getstreamisactive.md)
  Gets the stream activity state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/setcurrentstreamformat)*