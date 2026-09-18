# SetOutputLatency

**Framework**: VideoDriverKit  
**Kind**: method

Sets the output latency of the clock device.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetOutputLatency(uint32_t in_latency);
```

#### Discussion

Drivers can change the latency of the clock device dynamically. The object sends a notification to the host to update the object state on success. The object’s work queue synchronizes access to the value.

## Parameters

- `in_latency`: uint32_t output latency value to set.

## See Also

- [GetOutputLatency](iouservideoclockdevice/getoutputlatency.md)
  Gets the output latency of the clock device.
- [SetInputLatency](iouservideoclockdevice/setinputlatency.md)
  Sets the input latency of the clock device.
- [GetInputLatency](iouservideoclockdevice/getinputlatency.md)
  Gets the input latency of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/setoutputlatency)*