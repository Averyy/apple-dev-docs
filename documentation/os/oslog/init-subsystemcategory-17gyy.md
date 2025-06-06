# init(subsystem:category:)

**Framework**: os  
**Kind**: init

Creates a log using the specified subsystem and category.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst ?+
- macOS 10.12+
- tvOS 10.0+
- visionOS ?+
- watchOS 3.0+

## Declaration

```swift
convenience init(subsystem: String, category: String)
```

#### Return Value

 A custom log object that you can pass to other logging functions to perform logging and to determine whether a specific level of logging is in an enabled state.

## Parameters

- `subsystem`: An identifier string, in reverse DNS notation, that represents the app subsystem that’s logging information, such as  . The logging system uses this information to categorize and filter related log messages, and to group related logging settings.
- `category`: A category within the specified subsystem. The system uses this value to categorize and filter related log messages, and to group related logging settings within the subsystem. A category’s logging settings override those of the containing subsystem.

## See Also

- [convenience init(subsystem: String, category: OSLog.Category)](oslog/init(subsystem:category:)-72ghw.md)
  Creates a log using the specified subsystem and system-defined category.
- [struct Category](oslog/category.md)
  System-defined categories that identify well-known parts of your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/oslog/init(subsystem:category:)-17gyy)*