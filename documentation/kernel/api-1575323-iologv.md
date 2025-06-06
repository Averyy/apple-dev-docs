# IOLogv

**Framework**: Kernel  
**Kind**: func

Log a message to console in text mode, and /var/log/system.log.

**Availability**:
- DriverKit 24.4+
- macOS 10.6+

## Declaration

```swift
void IOLogv(const char *format, va_list ap);
```

#### Discussion

This function allows a driver to log diagnostic information to the screen during verbose boots, and to a log file found at /var/log/system.log. IOLogv should not be called from interrupt context.

## Parameters

- `format`: A printf() style format string (see printf(3) documentation).
- `ap`: stdarg(3) style variable arguments.

## See Also

- [OS_os_log](os_os_log.md)
- [IOLog](1575337-iolog.md)
  Log a message to console in text mode, and /var/log/system.log.
- [os_log_create](1643798-os_log_create.md)
  Creates a custom log object, to be passed to logging functions for sending messages to the logging system.
- [os_log_debug_enabled](1643808-os_log_debug_enabled.md)
  Returns a Boolean value indicating whether debug-level logging is enabled for a specified log object.
- [os_log_info_enabled](1643817-os_log_info_enabled.md)
  Returns a Boolean value indicating whether info-level logging is enabled for a specified log object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1575323-iologv)*