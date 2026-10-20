# summaryArgument

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The text the system adds to the notification summary to provide additional context.

**Availability**:
- iOS 12.0+ - Deprecated in 15.0
- iPadOS 12.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.14+
- tvOS 12.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 5.0+ - Deprecated in 8.0

> **Deprecated**: summaryArgument is ignored

## Declaration

```swift
var summaryArgument: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * summaryArgument;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * summaryArgument;
```

## See Also

### Retrieving group information
- [var threadIdentifier: String](./threadidentifier.md)
  The identifier that groups related notifications.
- [var categoryIdentifier: String](./categoryidentifier.md)
  The identifier of the notification’s category.
- [var summaryArgumentCount: Int](./summaryargumentcount.md)
  The number the system adds to the notification summary when the notification represents multiple items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcontent/summaryargument)*