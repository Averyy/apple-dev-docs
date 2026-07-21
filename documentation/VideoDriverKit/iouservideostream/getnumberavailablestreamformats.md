# GetNumberAvailableStreamFormats

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
size_t GetNumberAvailableStreamFormats();
```

#### Return Value

Returns size_t

#### Discussion

Get the number of available IOUserVideoStreamBasicDescription’s for the stream

Getting the value will be synchronized using the work queue created by the object.

## See Also

- [SetCurrentStreamFormat](iouservideostream/setcurrentstreamformat.md)
- [GetCurrentStreamFormat](iouservideostream/getcurrentstreamformat.md)
- [SetAvailableStreamFormats](iouservideostream/setavailablestreamformats.md)
- [GetAvailableStreamFormats](iouservideostream/getavailablestreamformats.md)
- [IOUserVideoStreamBasicDescription](videodriverkit/iouservideostreambasicdescription.md)
- [GetStreamDirection](iouservideostream/getstreamdirection.md)
- [IOUserVideoStreamDirection](videodriverkit/iouservideostreamdirection.md)
- [SetStreamIsActive](iouservideostream/setstreamisactive.md)
- [GetStreamIsActive](iouservideostream/getstreamisactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getnumberavailablestreamformats)*