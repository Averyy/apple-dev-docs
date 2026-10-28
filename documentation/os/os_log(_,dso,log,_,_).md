# os_log(_:dso:log:_:_:)

**Framework**: os  
**Kind**: func  
**Role**: Function

Sends a message to the logging system, optionally specifying a custom log object, log level, and any message-format arguments.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS
- watchOS 5.0+

> **Deprecated**: Use [`log(level:_:)`](./logger/log%28level,_%29.md) instead.

## Declaration

```swift
func os_log(_ type: OSLogType, dso: UnsafeRawPointer = #dsohandle, log: OSLog = .default, _ message: StaticString, _ args: any CVarArg...)
```

## Discussion

Call this function to capture information about things that might result in a failure. For more information about format strings, see `Formatting Log Messages`.

## Parameters

- `type`: The log level to assign to the message. For more information about log levels, see [`OSLogType`](./oslogtype.md).
- `log`: A custom log object. If unspecified, system uses the shared default log.
- `message`: A constant string or format string that produces a human-readable log message.
- `args`: If `message` is a constant string, do not specify arguments.

  If `message` is a format string, pass the expected number of arguments in the order that they appear in the string.

## See Also

### Log Messages
- [func os_log(OSLogMessage)](./os_log%28_%29.md)
  Adds a new log message to the default subsystem.
- [func os_log(OSLogType, log: OSLog, OSLogMessage)](./os_log%28_,log,_%29.md)
  Adds a new log message using an optional log object and log level.
- [func os_log(StaticString, dso: UnsafeRawPointer?, log: OSLog, type: OSLogType, any CVarArg...)](./os_log%28_,dso,log,type,_%29.md)
  Sends a message to the logging system, optionally specifying a custom log object, log level, and any message format arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_log(_:dso:log:_:_:))*