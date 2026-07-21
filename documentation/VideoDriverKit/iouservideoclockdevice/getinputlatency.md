# GetInputLatency

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
uint32_t GetInputLatency();
```

#### Return Value

Returns uint32_t

#### Discussion

Get the input latency of the clock device

Getting the value will be synchronized using the work queue created by the object.

## See Also

- [SetOutputLatency](iouservideoclockdevice/setoutputlatency.md)
- [GetOutputLatency](iouservideoclockdevice/getoutputlatency.md)
- [SetInputLatency](iouservideoclockdevice/setinputlatency.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getinputlatency)*