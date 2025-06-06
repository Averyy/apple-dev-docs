# init(subsystem:category:)

**Framework**: os  
**Kind**: init

Creates a log using the specified subsystem and system-defined category.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst ?+
- macOS 10.14+
- tvOS 12.0+
- visionOS ?+
- watchOS 5.0+

## Declaration

```swift
convenience init(subsystem: String, category: OSLog.Category)
```

#### Return Value

 A custom log object that you can pass to other logging functions to perform logging and to determine whether a specific level of logging is in an enabled state.

## Parameters

- `subsystem`: An identifier string, in reverse DNS notation, that represents the subsystem that’s performing logging, such as  . The logging system uses this information to categorize and filter related log messages.
- `category`: A system-defined category within the specified subsystem. The system uses this value to categorize and filter related log messages. A category’s logging settings override those of the containing subsystem.

## See Also

- [convenience init(subsystem: String, category: String)](oslog/init(subsystem:category:)-17gyy.md)
  Creates a log using the specified subsystem and category.
- [struct Category](oslog/category.md)
  System-defined categories that identify well-known parts of your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslog/init(subsystem:category:)-72ghw)*