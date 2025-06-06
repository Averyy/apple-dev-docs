# threadIdentifier

**Framework**: Usernotifications  
**Kind**: property

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
var threadIdentifier: String { get set }
```

## Mentions

- [Generating a remote notification](generating-a-remote-notification.md)

#### Discussion

You may specify any value for the string, but assign the same thread identifier string to all notifications that you want to group together visually.

## See Also

- [var categoryIdentifier: String](unmutablenotificationcontent/categoryidentifier.md)
  The identifier of the notification’s category.
- [var summaryArgument: String](unmutablenotificationcontent/summaryargument.md)
  The text the system adds to the notification summary to provide additional context.
- [var summaryArgumentCount: Int](unmutablenotificationcontent/summaryargumentcount.md)
  The number the system adds to the notification summary when the notification represents multiple items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/threadidentifier)*