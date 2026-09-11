# GetAvailableSampleRates

**Framework**: VideoDriverKit  
**Kind**: method

Gets available sample rates of the clock device.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
size_t GetAvailableSampleRates(double *out_sample_rates, size_t in_num_rates);
```

#### Return Value

Size_t indicating how many rates were set in the out_sample_rates buffer.

#### Discussion

The object’s work queue synchronizes access to the value.

## Parameters

- `out_sample_rates`: Pointer to a buffer of double’s with size corresponding to in_num_rates
- `in_num_rates`: 

## See Also

- [SetSampleRate](iouservideoclockdevice/setsamplerate.md)
  Sets the current sample rate for the clock device.
- [GetSampleRate](iouservideoclockdevice/getsamplerate.md)
  Gets sample rate of the clock device.
- [SetAvailableSampleRates](iouservideoclockdevice/setavailablesamplerates.md)
  Sets the available sample rates for the clock device.
- [GetNumberAvailableSampleRates](iouservideoclockdevice/getnumberavailablesamplerates.md)
  Gets number of available sample rates of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getavailablesamplerates)*