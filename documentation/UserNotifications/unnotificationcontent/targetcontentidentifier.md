# targetContentIdentifier

**Framework**: Usernotifications  
**Kind**: property

The value your app uses to determine which scene to display to handle the notification.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var targetContentIdentifier: String? { get }
```

## Mentions

- [Generating a remote notification](generating-a-remote-notification.md)

#### Discussion

Use this value to determine the content to show in your app when the user taps the notification.

## See Also

- [var launchImageName: String](unnotificationcontent/launchimagename.md)
  The name of the image or storyboard to use when your app launches because of the notification.
- [var badge: NSNumber?](unnotificationcontent/badge.md)
  The number that your app’s icon displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcontent/targetcontentidentifier)*