# GetCurrentStreamFormat

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
IOUserVideoStreamBasicDescription GetCurrentStreamFormat();
```

#### Return Value

Returns IOUserVideoStreamBasicDescription

#### Discussion

Get the current IOUserVideoStreamBasicDescription of the stream

Getting the current stream format will be synchronized using the work queue created by the object.

## See Also

- [SetCurrentStreamFormat](iouservideostream/setcurrentstreamformat.md)
- [SetAvailableStreamFormats](iouservideostream/setavailablestreamformats.md)
- [GetAvailableStreamFormats](iouservideostream/getavailablestreamformats.md)
- [GetNumberAvailableStreamFormats](iouservideostream/getnumberavailablestreamformats.md)
- [IOUserVideoStreamBasicDescription](videodriverkit/iouservideostreambasicdescription.md)
- [GetStreamDirection](iouservideostream/getstreamdirection.md)
- [IOUserVideoStreamDirection](videodriverkit/iouservideostreamdirection.md)
- [SetStreamIsActive](iouservideostream/setstreamisactive.md)
- [GetStreamIsActive](iouservideostream/getstreamisactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getcurrentstreamformat)*