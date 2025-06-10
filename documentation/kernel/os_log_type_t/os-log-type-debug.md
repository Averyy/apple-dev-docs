# OS_LOG_TYPE_DEBUG

**Framework**: Kernel  
**Kind**: econst

Debug-level messages are only captured in memory when debug logging is enabled through a configuration change. They’re purged in accordance with the configuration’s persistence setting. Messages logged at this level contain information that may be useful during development or while troubleshooting a specific problem. Debug logging is intended for use in a development environment and not in shipping software. Logging a message of this type is equivalent to calling the `os_log_debug` function.

**Availability**:
- macOS 10.12+

## Declaration

```swift
OS_LOG_TYPE_DEBUG
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/os_log_type_t/os_log_type_debug)*