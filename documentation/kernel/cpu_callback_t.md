# cpu_callback_t

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 11.0+

## Declaration

```c
typedef bool (*cpu_callback_t)(void *param, enum cpu_event event, unsigned int cpu_or_cluster);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/cpu_callback_t)*