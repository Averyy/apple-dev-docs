# arcade_upcall

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.15+

## Declaration

```swift
kern_return_t arcade_upcall(mach_port_t arcade_upcall, vm_offset_t path, mach_msg_type_number_t pathCnt, uint64_t offset, boolean_t *should_kill);
```

## See Also

- [mig_allocate](1558649-mig_allocate.md)
- [mig_dealloc_reply_port](1558668-mig_dealloc_reply_port.md)
- [mig_deallocate](1558654-mig_deallocate.md)
- [mig_get_reply_port](1558662-mig_get_reply_port.md)
- [mig_put_reply_port](1558665-mig_put_reply_port.md)
- [mig_strncpy](1558639-mig_strncpy.md)
- [mig_strncpy_zerofill](1645207-mig_strncpy_zerofill.md)
- [arcade_upcall_server](3281829-arcade_upcall_server.md)
- [arcade_upcall_server_routine](3281830-arcade_upcall_server_routine.md)
- [mig_impl_routine_t](mig_impl_routine_t.md)
- [mig_routine_arg_descriptor_t](mig_routine_arg_descriptor_t.md)
- [mig_routine_descriptor_t](mig_routine_descriptor_t.md)
- [mig_routine_t](mig_routine_t.md)
- [mig_server_routine_t](mig_server_routine_t.md)
- [mig_stub_routine_t](mig_stub_routine_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/3281827-arcade_upcall)*