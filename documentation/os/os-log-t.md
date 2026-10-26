# os_log_t

**Framework**: os  
**Role**: API Collection

A log object that you pass to logging functions to send messages to that log.

## Topics

### Getting the Standard Log Objects
- [OS_LOG_DEFAULT](./os_log_default.md)
  The shared default log.
- [OS_LOG_DISABLED](./os_log_disabled.md)
  The shared disabled log.
### Creating a Log Object
- [os_log_create](./os_log_create.md)
  Creates a custom log object.
### Getting Log Configuration
- [os_log_info_enabled](./os_log_info_enabled.md)
  Returns a Boolean value that indicates whether info-level logging is in an enabled state for a specified log object.
- [os_log_debug_enabled](./os_log_debug_enabled.md)
  Returns a Boolean value that indicates whether debug-level logging is in an enabled state for a specified log object.
- [os_log_type_enabled](./oslog/isenabled%28type%29.md)
  Returns a Boolean value that indicates whether the log can write messages with the specified log type.
- [os_signpost_enabled](./os_signpost_enabled.md)
  Returns a Boolean value that indicates whether signposts are in an enabled state for the specified log.
### Data Types
- [os_log_t](./os_log_t.md)
  A log object that you pass to logging functions to send messages to that log.

## See Also

### Log Messages
- [Message Argument Formatters](./message-argument-formatters.md)
  Manage the privacy and presentation of the message’s interpolated values using type-aware formatters.
- [Legacy Logging Symbols](./legacy-logging-symbols.md)
  Migrate your code away from using these legacy symbols.
- [os_log_with_type](./os_log_with_type.md)
  Sends a message at a specific logging level, such as default, info, debug, error, or fault, to the logging system.
- [os_log_type_t](./oslogtype.md)
  The various log levels that the unified logging system provides.
- [os_log](./os_log.md)
  Sends a default-level message to the logging system.
- [os_log_info](./os_log_info.md)
  Sends an info-level message to the logging system.
- [os_log_debug](./os_log_debug.md)
  Sends a debug-level message to the logging system.
- [os_log_error](./os_log_error.md)
  Sends an error-level message to the logging system.
- [os_log_fault](./os_log_fault.md)
  Sends a fault-level message to the logging system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os-log-t)*