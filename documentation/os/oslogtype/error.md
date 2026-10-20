# error

**Framework**: os  
**Kind**: property  
**Role**: Type Property

The error log level.

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
static let error: OSLogType
```

#### Discussion

Logging a message of this type is equivalent to calling the [`os_log_error`](../os_log_error.md) function. Use this log level to report process-level errors.

The system always writes error-level messages to the data store. They remain in the store until its size exceeds its storage quota, at which point, the system purges the oldest messages in the store to free up space. If an activity object exists, logging at this level captures information for the entire process chain.

## See Also

### Getting Log Types
- [static let debug: OSLogType](./debug.md)
  The debug log level.
- [static let info: OSLogType](./info.md)
  The informative log level.
- [static let `default`: OSLogType](./default.md)
  The default log level.
- [static let fault: OSLogType](./fault.md)
  The fault log level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogtype/error)*