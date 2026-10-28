# GetAvailableSampleRates

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets available sample rates of the clock device.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
size_t GetAvailableSampleRates(double *out_sample_rates, size_t in_num_rates);
```

## Return Value

The number of rates that were set in the `out_sample_rates` buffer.

## Discussion

The object’s work queue synchronizes access to the value.

## Parameters

- `out_sample_rates`: A pointer to a buffer of sample rates.
- `in_num_rates`: The number of rates in the buffer.

## See Also

### Working with sample rates
- [SetSampleRate](./setsamplerate.md)
  Sets the current sample rate for the clock device.
- [GetSampleRate](./getsamplerate.md)
  Gets sample rate of the clock device.
- [SetAvailableSampleRates](./setavailablesamplerates.md)
  Sets the available sample rates for the clock device.
- [GetNumberAvailableSampleRates](./getnumberavailablesamplerates.md)
  Gets number of available sample rates of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getavailablesamplerates)*