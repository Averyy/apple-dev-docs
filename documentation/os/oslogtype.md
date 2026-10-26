# OSLogType

**Framework**: os  
**Kind**: struct  
**Role**: Structure

The various log levels that the unified logging system provides.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct OSLogType
```

```c
typedef enum { ... } os_log_type_t;
```

#### Overview

A log level controls how and when the system writes a message to the unified logging system. To write a message with a specific log level, create a [`Logger`](./logger.md) and call its [`log(level:_:)`](./logger/log%28level,_%29.md) method. Alternatively, call the method that corresponds to the desired log level, such as [`debug(_:)`](./logger/debug%28_%29.md) or [`fault(_:)`](./logger/fault%28_%29.md).

## Topics

### Getting Log Types
- [static let debug: OSLogType](./oslogtype/debug.md)
  The debug log level.
- [static let info: OSLogType](./oslogtype/info.md)
  The informative log level.
- [static let `default`: OSLogType](./oslogtype/default.md)
  The default log level.
- [static let error: OSLogType](./oslogtype/error.md)
  The error log level.
- [static let fault: OSLogType](./oslogtype/fault.md)
  The fault log level.
### Creating a Log Type
- [init(UInt8)](./oslogtype/init%28_%29.md)
  Creates a log type from the specified value.
- [init(rawValue: UInt8)](./oslogtype/init%28rawvalue%29.md)
  Creates a log type from the specified raw value.
### Getting the Raw Value
- [var rawValue: UInt8](./oslogtype/rawvalue.md)
  The log type’s raw value.
### Enumeration Cases
- [OS_LOG_TYPE_DEBUG](./os_log_type_t/os_log_type_debug.md)
  The debug log level.
- [OS_LOG_TYPE_DEFAULT](./os_log_type_t/os_log_type_default.md)
  The default log level.
- [OS_LOG_TYPE_ERROR](./os_log_type_t/os_log_type_error.md)
  The error log level.
- [OS_LOG_TYPE_FAULT](./os_log_type_t/os_log_type_fault.md)
  The fault log level.
- [OS_LOG_TYPE_INFO](./os_log_type_t/os_log_type_info.md)
  The informational log level.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Log Messages
- [struct Logger](./logger.md)
  An object for writing interpolated string messages to the unified logging system.
- [Message Argument Formatters](./message-argument-formatters.md)
  Manage the privacy and presentation of the message’s interpolated values using type-aware formatters.
- [Legacy Logging Symbols](./legacy-logging-symbols.md)
  Migrate your code away from using these legacy symbols.
- [os_log_t](./os-log-t.md)
  A log object that you pass to logging functions to send messages to that log.
- [os_log_with_type](./os_log_with_type.md)
  Sends a message at a specific logging level, such as default, info, debug, error, or fault, to the logging system.
- [os_log](./os_log.md)
  Sends a default-level message to the logging system.
- [os_log_info](./os_log_info.md)
  Sends an info-level message to the logging system.
- [os_log_debug](./os_log_debug.md)
  Sends a debug-level message to the logging system.
- [os_log_error](./os_log_error.md)
  Sends an error-level message to the logging system.
- [os_log_fault](./os_log_fault.md)
  Sends a fault-level message to the logging system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslogtype)*