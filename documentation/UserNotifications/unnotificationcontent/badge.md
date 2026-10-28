# badge

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The number that your app’s icon displays.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var badge: NSNumber? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * badge;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * badge;
```

## Discussion

When the number in this property is `0`, the system doesn’t display a badge. When the number is greater than `0`, the system displays the badge with the specified number. When the value in this property is `nil`, the system leaves the current badge unchanged.

## See Also

### Reading app configuration
- [var launchImageName: String](./launchimagename.md)
  The name of the image or storyboard to use when your app launches because of the notification.
- [var targetContentIdentifier: String?](./targetcontentidentifier.md)
  The value your app uses to determine which scene to display to handle the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcontent/badge)*