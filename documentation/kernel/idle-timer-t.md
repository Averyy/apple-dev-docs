# idle_timer_t

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 11.0+

## Declaration

```swift
typedef void (*idle_timer_t)(void *refcon, uint64_t *new_timeout_ticks);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/idle_timer_t)*