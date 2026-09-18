# GetCurrentClientSampleTime

**Framework**: VideoDriverKit  
**Kind**: method

Gets the current sample time in the ring buffer that the client reads from and writes to.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
void GetCurrentClientSampleTime(uint64_t *out_input_sample_time, uint64_t *out_output_sample_time);
```

## Parameters

- `out_input_sample_time`: A pointer to a uint64_t value that this method sets to the current input sample time the client reads.
- `out_output_sample_time`: A pointer to a uint64_t value that this method sets to the current output sample time the client writes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getcurrentclientsampletime)*