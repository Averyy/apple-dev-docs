# error(_:)

**Framework**: os  
**Kind**: method

Writes information about an error to the log.

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
func error(_ message: OSLogMessage)
```

#### Discussion

> ❗ **Important**:  Don’t create an instance of [`OSLogMessage`](oslogmessage.md). Instead, provide an interpolated string as the `message` parameter and the system converts it automatically.

Use this method to write messages with the [`error`](oslogtype/error.md) log level to both the in-memory and on-disk log stores.

## Parameters

- `message`: The interpolated string that the logger writes to the log. Each of the message’s interpolations can specify individual formatting and privacy options. For more information, see  .

## See Also

- [func notice(OSLogMessage)](logger/notice(_:).md)
  Writes a message to the log using the default log type.
- [func debug(OSLogMessage)](logger/debug(_:).md)
  Writes a debug message to the log.
- [func trace(OSLogMessage)](logger/trace(_:).md)
  Writes a trace message to the log.
- [func info(OSLogMessage)](logger/info(_:).md)
  Writes an informative message to the log.
- [func warning(OSLogMessage)](logger/warning(_:).md)
  Writes information about a warning to the log.
- [func fault(OSLogMessage)](logger/fault(_:).md)
  Writes a message to the log about a bug that occurs when your app executes.
- [func critical(OSLogMessage)](logger/critical(_:).md)
  Writes a message to the log about a critical event in your app’s execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/logger/error(_:))*