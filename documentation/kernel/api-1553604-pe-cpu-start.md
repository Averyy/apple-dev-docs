# PE_cpu_start

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.0+

## Declaration

```swift
kern_return_t PE_cpu_start(cpu_id_t target, vm_offset_t start_paddr, vm_offset_t arg_paddr);
```

## See Also

- [PE_cpu_halt](1553664-pe_cpu_halt.md)
- [PE_cpu_machine_init](1553675-pe_cpu_machine_init.md)
- [PE_cpu_machine_quiesce](1553608-pe_cpu_machine_quiesce.md)
- [PE_cpu_signal](1553636-pe_cpu_signal.md)
- [PE_cpu_signal_cancel](1553700-pe_cpu_signal_cancel.md)
- [PE_cpu_signal_deferred](1553622-pe_cpu_signal_deferred.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1553604-pe_cpu_start)*