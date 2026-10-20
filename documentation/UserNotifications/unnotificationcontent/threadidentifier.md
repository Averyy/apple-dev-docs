# threadIdentifier

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The identifier that groups related notifications.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var threadIdentifier: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * threadIdentifier;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * threadIdentifier;
```

#### Discussion

For remote notifications, the system sets this property to the value of the `thread-id` key in the `aps` dictionary.

## See Also

### Retrieving group information
- [var categoryIdentifier: String](./categoryidentifier.md)
  The identifier of the notification’s category.
- [var summaryArgument: String](./summaryargument.md)
  The text the system adds to the notification summary to provide additional context.
- [var summaryArgumentCount: Int](./summaryargumentcount.md)
  The number the system adds to the notification summary when the notification represents multiple items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcontent/threadidentifier)*