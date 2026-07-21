# SetAvailableSampleRates

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetAvailableSampleRates(const double *in_sample_rates, size_t in_num_rates);
```

#### Return Value

Returns kern_return_t.

#### Discussion

Set the available sample rates for the clock device.

Changing the available sample rates will send a notification to the host to update the object state if successful. Setting the sample rates will be synchronized using the work queue created by the object.

## Parameters

- `in_sample_rates`: Pointer to a buffer of double’’s with size corresponding to in_num_rates.
- `in_num_rates`: Size_t of the number of sample rates in in_sample_rates buffer.

## See Also

- [SetSampleRate](iouservideoclockdevice/setsamplerate.md)
- [GetSampleRate](iouservideoclockdevice/getsamplerate.md)
- [GetAvailableSampleRates](iouservideoclockdevice/getavailablesamplerates.md)
- [GetNumberAvailableSampleRates](iouservideoclockdevice/getnumberavailablesamplerates.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/setavailablesamplerates)*