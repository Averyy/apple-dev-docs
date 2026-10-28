# info(_:)

**Framework**: os  
**Kind**: method  
**Role**: Instance Method

Writes an informative message to the log.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
func info(_ message: OSLogMessage)
```

## Discussion

> ❗ **Important**:  Don’t create an instance of [`OSLogMessage`](../oslogmessage.md). Instead, provide an interpolated string as the `message` parameter and the system converts it automatically.

Use this method to write messages with the [`info`](../oslogtype/info.md) log level to the in-memory log store only. If you use the `log` command line tool to collect your logs, the method also writes messages to the on-disk log store.

## Parameters

- `message`: The interpolated string that the logger writes to the log. Each of the message’s interpolations can specify individual formatting and privacy options. For more information, see [Message Argument Formatters](../message-argument-formatters.md).

## See Also

### Logging a Scoped Message
- [func notice(OSLogMessage)](./notice%28_%29.md)
  Writes a message to the log using the default log type.
- [func debug(OSLogMessage)](./debug%28_%29.md)
  Writes a debug message to the log.
- [func trace(OSLogMessage)](./trace%28_%29.md)
  Writes a trace message to the log.
- [func error(OSLogMessage)](./error%28_%29.md)
  Writes information about an error to the log.
- [func warning(OSLogMessage)](./warning%28_%29.md)
  Writes information about a warning to the log.
- [func fault(OSLogMessage)](./fault%28_%29.md)
  Writes a message to the log about a bug that occurs when your app executes.
- [func critical(OSLogMessage)](./critical%28_%29.md)
  Writes a message to the log about a critical event in your app’s execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/logger/info(_:))*