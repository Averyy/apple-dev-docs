# log(level:_:)

**Framework**: os  
**Kind**: method

Writes a message to the log using the specified log type.

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
func log(level: OSLogType, _ message: OSLogMessage)
```

#### Discussion

> ❗ **Important**:  Don’t create an instance of [`OSLogMessage`](oslogmessage.md). Instead, provide an interpolated string as the `message` parameter and the system converts it automatically.

 Don’t create an instance of [`OSLogMessage`](oslogmessage.md). Instead, provide an interpolated string as the `message` parameter and the system converts it automatically.

## Parameters

- `level`: The message’s log level, which determines the severity of the message and whether the system persists it to disk. For possible values, see  .
- `message`: The interpolated string that the logger writes to the log. Each of the message’s interpolations can specify individual formatting and privacy options. For more information, see  .

## See Also

- [func log(OSLogMessage)](logger/log(_:).md)
  Writes a message to the log using the default log type.
- [struct OSLogType](oslogtype.md)
  The various log levels that the unified logging system provides.
- [struct OSLogMessage](oslogmessage.md)
  An object that represents a log message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/logger/log(level:_:))*