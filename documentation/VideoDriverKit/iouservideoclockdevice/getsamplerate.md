# GetSampleRate

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets sample rate of the clock device.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
double GetSampleRate();
```

## Discussion

The object’s work queue synchronizes access to the value.

## See Also

### Working with sample rates
- [SetSampleRate](./setsamplerate.md)
  Sets the current sample rate for the clock device.
- [SetAvailableSampleRates](./setavailablesamplerates.md)
  Sets the available sample rates for the clock device.
- [GetAvailableSampleRates](./getavailablesamplerates.md)
  Gets available sample rates of the clock device.
- [GetNumberAvailableSampleRates](./getnumberavailablesamplerates.md)
  Gets number of available sample rates of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getsamplerate)*