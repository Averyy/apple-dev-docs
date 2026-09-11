# DeviceSampleRateChanged

**Framework**: VideoDriverKit  
**Kind**: method

Call to update stream formats when the owning video device changes sample rate

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
kern_return_t DeviceSampleRateChanged(double in_sample_rate);
```

#### Discussion

Goes through all the available stream formats and selects the closet format with the matching sample rate. `HandleChangeCurrentStreamFormat()` will be called on the stream to update its format.

## See Also

- [HandleChangeCurrentStreamFormat](iouservideostream/handlechangecurrentstreamformat.md)
  The system calls this virtual method when the stream’s format changes.
- [HandleChangeStreamIsActive](iouservideostream/handlechangestreamisactive.md)
  The system calls this virtual method when the stream active state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/devicesampleratechanged)*