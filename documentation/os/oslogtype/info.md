# info

**Framework**: os  
**Kind**: property

The informative log level.

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
static let info: OSLogType
```

#### Discussion

Logging a message of this type is equivalent to calling the [`os_log_info`](os_log_info.md) function. Use this level to capture information that may be helpful, but not essential, for troubleshooting errors.

The system stores info-level messages in memory buffers and, without a configuration change, purges the oldest messages as those buffers fill up. However, the system writes the messages to the data store when faults and, optionally, errors occur. Info-level messages remain in the data store until the store’s size exceeds its storage quota, at which point, the system purges the oldest messages in the data store to free up space.

## See Also

- [static let debug: OSLogType](oslogtype/debug.md)
  The debug log level.
- [static let `default`: OSLogType](oslogtype/default.md)
  The default log level.
- [static let error: OSLogType](oslogtype/error.md)
  The error log level.
- [static let fault: OSLogType](oslogtype/fault.md)
  The fault log level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogtype/info)*