# default

**Framework**: os  
**Kind**: property

The default log level.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst ?+
- macOS 10.12+
- tvOS 10.0+
- visionOS ?+
- watchOS 3.0+

## Declaration

```swift
static let `default`: OSLogType
```

#### Discussion

Logging a message of this type is equivalent to calling the [`os_log`](os_log.md) function. Use this level to capture information about things that might result in a failure.

The system stores default-level messages in memory buffers and, without a configuration change, compresses the messages and writes them to the data store as those buffers fill up. They remain in the data store until the store’s size exceeds its storage quota, at which point, the system purges the oldest messages in the store to free up space.

## See Also

- [static let debug: OSLogType](oslogtype/debug.md)
  The debug log level.
- [static let info: OSLogType](oslogtype/info.md)
  The informative log level.
- [static let error: OSLogType](oslogtype/error.md)
  The error log level.
- [static let fault: OSLogType](oslogtype/fault.md)
  The fault log level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogtype/default)*