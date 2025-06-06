# vm_remap_new

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 11.3+

## Declaration

```swift
kern_return_t vm_remap_new(vm_map_t target_task, vm_address_t *target_address, vm_size_t size, vm_address_t mask, int flags, vm_map_read_t src_task, vm_address_t src_address, boolean_t copy, vm_prot_t *cur_protection, vm_prot_t *max_protection, vm_inherit_t inheritance);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3728001-vm_remap_new)*