# HandleChangeSampleRate

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t HandleChangeSampleRate(double in_sample_rate);
```

#### Return Value

Returns kIOReturnSuccess on sucess. Upon sucess the controls value should be updated.

#### Discussion

Virtual method will be called when the device’s sample rate will be changed.

Default implementation will call SetSampleRate() and return kIOReturnSuccess. Subclass can override this method to handle changes to this value and should return kIOReturnSucess upon success.

## Parameters

- `in_sample_rate`: The double sample rate attempting to be set on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/handlechangesamplerate)*