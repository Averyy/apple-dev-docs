# HandleChangeSampleRate

**Framework**: VideoDriverKit  
**Kind**: method

The system calls this virtual method when the device’s sample rate changes.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
virtual kern_return_t HandleChangeSampleRate(double in_sample_rate);
```

#### Return Value

`kIOReturnSuccess` on success. Upon success the control’s value should be updated.

#### Discussion

The default implementation calls SetSampleRate() and returns `kIOReturnSuccess`. Subclass can override this method to handle changes to this value and should return `kIOReturnSuccess` upon success.

## Parameters

- `in_sample_rate`: The double sample rate attempting to be set on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice/handlechangesamplerate)*