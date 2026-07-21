# SetAvailableStreamFormats

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetAvailableStreamFormats(const IOUserVideoStreamBasicDescription *in_formats, uint32_t in_num_formats);
```

#### Return Value

Returns kern_return_t.

#### Discussion

Set the available IOUserVideoStreamBasicDescription’s for the stream.

Changing the available formats will send a notification to the host to update the object state if successful. Setting the stream formats will be synchronized using the work queue created by the object.

## Parameters

- `in_formats`: Pointer to a buffer of IOUserVideoStreamBasicDescription’s with size corresponding to in_num_formats.
- `in_num_formats`: Size_t of the number of formats in in_formats buffer.

## See Also

- [SetCurrentStreamFormat](iouservideostream/setcurrentstreamformat.md)
- [GetCurrentStreamFormat](iouservideostream/getcurrentstreamformat.md)
- [GetAvailableStreamFormats](iouservideostream/getavailablestreamformats.md)
- [GetNumberAvailableStreamFormats](iouservideostream/getnumberavailablestreamformats.md)
- [IOUserVideoStreamBasicDescription](videodriverkit/iouservideostreambasicdescription.md)
- [GetStreamDirection](iouservideostream/getstreamdirection.md)
- [IOUserVideoStreamDirection](videodriverkit/iouservideostreamdirection.md)
- [SetStreamIsActive](iouservideostream/setstreamisactive.md)
- [GetStreamIsActive](iouservideostream/getstreamisactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/setavailablestreamformats)*