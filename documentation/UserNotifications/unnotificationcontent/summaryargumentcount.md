# summaryArgumentCount

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The number the system adds to the notification summary when the notification represents multiple items.

**Availability**:
- iOS 12.0+ - Deprecated in 15.0
- iPadOS 12.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.14+
- tvOS 12.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 5.0+ - Deprecated in 8.0

> **Deprecated**: summaryArgumentCount is ignored

## Declaration

```swift
var summaryArgumentCount: Int { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) NSUInteger summaryArgumentCount;
```

*macOS*

```objc
@property (atomic, assign, readonly) NSUInteger summaryArgumentCount;
```

## See Also

### Retrieving group information
- [var threadIdentifier: String](./threadidentifier.md)
  The identifier that groups related notifications.
- [var categoryIdentifier: String](./categoryidentifier.md)
  The identifier of the notification’s category.
- [var summaryArgument: String](./summaryargument.md)
  The text the system adds to the notification summary to provide additional context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcontent/summaryargumentcount)*