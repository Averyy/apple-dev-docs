# SetStreamIsActive

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetStreamIsActive(bool in_is_active);
```

#### Return Value

Returns kern_return_t.

#### Discussion

Set the bool value indicating that the stream is active and doing IO.

Changing the stream active state will send a notification to the host to update the object state if successful. Setting the stream active state will be synchronized using the work queue created by the object.

## Parameters

- `in_is_active`: Bool value, where true indicates that the stream is enabled and doing IO.

## See Also

- [SetCurrentStreamFormat](iouservideostream/setcurrentstreamformat.md)
- [GetCurrentStreamFormat](iouservideostream/getcurrentstreamformat.md)
- [SetAvailableStreamFormats](iouservideostream/setavailablestreamformats.md)
- [GetAvailableStreamFormats](iouservideostream/getavailablestreamformats.md)
- [GetNumberAvailableStreamFormats](iouservideostream/getnumberavailablestreamformats.md)
- [IOUserVideoStreamBasicDescription](videodriverkit/iouservideostreambasicdescription.md)
- [GetStreamDirection](iouservideostream/getstreamdirection.md)
- [IOUserVideoStreamDirection](videodriverkit/iouservideostreamdirection.md)
- [GetStreamIsActive](iouservideostream/getstreamisactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/setstreamisactive)*