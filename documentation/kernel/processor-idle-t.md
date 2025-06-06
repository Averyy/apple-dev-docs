# processor_idle_t

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 11.0+

## Declaration

```swift
typedef void (*processor_idle_t)(cpu_id_t cpu_id, boolean_t enter, uint64_t *new_timeout_ticks);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/processor_idle_t)*