# idle_timer_t

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 11.0+

## Declaration

```c
typedef void (*idle_timer_t)(void *refcon, uint64_t *new_timeout_ticks);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/idle_timer_t)*