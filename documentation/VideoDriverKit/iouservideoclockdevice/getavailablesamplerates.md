# GetAvailableSampleRates

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
size_t GetAvailableSampleRates(double *out_sample_rates, size_t in_num_rates);
```

#### Return Value

Returns size_t indicating how many rates were set in the out_sample_rates buffer.

#### Discussion

Get availble sample rates of the clock device.

Getting the value will be synchronized using the work queue created by the object.

## Parameters

- `out_sample_rates`: Pointer to a buffer of double’s with size corresponding to in_num_rates
- `in_num_rates`: 

## See Also

- [SetSampleRate](iouservideoclockdevice/setsamplerate.md)
- [GetSampleRate](iouservideoclockdevice/getsamplerate.md)
- [SetAvailableSampleRates](iouservideoclockdevice/setavailablesamplerates.md)
- [GetNumberAvailableSampleRates](iouservideoclockdevice/getnumberavailablesamplerates.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getavailablesamplerates)*