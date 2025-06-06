# Debugger

**Framework**: Kernel  
**Kind**: func

Enter the kernel debugger.

**Availability**:
- macOS 10.0+

## Declaration

```swift
void Debugger(const char *reason);
```

#### Discussion

This function freezes the kernel and enters the builtin debugger. It may not be possible to exit the debugger without a second machine.

## Parameters

- `reason`: A C-string to describe why the debugger is being entered.

## See Also

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
- [kernel_debug_enter](3242844-kernel_debug_enter.md)
- [kernel_debug_filtered](2123006-kernel_debug_filtered.md)
- [kernel_debug_flags](2977320-kernel_debug_flags.md)
- [kernel_debug_register_callback](3242845-kernel_debug_register_callback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1575299-debugger)*