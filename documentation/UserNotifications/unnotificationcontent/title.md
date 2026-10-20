# title

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The localized text that provides the notification’s primary description.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var title: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * title;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * title;
```

#### Discussion

When a title is present, the system attempts to display a notification alert. If your app isn’t authorized to display alert-based notifications, the system ignores this property.

Title strings should be short, usually only a couple of words describing the reason for the notification. In watchOS, the system displays the title string as part of the short look notification interface, which has limited space.

## See Also

### Accessing the primary content
- [var subtitle: String](./subtitle.md)
  The localized text that provides the notification’s secondary description.
- [var body: String](./body.md)
  The localized text that provides the notification’s main content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcontent/title)*