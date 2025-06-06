# gpu_accumulate_time

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.10+

## Declaration

```swift
uint64_t gpu_accumulate_time(uint32_t scope, uint32_t gpu_id, uint32_t gpu_domain, uint64_t gpu_accumulated_ns, uint64_t gpu_tstamp_ns);
```

## See Also

- [io_rate_update](1478470-io_rate_update.md)
- [io_rate_update_register](1478504-io_rate_update_register.md)
- [gpu_describe](1478509-gpu_describe.md)
- [gpu_fceiling_cb_register](1478505-gpu_fceiling_cb_register.md)
- [gpu_submission_telemetry](1478498-gpu_submission_telemetry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1478468-gpu_accumulate_time)*