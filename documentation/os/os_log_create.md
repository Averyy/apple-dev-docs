# os_log_create

**Framework**: os  
**Kind**: func  
**Role**: Function

Creates a custom log object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```c
extern os_log_tos_log_create(const char *subsystem, const char *category);
```

## Return Value

A value of type `os_log_t`, which can be passed to other logging functions to perform logging and to determine whether a specific level of logging is enabled. A value is always returned and should be released when no longer needed.

## Discussion

Typically, use the [`OS_LOG_DEFAULT`](./os_log_default.md) constant to perform logging using the system’s behavior. Create a custom log object only when you want to tag messages with a specific subsystem and category for the purpose of filtering, or to customize the logging behavior of your subsystem with a profile for debugging purposes. You only need to call this function once to initialize a custom log object. It doesn’t need to be called again when changing logging settings. The system automatically detects changes to logging settings.

## Parameters

- `subsystem`: An identifier string, in reverse DNS notation, that represents the subsystem that’s performing logging, for example, `com.your_company.your_subsystem_name`. The subsystem is used for categorization and filtering of related log messages, as well as for grouping related logging settings.
- `category`: A category within the specified subsystem. The system uses the category to categorize and filter related log messages, as well as to group related logging settings within the subsystem’s settings. A category’s logging settings override those of the parent subsystem.

## See Also

### Related Documentation
- [func isEnabled(type: OSLogType) -> Bool](./oslog/isenabled%28type%29.md)
  Returns a Boolean value that indicates whether the log can write messages with the specified log type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_log_create)*