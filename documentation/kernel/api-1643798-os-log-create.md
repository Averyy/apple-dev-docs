# os_log_create

**Framework**: Kernel  
**Kind**: func

Creates a custom log object, to be passed to logging functions for sending messages to the logging system.

**Availability**:
- macOS 10.12+

## Declaration

```swift
os_log_t os_log_create(const char *subsystem, const char *category);
```

#### Return_value

A value of type `os_log_t`, which can be passed to other logging functions to perform logging and to determine whether a specific level of logging is enabled. A value is always returned and should be released when no longer needed.

#### Discussion

Generally, use the `OS_LOG_DEFAULT` constant to perform logging using the system’s behavior. Create a custom log object only when you want to tag messages with a specific subsystem and category for the purpose of filtering, or to customize the logging behavior of your subsystem with a profile for debugging purposes. This function only needs to be called once to initialize a custom log object. It doesn’t need to be called again when changing logging settings. The system automatically detects changes to logging settings.

## Parameters

- `subsystem`: An identifier string, in reverse DNS notation, representing the subsystem that’s performing logging. For example,  . The subsystem is used for categorization and filtering of related log messages, as well as for grouping related logging settings.
- `category`: A category within the specified subsystem. The category is used for categorization and filtering of related log messages, as well as for grouping related logging settings within the subsystem’s settings. A category’s logging settings override those of the parent subsystem.

## See Also

- [OS_os_log](os_os_log.md)
- [IOLog](1575337-iolog.md)
  Log a message to console in text mode, and /var/log/system.log.
- [IOLogv](1575323-iologv.md)
  Log a message to console in text mode, and /var/log/system.log.
- [os_log_debug_enabled](1643808-os_log_debug_enabled.md)
  Returns a Boolean value indicating whether debug-level logging is enabled for a specified log object.
- [os_log_info_enabled](1643817-os_log_info_enabled.md)
  Returns a Boolean value indicating whether info-level logging is enabled for a specified log object.
- [OS_LOG_TYPE_DEFAULT](os_log_type_t/os_log_type_default.md)
  Default-level messages are initially stored in memory buffers. Without a configuration change, they are compressed and moved to the data store as memory buffers fill. They remain there until a storage quota is exceeded, at which point, the oldest messages are purged. Use this level to capture information about things that  result a failure. Logging a message of this type is equivalent to calling the  function.
- [pseudoSymbol-1841412](pseudoSymbol-1841412)
- [pseudoSymbol-1841415](pseudoSymbol-1841415)
- [pseudoSymbol-1841417](pseudoSymbol-1841417)
- [isEnabled(type:)](../os/oslog/isenabled(type:).md)
  Returns a Boolean value that indicates whether the log can write messages with the specified log type.
- [pseudoSymbol-1841413](pseudoSymbol-1841413)
- [pseudoSymbol-1841414](pseudoSymbol-1841414)
- [pseudoSymbol-1841416](pseudoSymbol-1841416)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1643798-os_log_create)*