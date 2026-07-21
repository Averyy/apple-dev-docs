# SetSampleRate

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetSampleRate(double in_sample_rate);
```

#### Return Value

Returns kern_return_t.

#### Discussion

Set the current sample rate for the clock device.

Changing the sample rate will send a notification to the host to update the object state if successful. Setting the sample rate will be synchronized using the work queue created by the object.

## Parameters

- `in_sample_rate`: The sample rate to set on the clock device..

## See Also

- [GetSampleRate](iouservideoclockdevice/getsamplerate.md)
- [SetAvailableSampleRates](iouservideoclockdevice/setavailablesamplerates.md)
- [GetAvailableSampleRates](iouservideoclockdevice/getavailablesamplerates.md)
- [GetNumberAvailableSampleRates](iouservideoclockdevice/getnumberavailablesamplerates.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/setsamplerate)*