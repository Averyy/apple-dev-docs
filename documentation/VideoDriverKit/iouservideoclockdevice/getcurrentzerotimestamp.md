# GetCurrentZeroTimestamp

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
void GetCurrentZeroTimestamp(uint64_t *out_sample_time, uint64_t *out_host_time);
```

#### Discussion

Get the current zero timestamp value.

## Parameters

- `out_sample_time`: Pointer to uint64_t that will be set with last updated sample time.
- `out_host_time`: Pointer to uint64_t that will be set with last updated host time.

## See Also

- [UpdateCurrentZeroTimestamp](iouservideoclockdevice/updatecurrentzerotimestamp.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getcurrentzerotimestamp)*