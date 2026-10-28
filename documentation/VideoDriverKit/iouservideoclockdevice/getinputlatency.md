# GetInputLatency

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the input latency of the clock device.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
uint32_t GetInputLatency();
```

## Discussion

The object’s work queue synchronizes access to the value.

## See Also

### Working with timing and latency
- [SetOutputLatency](./setoutputlatency.md)
  Sets the output latency of the clock device.
- [GetOutputLatency](./getoutputlatency.md)
  Gets the output latency of the clock device.
- [SetInputLatency](./setinputlatency.md)
  Sets the input latency of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getinputlatency)*