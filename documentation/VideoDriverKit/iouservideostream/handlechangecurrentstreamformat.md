# HandleChangeCurrentStreamFormat

**Framework**: VideoDriverKit  
**Kind**: method

The system calls this virtual method when the stream’s format changes.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
virtual kern_return_t HandleChangeCurrentStreamFormat(const IOUserVideoStreamBasicDescription *in_format);
```

#### Return Value

`kIOReturnSuccess` on success. Upon success the stream’s format should be updated.

#### Discussion

The default implementation calls `SetCurrentStreamFormat()` and returns `kIOReturnSuccess`. Subclass and override this method to handle changing stream format and return `kIOReturnSuccess` upon success.

## Parameters

- `in_format`: Pointer to a basic description, to be set on the stream.

## See Also

- [HandleChangeStreamIsActive](iouservideostream/handlechangestreamisactive.md)
  The system calls this virtual method when the stream active state changes.
- [DeviceSampleRateChanged](iouservideostream/devicesampleratechanged.md)
  Call to update stream formats when the owning video device changes sample rate


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/handlechangecurrentstreamformat)*