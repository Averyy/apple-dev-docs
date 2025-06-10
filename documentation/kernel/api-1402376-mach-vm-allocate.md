# mach_vm_allocate

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
kern_return_t mach_vm_allocate(vm_map_t target, mach_vm_address_t *address, mach_vm_size_t size, int flags);
```

## See Also

- [mach_vm_deallocate](1402285-mach_vm_deallocate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1402376-mach_vm_allocate)*