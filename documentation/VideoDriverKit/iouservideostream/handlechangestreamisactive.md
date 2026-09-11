# HandleChangeStreamIsActive

**Framework**: VideoDriverKit  
**Kind**: method

The system calls this virtual method when the stream active state changes.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
virtual kern_return_t HandleChangeStreamIsActive(bool in_is_active);
```

#### Return Value

`kIOReturnSuccess` on success. Upon success the stream’s active state should be changed.

#### Discussion

The default implementation calls `SetStreamIsActive()` and returns `kIOReturnSuccess`. Subclass and override this method to handle changing stream active state and return `kIOReturnSuccess` upon success.

## See Also

- [HandleChangeCurrentStreamFormat](iouservideostream/handlechangecurrentstreamformat.md)
  The system calls this virtual method when the stream’s format changes.
- [DeviceSampleRateChanged](iouservideostream/devicesampleratechanged.md)
  Call to update stream formats when the owning video device changes sample rate


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/handlechangestreamisactive)*