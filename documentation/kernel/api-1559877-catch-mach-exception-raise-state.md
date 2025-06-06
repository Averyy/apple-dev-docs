# catch_mach_exception_raise_state

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.5+

## Declaration

```swift
kern_return_t catch_mach_exception_raise_state(mach_port_t exception_port, exception_type_t exception, const mach_exception_data_t code, mach_msg_type_number_t codeCnt, int *flavor, const thread_state_t old_state, mach_msg_type_number_t old_stateCnt, thread_state_t new_state, mach_msg_type_number_t *new_stateCnt);
```

## See Also

- [catch_exception_raise](1537287-catch_exception_raise.md)
- [catch_exception_raise_state](1537255-catch_exception_raise_state.md)
- [catch_exception_raise_state_identity](1537251-catch_exception_raise_state_iden.md)
- [catch_mach_exception_raise](1559883-catch_mach_exception_raise.md)
- [catch_mach_exception_raise_state_identity](1559863-catch_mach_exception_raise_state.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1559877-catch_mach_exception_raise_state)*