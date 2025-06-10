# launchImageName

**Framework**: User Notifications  
**Kind**: property

The name of the image or storyboard to use when your app launches because of the notification.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var launchImageName: String { get set }
```

#### Discussion

If you specify a value for this property, the system displays the specified image or storyboard when the system launches your app. The string in this property must match the name of an image file or storyboard in your app’s bundle. Specify `nil` to use the app’s default launch image. The default value of this property is `nil`.

## See Also

- [var badge: NSNumber?](unmutablenotificationcontent/badge.md)
  The number that your app’s icon displays.
- [var targetContentIdentifier: String?](unmutablenotificationcontent/targetcontentidentifier.md)
  The value your app uses to determine which scene to display to handle the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/launchimagename)*