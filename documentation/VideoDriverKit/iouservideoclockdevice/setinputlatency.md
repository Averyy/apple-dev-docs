# SetInputLatency

**Framework**: VideoDriverKit  
**Kind**: method

Sets the input latency of the clock device.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetInputLatency(uint32_t in_latency);
```

#### Return Value

A kern_return_t value indicating success or failure.

#### Discussion

Drivers can change the latency of the clock device dynamically. If successful, the clock device sends a notification to the host to update the object state. The object’s work queue synchronizes access to this value when it changes.

## Parameters

- `in_latency`: The uint32_t input latency value to set.

## See Also

- [SetOutputLatency](iouservideoclockdevice/setoutputlatency.md)
  Sets the output latency of the clock device.
- [GetOutputLatency](iouservideoclockdevice/getoutputlatency.md)
  Gets the output latency of the clock device.
- [GetInputLatency](iouservideoclockdevice/getinputlatency.md)
  Gets the input latency of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/setinputlatency)*