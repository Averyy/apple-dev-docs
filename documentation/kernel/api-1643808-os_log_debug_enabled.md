# os_log_debug_enabled

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Returns a Boolean value indicating whether debug-level logging is enabled for a specified log object.

**Availability**:
- macOS 10.12+

## Declaration

```c
bool os_log_debug_enabled(os_log_t log);
```

#### Return Value

[`YES`](../ObjectiveC/yes.md) if debug-level logging is enabled, otherwise [`NO`](../ObjectiveC/no.md).

## Parameters

- `log`: The `OS_LOG_DEFAULT` constant or a custom log object previously created by the [`os_log_create`](./api-1643798-os_log_create.md) function.

## See Also

### Logging
- [OS_os_log](./os_os_log.md)
- [IOLog](./api-1575337-iolog.md)
  Log a message to console in text mode, and /var/log/system.log.
- [IOLogv](./api-1575323-iologv.md)
  Log a message to console in text mode, and /var/log/system.log.
- [os_log_create](./api-1643798-os_log_create.md)
  Creates a custom log object, to be passed to logging functions for sending messages to the logging system.
- [os_log_info_enabled](./api-1643817-os_log_info_enabled.md)
  Returns a Boolean value indicating whether info-level logging is enabled for a specified log object.
### Related Documentation
- [isEnabled(type:)](../os/oslog/isenabled%28type%29.md)
  Returns a Boolean value that indicates whether the log can write messages with the specified log type.
- [pseudoSymbol-1841414](pseudoSymbol-1841414)
- [OS_LOG_TYPE_DEBUG](./os_log_type_t/os_log_type_debug.md)
  Debug-level messages are only captured in memory when debug logging is enabled through a configuration change. They’re purged in accordance with the configuration’s persistence setting. Messages logged at this level contain information that may be useful during development or while troubleshooting a specific problem. Debug logging is intended for use in a development environment and not in shipping software. Logging a message of this type is equivalent to calling the  function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1643808-os_log_debug_enabled)*