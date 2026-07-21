# GetCurrentClientSampleTime

**Framework**: VideoDriverKit  
**Kind**: method

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
void GetCurrentClientSampleTime(uint64_t *out_input_sample_time, uint64_t *out_output_sample_time);
```

#### Discussion

Get the current sample time in the ring buffer written to/read from by the client

## Parameters

- `out_input_sample_time`: Pointer to uint64_t that will be set with the current input sample time read by the client.
- `out_output_sample_time`: Pointer to uint64_t that will be set with the current output sample time written by the client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice/getcurrentclientsampletime)*