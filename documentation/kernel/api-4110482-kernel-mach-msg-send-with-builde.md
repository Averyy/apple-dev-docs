# kernel_mach_msg_send_with_builder

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 13.1+

## Declaration

```swift
mach_msg_return_t kernel_mach_msg_send_with_builder(mach_msg_size_t descriptor_count, mach_msg_size_t payload_size, void (^builder)(mach_msg_header_t *header, mach_msg_descriptor_t *descs, void *payload));
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/4110482-kernel_mach_msg_send_with_builde)*