# log(_:)

**Framework**: os  
**Kind**: method

Writes a message to the log using the default log type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
func log(_ message: OSLogMessage)
```

#### Discussion

> ❗ **Important**:  Don’t create an instance of [`OSLogMessage`](oslogmessage.md). Instead, provide an interpolated string as the `message` parameter and the system converts it automatically.

 Don’t create an instance of [`OSLogMessage`](oslogmessage.md). Instead, provide an interpolated string as the `message` parameter and the system converts it automatically.

Use this method to write messages using the [`default`](oslogtype/default.md) log level to both the in-memory and on-disk log stores. This method is functionally equivalent to the [`notice(_:)`](logger/notice(_:).md) method.

## Parameters

- `message`: The interpolated string that the logger writes to the log. Each of the message’s interpolations can specify individual formatting and privacy options. For more information, see  .

## See Also

- [func log(level: OSLogType, OSLogMessage)](logger/log(level:_:).md)
  Writes a message to the log using the specified log type.
- [struct OSLogType](oslogtype.md)
  The various log levels that the unified logging system provides.
- [struct OSLogMessage](oslogmessage.md)
  An object that represents a log message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/logger/log(_:))*