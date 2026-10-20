# catch_exception_raise

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```c
kern_return_t catch_exception_raise(mach_port_t exception_port, mach_port_t thread, mach_port_t task, exception_type_t exception, exception_data_t code, mach_msg_type_number_t codeCnt);
```

## See Also

### Exceptions
- [catch_exception_raise_state](./api-1537255-catch_exception_raise_state.md)
- [catch_exception_raise_state_identity](./api-1537251-catch_exception_raise_state_iden.md)
- [catch_mach_exception_raise](./api-1559883-catch_mach_exception_raise.md)
- [catch_mach_exception_raise_state](./api-1559877-catch_mach_exception_raise_state.md)
- [catch_mach_exception_raise_state_identity](./api-1559863-catch_mach_exception_raise_state.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1537287-catch_exception_raise)*