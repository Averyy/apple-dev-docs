# fault

**Framework**: os  
**Kind**: property  
**Role**: Type Property

The fault log level.

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
static let fault: OSLogType
```

## Discussion

Logging a message at this level is equivalent to calling the [`os_log_fault`](../os_log_fault.md) function. Use this level only to capture system-level or multiprocess information when reporting system errors.

The system always writes fault-level messages to the data store. They remain in the store until its size exceeds its storage quota, at which point, the system purges the oldest messages in the store to free up space. If an activity object exists, logging at this level captures information for the entire process chain.

## See Also

### Getting Log Types
- [static let debug: OSLogType](./debug.md)
  The debug log level.
- [static let info: OSLogType](./info.md)
  The informative log level.
- [static let `default`: OSLogType](./default.md)
  The default log level.
- [static let error: OSLogType](./error.md)
  The error log level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogtype/fault)*