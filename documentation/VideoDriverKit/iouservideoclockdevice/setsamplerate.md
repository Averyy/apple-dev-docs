# SetSampleRate

**Framework**: VideoDriverKit  
**Kind**: method

Sets the current sample rate for the clock device.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetSampleRate(double in_sample_rate);
```

#### Discussion

Changing the sample rate will send a notification to the host to update the object state if successful. The object’s work queue synchronizes access to the sample rate.

## Parameters

- `in_sample_rate`: The sample rate to set on the clock device..

## See Also

- [GetSampleRate](iouservideoclockdevice/getsamplerate.md)
  Gets sample rate of the clock device.
- [SetAvailableSampleRates](iouservideoclockdevice/setavailablesamplerates.md)
  Sets the available sample rates for the clock device.
- [GetAvailableSampleRates](iouservideoclockdevice/getavailablesamplerates.md)
  Gets available sample rates of the clock device.
- [GetNumberAvailableSampleRates](iouservideoclockdevice/getnumberavailablesamplerates.md)
  Gets number of available sample rates of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/setsamplerate)*