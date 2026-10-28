# OS_LOG_DEFAULT

**Framework**: os  
**Kind**: macro  
**Role**: Macro

The shared default log.

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
#define OS_LOG_DEFAULT
```

## Discussion

Passing this constant to an `os_log` function, such as [`os_log`](./os_log.md), [`os_log_info`](./os_log_info.md), [`os_log_debug`](./os_log_debug.md), [`os_log_error`](./os_log_error.md), or [`os_log_fault`](./os_log_fault.md), causes the system to log a message with the system’s standard behavior.

## See Also

### Getting the Standard Log Objects
- [OS_LOG_DISABLED](./os_log_disabled.md)
  The shared disabled log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_log_default)*