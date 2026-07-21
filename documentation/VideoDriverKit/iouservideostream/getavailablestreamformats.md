# GetAvailableStreamFormats

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
size_t GetAvailableStreamFormats(IOUserVideoStreamBasicDescription *out_formats, size_t in_num_formats);
```

#### Return Value

Returns size_t indicating how many formats were set in out_formats buffer.

#### Discussion

Get the available IOUserVideoStreamBasicDescription’s for the stream.

Getting the value will be synchronized using the work queue created by the object.

## Parameters

- `out_formats`: Pointer to a buffer of IOUserVideoStreamBasicDescription’s with size corresponding to in_num_formats.
- `in_num_formats`: Size_t of the number of formats in out_formats buffer.

## See Also

- [SetCurrentStreamFormat](iouservideostream/setcurrentstreamformat.md)
- [GetCurrentStreamFormat](iouservideostream/getcurrentstreamformat.md)
- [SetAvailableStreamFormats](iouservideostream/setavailablestreamformats.md)
- [GetNumberAvailableStreamFormats](iouservideostream/getnumberavailablestreamformats.md)
- [IOUserVideoStreamBasicDescription](videodriverkit/iouservideostreambasicdescription.md)
- [GetStreamDirection](iouservideostream/getstreamdirection.md)
- [IOUserVideoStreamDirection](videodriverkit/iouservideostreamdirection.md)
- [SetStreamIsActive](iouservideostream/setstreamisactive.md)
- [GetStreamIsActive](iouservideostream/getstreamisactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/getavailablestreamformats)*