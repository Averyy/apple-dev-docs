# OSLogMessage

**Framework**: os  
**Kind**: struct  
**Role**: Structure

An object that represents a log message.

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
@frozen
struct OSLogMessage
```

## Overview

> ❗ **Important**:  You don’t create instances of [`OSLogMessage`](./oslogmessage.md) directly. Instead, the system creates them for you when writing messages to the unified logging system using a [`Logger`](./logger.md).

## Topics

### Getting the Message Details
- [var bufferSize: Int](./oslogmessage/buffersize.md)
  The byte size of the buffer that the logging system receives.
- [let interpolation: OSLogInterpolation](./oslogmessage/interpolation.md)
  The log message’s string interpolation.
- [var maxOSLogArgumentCount: UInt8](./maxoslogargumentcount.md)
  The maximum number of interpolated expressions that a log message may contain.

## Relationships

### Conforms To
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringInterpolation](../Swift/expressiblebystringinterpolation.md)
- [ExpressibleByStringLiteral](../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/expressiblebyunicodescalarliteral.md)

## See Also

### Logging a Message
- [func log(OSLogMessage)](./logger/log%28_%29.md)
  Writes a message to the log using the default log type.
- [func log(level: OSLogType, OSLogMessage)](./logger/log%28level,_%29.md)
  Writes a message to the log using the specified log type.
- [struct OSLogType](./oslogtype.md)
  The various log levels that the unified logging system provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogmessage)*