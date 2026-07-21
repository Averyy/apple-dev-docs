# UpdateCurrentZeroTimestamp

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
void UpdateCurrentZeroTimestamp(uint64_t in_sample_time, uint64_t in_host_time);
```

#### Discussion

Update the current timestamp value.

Updating the current timestamp should use the time passed in the hardware interrupt.

## Parameters

- `in_sample_time`: uint64_t the most current sample time being tracked by the hardware device.
- `in_host_time`: uint64_t the most current host time being tracked by the hardware device.

## See Also

- [GetCurrentZeroTimestamp](iouservideoclockdevice/getcurrentzerotimestamp.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/updatecurrentzerotimestamp)*