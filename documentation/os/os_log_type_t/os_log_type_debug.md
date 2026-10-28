# OS_LOG_TYPE_DEBUG

**Framework**: os  
**Kind**: case  
**Role**: Enumeration Case

The debug log level.

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
OS_LOG_TYPE_DEBUG
```

## Discussion

Logging a message of this type is equivalent to calling the [`os_log_debug`](../os_log_debug.md) function. Use this level to capture information that may be useful during development or while troubleshooting a specific problem.

Debug-level messages are only captured in memory when debug logging is enabled through a configuration change. They’re purged in accordance with the configuration’s persistence setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_log_type_t/os_log_type_debug)*