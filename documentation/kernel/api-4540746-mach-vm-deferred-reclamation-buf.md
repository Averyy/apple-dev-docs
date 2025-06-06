# mach_vm_deferred_reclamation_buffer_allocate

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 15.4+

## Declaration

```swift
kern_return_t mach_vm_deferred_reclamation_buffer_allocate(task_t target_task, mach_vm_address_t *address, uint32_t len, uint32_t max_len);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/4540746-mach_vm_deferred_reclamation_buf)*