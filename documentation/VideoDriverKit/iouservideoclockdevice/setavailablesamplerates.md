# SetAvailableSampleRates

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the available sample rates for the clock device.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t SetAvailableSampleRates(const double *in_sample_rates, size_t in_num_rates);
```

#### Discussion

Changing the available sample rates will send a notification to the host to update the object state if successful. The object’s work queue synchronizes access to the sample rates.

## Parameters

- `in_sample_rates`: Pointer to a buffer of double’’s with size corresponding to in_num_rates.
- `in_num_rates`: Size_t of the number of sample rates in in_sample_rates buffer.

## See Also

### Working with sample rates
- [SetSampleRate](./setsamplerate.md)
  Sets the current sample rate for the clock device.
- [GetSampleRate](./getsamplerate.md)
  Gets sample rate of the clock device.
- [GetAvailableSampleRates](./getavailablesamplerates.md)
  Gets available sample rates of the clock device.
- [GetNumberAvailableSampleRates](./getnumberavailablesamplerates.md)
  Gets number of available sample rates of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/setavailablesamplerates)*