# HandleChangeCurrentStreamFormat

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t HandleChangeCurrentStreamFormat(const IOUserVideoStreamBasicDescription *in_format);
```

#### Return Value

Returns kIOReturnSuccess on sucess. Upon sucess the stream’s format should be updated.

#### Discussion

Virtual method will be called when the streams format will be changed

Default implementation will call SetCurrentStreamFormat() and return kIOReturnSuccess. Subclass and override this method to handle changing stream format and return kIOReturnSucess upon success.

## Parameters

- `in_format`: Pointer to IOUserVideoStreamBasicDescription attempting to be set on the stream.

## See Also

- [HandleChangeStreamIsActive](iouservideostream/handlechangestreamisactive.md)
- [DeviceSampleRateChanged](iouservideostream/devicesampleratechanged.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/handlechangecurrentstreamformat)*