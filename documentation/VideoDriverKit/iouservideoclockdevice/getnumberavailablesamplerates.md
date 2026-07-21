# GetNumberAvailableSampleRates

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
size_t GetNumberAvailableSampleRates();
```

#### Return Value

Returns size_t.

#### Discussion

Get number of available sample rates of the clock device.

Getting the value will be synchronized using the work queue created by the object.

## See Also

- [SetSampleRate](iouservideoclockdevice/setsamplerate.md)
- [GetSampleRate](iouservideoclockdevice/getsamplerate.md)
- [SetAvailableSampleRates](iouservideoclockdevice/setavailablesamplerates.md)
- [GetAvailableSampleRates](iouservideoclockdevice/getavailablesamplerates.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getnumberavailablesamplerates)*