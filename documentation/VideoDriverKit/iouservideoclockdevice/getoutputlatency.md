# GetOutputLatency

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the output latency of the clock device.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
uint32_t GetOutputLatency();
```

#### Discussion

The object’s work queue synchronizes access to the value.

## See Also

### Working with timing and latency
- [SetOutputLatency](./setoutputlatency.md)
  Sets the output latency of the clock device.
- [SetInputLatency](./setinputlatency.md)
  Sets the input latency of the clock device.
- [GetInputLatency](./getinputlatency.md)
  Gets the input latency of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getoutputlatency)*