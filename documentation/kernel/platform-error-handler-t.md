# platform_error_handler_t

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 11.0+

## Declaration

```swift
typedef void (*platform_error_handler_t)(void *refcon, vm_offset_t fault_addr);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/platform_error_handler_t)*