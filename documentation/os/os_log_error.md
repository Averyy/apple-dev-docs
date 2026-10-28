# os_log_error

**Framework**: os  
**Kind**: macro  
**Role**: Macro

Sends an error-level message to the logging system.

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
#define os_log_error(log, format, ...)
```

## Discussion

Calling this function is equivalent to calling the [`os_log_with_type`](./os_log_with_type.md) function and specifying a log type of [`OS_LOG_TYPE_ERROR`](../kernel/os_log_type_t/os_log_type_error.md).

## Parameters

- `log`: The [`OS_LOG_DEFAULT`](./os_log_default.md) constant or a custom log object previously created by the [`os_log_create`](./os_log_create.md) function.
- `format`: A constant string or format string that produces a human-readable log message. See [String Format Specifiers](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265).

## See Also

### Related Documentation
- [OS_LOG_TYPE_ERROR](../kernel/os_log_type_t/os_log_type_error.md)
  Error-level messages are always saved in the data store. They remain there until a storage quota is exceeded, at which point, the oldest messages are purged. Error-level messages are intended for reporting process-level errors. If an activity object exists, logging at this level captures information for the entire process chain. Logging a message of this type is equivalent to calling the  function.
### Log Messages
- [Message Argument Formatters](./message-argument-formatters.md)
  Manage the privacy and presentation of the message’s interpolated values using type-aware formatters.
- [Legacy Logging Symbols](./legacy-logging-symbols.md)
  Migrate your code away from using these legacy symbols.
- [os_log_t](./os-log-t.md)
  A log object that you pass to logging functions to send messages to that log.
- [os_log_with_type](./os_log_with_type.md)
  Sends a message at a specific logging level, such as default, info, debug, error, or fault, to the logging system.
- [struct OSLogType](./oslogtype.md)
  The various log levels that the unified logging system provides.
- [os_log](./os_log.md)
  Sends a default-level message to the logging system.
- [os_log_info](./os_log_info.md)
  Sends an info-level message to the logging system.
- [os_log_debug](./os_log_debug.md)
  Sends a debug-level message to the logging system.
- [os_log_fault](./os_log_fault.md)
  Sends a fault-level message to the logging system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_log_error)*