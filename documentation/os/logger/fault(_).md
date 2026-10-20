# fault(_:)

**Framework**: os  
**Kind**: method  
**Role**: Instance Method

Writes a message to the log about a bug that occurs when your app executes.

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
func fault(_ message: OSLogMessage)
```

#### Discussion

> ❗ **Important**:  Don’t create an instance of [`OSLogMessage`](../oslogmessage.md). Instead, provide an interpolated string as the `message` parameter and the system converts it automatically.

Use this method to write messages with the [`fault`](../oslogtype/fault.md) log level to both the in-memory and on-disk log stores.

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
- [func info(OSLogMessage)](./info%28_%29.md)
  Writes an informative message to the log.
- [func error(OSLogMessage)](./error%28_%29.md)
  Writes information about an error to the log.
- [func warning(OSLogMessage)](./warning%28_%29.md)
  Writes information about a warning to the log.
- [func critical(OSLogMessage)](./critical%28_%29.md)
  Writes a message to the log about a critical event in your app’s execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/logger/fault(_:))*