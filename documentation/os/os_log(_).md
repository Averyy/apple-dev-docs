# os_log(_:)

**Framework**: os  
**Kind**: func  
**Role**: Function

Adds a new log message to the default subsystem.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use [`log(_:)`](./logger/log%28_%29.md) instead.

## Declaration

```swift
func os_log(_ message: OSLogMessage)
```

## Parameters

- `message`: A string containing the message you want to log. Always specify this parameter as a string; this function converts it to an [`OSLogMessage`](./oslogmessage.md) object. You may include interpolated values in the string.

## See Also

### Log Messages
- [func os_log(OSLogType, log: OSLog, OSLogMessage)](./os_log%28_,log,_%29.md)
  Adds a new log message using an optional log object and log level.
- [func os_log(OSLogType, dso: UnsafeRawPointer, log: OSLog, StaticString, any CVarArg...)](./os_log%28_,dso,log,_,_%29.md)
  Sends a message to the logging system, optionally specifying a custom log object, log level, and any message-format arguments.
- [func os_log(StaticString, dso: UnsafeRawPointer?, log: OSLog, type: OSLogType, any CVarArg...)](./os_log%28_,dso,log,type,_%29.md)
  Sends a message to the logging system, optionally specifying a custom log object, log level, and any message format arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_log(_:))*