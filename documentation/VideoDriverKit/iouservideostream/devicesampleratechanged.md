# DeviceSampleRateChanged

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t DeviceSampleRateChanged(double in_sample_rate);
```

#### Return Value

Kern_return_t

#### Discussion

Call to update stream formats when the owning video device changes sample rate

Goes through all the available stream formats and selects the closet format with the matching sample rate. HandleChangeCurrentStreamFormat() will be called on the stream to update its format.

## See Also

- [HandleChangeCurrentStreamFormat](iouservideostream/handlechangecurrentstreamformat.md)
- [HandleChangeStreamIsActive](iouservideostream/handlechangestreamisactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/devicesampleratechanged)*