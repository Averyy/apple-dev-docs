# gpu_submission_telemetry

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.11+

## Declaration

```swift
void gpu_submission_telemetry(uint64_t gpu_ncmds_total, uint64_t gpu_noutstanding, uint64_t gpu_busy_ns_total, uint64_t gpu_cycles, uint64_t gpu_telemetry_valid_flags, uint64_t gpu_telemetry_misc);
```

## See Also

- [io_rate_update](1478470-io_rate_update.md)
- [io_rate_update_register](1478504-io_rate_update_register.md)
- [gpu_accumulate_time](1478468-gpu_accumulate_time.md)
- [gpu_describe](1478509-gpu_describe.md)
- [gpu_fceiling_cb_register](1478505-gpu_fceiling_cb_register.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1478498-gpu_submission_telemetry)*