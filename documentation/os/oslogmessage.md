# OSLogMessage

**Framework**: os  
**Kind**: struct

An object that represents a log message.

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
@frozen
struct OSLogMessage
```

#### Overview

> ❗ **Important**:  You don’t create instances of [`OSLogMessage`](oslogmessage.md) directly. Instead, the system creates them for you when writing messages to the unified logging system using a [`Logger`](logger.md).

## Topics

### Getting the Message Details
- [var bufferSize: Int](oslogmessage/buffersize.md)
  The byte size of the buffer that the logging system receives.
- [let interpolation: OSLogInterpolation](oslogmessage/interpolation.md)
  The log message’s string interpolation.
- [var maxOSLogArgumentCount: UInt8](maxoslogargumentcount.md)
  The maximum number of interpolated expressions that a log message may contain.

## Relationships

### Conforms To
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringInterpolation](../Swift/ExpressibleByStringInterpolation.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)

## See Also

- [func log(OSLogMessage)](logger/log(_:).md)
  Writes a message to the log using the default log type.
- [func log(level: OSLogType, OSLogMessage)](logger/log(level:_:).md)
  Writes a message to the log using the specified log type.
- [struct OSLogType](oslogtype.md)
  The various log levels that the unified logging system provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogmessage)*