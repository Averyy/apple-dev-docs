# SetCurrentStreamFormat

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetCurrentStreamFormat(const IOUserVideoStreamBasicDescription *in_format);
```

#### Return Value

Returns kern_return_t

#### Discussion

Set the current stream format

Changing the format will send a notification to the host to update the object state if successful. Setting the stream format will be synchronized using the work queue created by the object.

## Parameters

- `in_format`: Pointer to a IOUserVideoStreamBasicDescription.

## See Also

- [GetCurrentStreamFormat](iouservideostream/getcurrentstreamformat.md)
- [SetAvailableStreamFormats](iouservideostream/setavailablestreamformats.md)
- [GetAvailableStreamFormats](iouservideostream/getavailablestreamformats.md)
- [GetNumberAvailableStreamFormats](iouservideostream/getnumberavailablestreamformats.md)
- [IOUserVideoStreamBasicDescription](videodriverkit/iouservideostreambasicdescription.md)
- [GetStreamDirection](iouservideostream/getstreamdirection.md)
- [IOUserVideoStreamDirection](videodriverkit/iouservideostreamdirection.md)
- [SetStreamIsActive](iouservideostream/setstreamisactive.md)
- [GetStreamIsActive](iouservideostream/getstreamisactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/setcurrentstreamformat)*