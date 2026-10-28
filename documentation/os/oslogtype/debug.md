# debug

**Framework**: os  
**Kind**: property  
**Role**: Type Property

The debug log level.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS
- watchOS 3.0+

## Declaration

```swift
static let debug: OSLogType
```

## Discussion

Logging a message of this type is equivalent to calling the [`os_log_debug`](../os_log_debug.md) function. Use this level to capture information that may be useful during development or while troubleshooting a specific problem.

The system only captures debug-level messages in memory when you enable debug logging through a configuration change, and purges them in accordance with the configuration’s persistence setting.

## See Also

### Getting Log Types
- [static let info: OSLogType](./info.md)
  The informative log level.
- [static let `default`: OSLogType](./default.md)
  The default log level.
- [static let error: OSLogType](./error.md)
  The error log level.
- [static let fault: OSLogType](./fault.md)
  The fault log level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogtype/debug)*