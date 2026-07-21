# GetOutputLatency

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
uint32_t GetOutputLatency();
```

#### Return Value

Returns uint32_t

#### Discussion

Get the output latency of the clock device

Getting the value will be synchronized using the work queue created by the object.

## See Also

- [SetOutputLatency](iouservideoclockdevice/setoutputlatency.md)
- [SetInputLatency](iouservideoclockdevice/setinputlatency.md)
- [GetInputLatency](iouservideoclockdevice/getinputlatency.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getoutputlatency)*