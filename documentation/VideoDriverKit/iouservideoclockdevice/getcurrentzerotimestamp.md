# GetCurrentZeroTimestamp

**Framework**: VideoDriverKit  
**Kind**: method

Gets the current zero timestamp value.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
void GetCurrentZeroTimestamp(uint64_t *out_sample_time, uint64_t *out_host_time);
```

## Parameters

- `out_sample_time`: Pointer to uint64_t that will be set with last updated sample time.
- `out_host_time`: Pointer to uint64_t that will be set with last updated host time.

## See Also

- [UpdateCurrentZeroTimestamp](iouservideoclockdevice/updatecurrentzerotimestamp.md)
  Update the current timestamp value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getcurrentzerotimestamp)*