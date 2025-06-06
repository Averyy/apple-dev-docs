# kernel_debug_enter

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.15+

## Declaration

```swift
void kernel_debug_enter(uint32_t coreid, uint32_t debugid, uint64_t timestamp, uintptr_t arg1, uintptr_t arg2, uintptr_t arg3, uintptr_t arg4, uintptr_t threadid);
```

## See Also

- [Debugger](1575299-debugger.md)
  Enter the kernel debugger.
- [kdbg_get_cpu](3197813-kdbg_get_cpu.md)
- [kdbg_get_timestamp](3197814-kdbg_get_timestamp.md)
- [kdbg_set_cpu](3197815-kdbg_set_cpu.md)
- [kdbg_set_timestamp](3197816-kdbg_set_timestamp.md)
- [kdbg_set_timestamp_and_cpu](3197817-kdbg_set_timestamp_and_cpu.md)
- [kdebug_commpage_state](3242840-kdebug_commpage_state.md)
- [kdebug_debugid_enabled](3242841-kdebug_debugid_enabled.md)
- [kdebug_debugid_explicitly_enabled](3242842-kdebug_debugid_explicitly_enable.md)
- [kdebug_using_continuous_time](3242843-kdebug_using_continuous_time.md)
- [kernel_debug](1568810-kernel_debug.md)
- [kernel_debug1](1568762-kernel_debug1.md)
- [kernel_debug_filtered](2123006-kernel_debug_filtered.md)
- [kernel_debug_flags](2977320-kernel_debug_flags.md)
- [kernel_debug_register_callback](3242845-kernel_debug_register_callback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3242844-kernel_debug_enter)*