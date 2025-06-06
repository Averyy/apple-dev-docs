# OSLogType

**Framework**: os  
**Kind**: struct

The various log levels that the unified logging system provides.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct OSLogType
```

#### Overview

A log level controls how and when the system writes a message to the unified logging system. To write a message with a specific log level, create a [`Logger`](logger.md) and call its [`log(level:_:)`](logger/log(level:_:).md) method. Alternatively, call the method that corresponds to the desired log level, such as [`debug(_:)`](logger/debug(_:).md) or [`fault(_:)`](logger/fault(_:).md).

## Topics

### Getting Log Types
- [static let debug: OSLogType](oslogtype/debug.md)
  The debug log level.
- [static let info: OSLogType](oslogtype/info.md)
  The informative log level.
- [static let `default`: OSLogType](oslogtype/default.md)
  The default log level.
- [static let error: OSLogType](oslogtype/error.md)
  The error log level.
- [static let fault: OSLogType](oslogtype/fault.md)
  The fault log level.
### Creating a Log Type
- [init(UInt8)](oslogtype/init(_:).md)
  Creates a log type from the specified value.
- [init(rawValue: UInt8)](oslogtype/init(rawvalue:).md)
  Creates a log type from the specified raw value.
### Getting the Raw Value
- [var rawValue: UInt8](oslogtype/rawvalue.md)
  The log type’s raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct Logger](logger.md)
  An object for writing interpolated string messages to the unified logging system.
- [Message Argument Formatters](message-argument-formatters.md)
  Manage the privacy and presentation of the message’s interpolated values using type-aware formatters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogtype)*