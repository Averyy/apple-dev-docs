# os_log(_:dso:log:type:_:)

**Framework**: os  
**Kind**: func  
**Role**: Function

Sends a message to the logging system, optionally specifying a custom log object, log level, and any message format arguments.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS
- watchOS 3.0+

> **Deprecated**: Use [`log(level:_:)`](./logger/log%28level,_%29.md) instead.

## Declaration

```swift
func os_log(_ message: StaticString, dso: UnsafeRawPointer? = #dsohandle, log: OSLog = .default, type: OSLogType = .default, _ args: any CVarArg...)
```

## Discussion

Call this function to capture information about things that might result in a failure. For more information about format strings, see [String Format Specifiers](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265).

## Parameters

- `message`: A constant string or format string that produces a human-readable log message.
- `log`: A custom log object. If unspecified, system uses the shared default log.
- `type`: The log level. If unspecified, the system uses the default log level.
- `args`: If `message` is a constant string, do not specify arguments.

  If `message` is a format string, pass the expected number of arguments in the order that they appear in the string.

## See Also

### Log Messages
- [func os_log(OSLogMessage)](./os_log%28_%29.md)
  Adds a new log message to the default subsystem.
- [func os_log(OSLogType, log: OSLog, OSLogMessage)](./os_log%28_,log,_%29.md)
  Adds a new log message using an optional log object and log level.
- [func os_log(OSLogType, dso: UnsafeRawPointer, log: OSLog, StaticString, any CVarArg...)](./os_log%28_,dso,log,_,_%29.md)
  Sends a message to the logging system, optionally specifying a custom log object, log level, and any message-format arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_log(_:dso:log:type:_:))*