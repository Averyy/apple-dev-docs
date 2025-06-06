# Logger

**Framework**: os  
**Kind**: struct

An object for writing interpolated string messages to the unified logging system.

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
struct Logger
```

## Mentions

- [Generating Log Messages from Your Code](generating-log-messages-from-your-code.md)

#### Overview

Create a [`Logger`](logger.md) structure and use it to log messages about your app’s behavior. When logging a message, you specify the message and any program variables or custom data to help you assess the state of your app. You also choose a log level to indicate the severity of that message. The system records log messages in memory and, in some cases, also writes those messages to an on-disk data store. The log level determines which messages stay in memory and which go to disk.

When you create a [`Logger`](logger.md) structure, assign an optional subsystem and category string to add context to all messages you log. A subsystem corresponds to a large functional area of your app, and a category corresponds to a specific area within a particular subsystem. When diagnosing problems, use those strings to filter out unrelated messages.

To log a message, call the method that represents the appropriate log level for that message. To create the message, use a Swift string. Strings may contain interpolated values, such as signed and unsigned integers, floating-point and double values, Booleans, other strings, Objective-C objects, and types that conform to the [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible) protocol. You can also include metatypes such as `Int.self`.

```swift
let logger = Logger()
let x = 42
logger.info("The answer is \(x)")
```

When you include an interpolated string or custom object in your message, the system redacts the value of that string or object by default. This behavior prevents the system from leaking potentially user-sensitive information in the log files, such as the user’s account information. If the data doesn’t contain sensitive information, change the privacy option of that value when logging the information. In the following code example, the system redacts the account information in the first log message, but displays the user’s selection in the second log message:

```swift
logger.log("Paid with bank account \(accountNumber)")   // Redacted!
logger.log("Ordered smoothie \(smoothieName, privacy: .public)")  // Visible
```

## Topics

### Creating a Logger
- [init()](logger/init.md)
  Creates a logger that writes to the default subsystem.
- [init(subsystem: String, category: String)](logger/init(subsystem:category:).md)
  Creates a logger using the specified subsystem and category.
- [init(OSLog)](logger/init(_:).md)
  Creates a logger that writes to the specified log.
- [class OSLog](oslog.md)
  A container of related log messages.
### Logging a Message
- [func log(OSLogMessage)](logger/log(_:).md)
  Writes a message to the log using the default log type.
- [func log(level: OSLogType, OSLogMessage)](logger/log(level:_:).md)
  Writes a message to the log using the specified log type.
- [struct OSLogType](oslogtype.md)
  The various log levels that the unified logging system provides.
- [struct OSLogMessage](oslogmessage.md)
  An object that represents a log message.
### Logging a Scoped Message
- [func notice(OSLogMessage)](logger/notice(_:).md)
  Writes a message to the log using the default log type.
- [func debug(OSLogMessage)](logger/debug(_:).md)
  Writes a debug message to the log.
- [func trace(OSLogMessage)](logger/trace(_:).md)
  Writes a trace message to the log.
- [func info(OSLogMessage)](logger/info(_:).md)
  Writes an informative message to the log.
- [func error(OSLogMessage)](logger/error(_:).md)
  Writes information about an error to the log.
- [func warning(OSLogMessage)](logger/warning(_:).md)
  Writes information about a warning to the log.
- [func fault(OSLogMessage)](logger/fault(_:).md)
  Writes a message to the log about a bug that occurs when your app executes.
- [func critical(OSLogMessage)](logger/critical(_:).md)
  Writes a message to the log about a critical event in your app’s execution.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [Message Argument Formatters](message-argument-formatters.md)
  Manage the privacy and presentation of the message’s interpolated values using type-aware formatters.
- [struct OSLogType](oslogtype.md)
  The various log levels that the unified logging system provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/logger)*