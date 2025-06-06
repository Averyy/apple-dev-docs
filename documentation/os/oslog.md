# OSLog

**Framework**: os  
**Kind**: class

A container of related log messages.

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
class OSLog
```

## Mentions

- [Generating Log Messages from Your Code](generating-log-messages-from-your-code.md)

#### Overview

A log categorizes the messages you write and makes it easy to sort and filter them. Each log contains a subsystem and a category, which you define. A subsystem identifies a major functional area of your app, which you specify using reverse DNS notation, such as `com.your_company.your_subsystem_name`. A category segregates specific areas within a subsystem.

## Topics

### Creating a Log
- [convenience init(subsystem: String, category: String)](oslog/init(subsystem:category:)-17gyy.md)
  Creates a log using the specified subsystem and category.
- [convenience init(subsystem: String, category: OSLog.Category)](oslog/init(subsystem:category:)-72ghw.md)
  Creates a log using the specified subsystem and system-defined category.
- [struct Category](oslog/category.md)
  System-defined categories that identify well-known parts of your app.
### Getting the Shared Logs
- [static let `default`: OSLog](oslog/default.md)
  The shared default log.
- [static let disabled: OSLog](oslog/disabled.md)
  The shared disabled log.
### Getting Log Configuration
- [func isEnabled(type: OSLogType) -> Bool](oslog/isenabled(type:).md)
  Returns a Boolean value that indicates whether the log can write messages with the specified log type.
- [var signpostsEnabled: Bool](oslog/signpostsenabled.md)
  A Boolean value that indicates whether a log is able to use signpost logging.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init()](logger/init.md)
  Creates a logger that writes to the default subsystem.
- [init(subsystem: String, category: String)](logger/init(subsystem:category:).md)
  Creates a logger using the specified subsystem and category.
- [init(OSLog)](logger/init(_:).md)
  Creates a logger that writes to the specified log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslog)*