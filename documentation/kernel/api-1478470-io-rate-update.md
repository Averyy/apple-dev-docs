# io_rate_update

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.10+

## Declaration

```swift
uint64_t io_rate_update(uint64_t io_rate_flags, uint64_t read_ops_delta, uint64_t write_ops_delta, uint64_t read_bytes_delta, uint64_t write_bytes_delta);
```

## See Also

- [io_rate_update_register](1478504-io_rate_update_register.md)
- [gpu_accumulate_time](1478468-gpu_accumulate_time.md)
- [gpu_describe](1478509-gpu_describe.md)
- [gpu_fceiling_cb_register](1478505-gpu_fceiling_cb_register.md)
- [gpu_submission_telemetry](1478498-gpu_submission_telemetry.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1478470-io_rate_update)*