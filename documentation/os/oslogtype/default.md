# default

**Framework**: os  
**Kind**: property  
**Role**: Type Property

The default log level.

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
static let `default`: OSLogType
```

#### Discussion

Logging a message of this type is equivalent to calling the [`os_log`](../os_log.md) function. Use this level to capture information about things that might result in a failure.

The system stores default-level messages in memory buffers and, without a configuration change, compresses the messages and writes them to the data store as those buffers fill up. They remain in the data store until the store’s size exceeds its storage quota, at which point, the system purges the oldest messages in the store to free up space.

## See Also

### Getting Log Types
- [static let debug: OSLogType](./debug.md)
  The debug log level.
- [static let info: OSLogType](./info.md)
  The informative log level.
- [static let error: OSLogType](./error.md)
  The error log level.
- [static let fault: OSLogType](./fault.md)
  The fault log level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogtype/default)*