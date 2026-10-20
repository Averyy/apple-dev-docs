# allowInCarPlay

**Framework**: User Notifications  
**Kind**: property  
**Role**: Type Property

Allow CarPlay to display notifications of this type.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static var allowInCarPlay: UNNotificationCategoryOptions { get }
```

```c
UNNotificationCategoryOptionAllowInCarPlay
```

#### Discussion

Apps must be approved for CarPlay overall and then you must enable CarPlay for the notification types you want displayed. If a category doesn’t explicitly contain this option, notifications of that type aren’t displayed in a CarPlay environment.

## See Also

### Customizing a category
- [static var allowAnnouncement: UNNotificationCategoryOptions](./allowannouncement.md)
  An option that grants Siri permission to read incoming messages out loud when the user has a compatible audio output device connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcategoryoptions/allowincarplay)*