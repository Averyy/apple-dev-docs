# DeviceSampleRateChanged

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Call to update stream formats when the owning video device changes sample rate.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t DeviceSampleRateChanged(double in_sample_rate);
```

## Discussion

Goes through all the available stream formats and selects the closet format with the matching sample rate. The system calls [`HandleChangeCurrentStreamFormat`](./handlechangecurrentstreamformat.md) on the stream to update its format.

## See Also

### Managing stream changes
- [HandleChangeCurrentStreamFormat](./handlechangecurrentstreamformat.md)
  The system calls this virtual method when the stream’s format changes.
- [HandleChangeStreamIsActive](./handlechangestreamisactive.md)
  The system calls this virtual method when the stream active state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideostream/devicesampleratechanged)*