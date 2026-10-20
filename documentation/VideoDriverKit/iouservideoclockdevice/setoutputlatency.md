# SetOutputLatency

**Framework**: VideoDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the output latency of the clock device.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
kern_return_t SetOutputLatency(uint32_t in_latency);
```

#### Discussion

Drivers can change the latency of the clock device dynamically. The object sends a notification to the host to update the object state on success. The object’s work queue synchronizes access to the value.

## Parameters

- `in_latency`: uint32_t output latency value to set.

## See Also

### Working with timing and latency
- [GetOutputLatency](./getoutputlatency.md)
  Gets the output latency of the clock device.
- [SetInputLatency](./setinputlatency.md)
  Sets the input latency of the clock device.
- [GetInputLatency](./getinputlatency.md)
  Gets the input latency of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/setoutputlatency)*