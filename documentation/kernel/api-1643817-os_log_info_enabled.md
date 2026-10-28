# os_log_info_enabled

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Returns a Boolean value indicating whether info-level logging is enabled for a specified log object.

**Availability**:
- macOS 10.12+

## Declaration

```c
bool os_log_info_enabled(os_log_t log);
```

## Return Value

[`YES`](../ObjectiveC/yes.md) if info-level logging is enabled, otherwise [`NO`](../ObjectiveC/no.md).

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
- [os_log_debug_enabled](./api-1643808-os_log_debug_enabled.md)
  Returns a Boolean value indicating whether debug-level logging is enabled for a specified log object.
### Related Documentation
- [OS_LOG_TYPE_INFO](./os_log_type_t/os_log_type_info.md)
  Info-level messages are initially stored in memory buffers. Without a configuration change, they are not moved to the data store and are purged as memory buffers fill. They are, however, captured in the data store when faults and, optionally, errors occur. When info-level messages are added to the data store, they remain there until a storage quota is exceeded, at which point, the oldest messages are purged. Use this level to capture information that may be helpful, but isn’t essential, for troubleshooting errors. Logging a message of this type is equivalent to calling the  function.
- [isEnabled(type:)](../os/oslog/isenabled%28type%29.md)
  Returns a Boolean value that indicates whether the log can write messages with the specified log type.
- [pseudoSymbol-1841413](pseudoSymbol-1841413)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1643817-os_log_info_enabled)*