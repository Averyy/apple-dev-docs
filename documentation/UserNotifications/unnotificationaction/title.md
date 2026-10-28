# title

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The localized string to use as the title of the action.

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

## Discussion

The system displays this string as the title of the button that the user taps or selects in the notification interface.

## See Also

### Getting Information
- [var identifier: String](./identifier.md)
  The unique string that your app uses to identify the action.
- [var icon: UNNotificationActionIcon?](./icon.md)
  The icon associated with the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationaction/title)*