# kdebug_register_coproc

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 12.0+

## Declaration

```swift
int kdebug_register_coproc(const char *name, kdebug_coproc_flags_t flags, kd_callback_fn callback, void *context);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3755390-kdebug_register_coproc)*