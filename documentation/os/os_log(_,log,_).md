# os_log(_:log:_:)

**Framework**: os  
**Kind**: func  
**Role**: Function

Adds a new log message using an optional log object and log level.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use [`log(level:_:)`](./logger/log%28level,_%29.md) instead.

## Declaration

```swift
func os_log(_ logLevel: OSLogType = .default, log logObject: OSLog = .default, _ message: OSLogMessage)
```

#### Discussion

Use this method to capture information at any log level.

## Parameters

- `logLevel`: The log level to assign to the message. For more information about log levels, see [`OSLogType`](./oslogtype.md).
- `logObject`: The log object that receives the message. The message inherits the same subsystem and category as the log object.
- `message`: A string containing the message you want to log. Always specify this parameter as a string; this function converts it to an [`OSLogMessage`](./oslogmessage.md) object. The string may contain interpolated values.

## See Also

### Log Messages
- [func os_log(OSLogMessage)](./os_log%28_%29.md)
  Adds a new log message to the default subsystem.
- [func os_log(OSLogType, dso: UnsafeRawPointer, log: OSLog, StaticString, any CVarArg...)](./os_log%28_,dso,log,_,_%29.md)
  Sends a message to the logging system, optionally specifying a custom log object, log level, and any message-format arguments.
- [func os_log(StaticString, dso: UnsafeRawPointer?, log: OSLog, type: OSLogType, any CVarArg...)](./os_log%28_,dso,log,type,_%29.md)
  Sends a message to the logging system, optionally specifying a custom log object, log level, and any message format arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_log(_:log:_:))*