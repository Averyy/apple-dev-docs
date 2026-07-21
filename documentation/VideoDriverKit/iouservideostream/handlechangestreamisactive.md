# HandleChangeStreamIsActive

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t HandleChangeStreamIsActive(bool in_is_active);
```

#### Return Value

Returns kIOReturnSuccess on sucess. Upon sucess the stream’s active state should be changed

#### Discussion

Virtual method will be called when the stream active state is changed.

Default implementation will call SetStreamIsActive() and return kIOReturnSuccess. Subclass and override this method to handle changing stream active state and return kIOReturnSucess upon success.

## See Also

- [HandleChangeCurrentStreamFormat](iouservideostream/handlechangecurrentstreamformat.md)
- [DeviceSampleRateChanged](iouservideostream/devicesampleratechanged.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/handlechangestreamisactive)*