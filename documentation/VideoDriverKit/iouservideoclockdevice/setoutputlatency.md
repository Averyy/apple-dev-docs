# SetOutputLatency

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
kern_return_t SetOutputLatency(uint32_t in_latency);
```

#### Return Value

Returns kern_return_t.

#### Discussion

Set the output latency of the clock device.

Drivers can change the latency of the clock device dynamically.  A notification will be sent to the host to update the object state if successful. Setting the value will be synchronized using the work queue created by the object.

## Parameters

- `in_latency`: uint32_t output latency value to set.

## See Also

- [GetOutputLatency](iouservideoclockdevice/getoutputlatency.md)
- [SetInputLatency](iouservideoclockdevice/setinputlatency.md)
- [GetInputLatency](iouservideoclockdevice/getinputlatency.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/setoutputlatency)*