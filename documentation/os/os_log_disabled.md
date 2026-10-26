# OS_LOG_DISABLED

**Framework**: os  
**Kind**: macro  
**Role**: Macro

The shared disabled log.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
#define OS_LOG_DISABLED
```

#### Discussion

Passing this constant to an `os_log` function, such as `os_log`, `os_log_info`, `os_log_debug`, `os_log_error`, or `os_log_fault`, prevents the system from logging a message.

## See Also

### Getting the Standard Log Objects
- [OS_LOG_DEFAULT](./os_log_default.md)
  The shared default log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_log_disabled)*