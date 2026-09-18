# HandleChangeSampleRate

**Framework**: VideoDriverKit  
**Kind**: method

The system calls this virtual method when the clock device’s sample rate changes.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
virtual kern_return_t HandleChangeSampleRate(double in_sample_rate);
```

#### Return Value

`kIOReturnSuccess` on success. Upon success the value should be updated.

#### Discussion

The default implementation calls SetSampleRate() and returns `kIOReturnSuccess`. Subclass and override this method to handle changes to this value and return `kIOReturnSuccess` upon success.

## Parameters

- `in_sample_rate`: The double sample rate attempting to be set on the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/handlechangesamplerate)*