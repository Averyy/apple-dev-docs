# UNShowPreviewsSetting

**Framework**: User Notifications  
**Kind**: enum

Constants indicating the style previewing a notification’s content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
enum UNShowPreviewsSetting
```

## Topics

### Preview Styes
- [UNShowPreviewsSetting.always](unshowpreviewssetting/always.md)
  The notification’s content is always shown, even when the device is locked.
- [UNShowPreviewsSetting.whenAuthenticated](unshowpreviewssetting/whenauthenticated.md)
  The notification’s content is shown only when the device is unlocked.
- [UNShowPreviewsSetting.never](unshowpreviewssetting/never.md)
  The notification’s content is never shown, even when the device is unlocked
### Initializers
- [init?(rawValue: Int)](unshowpreviewssetting/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var alertStyle: UNAlertStyle](unnotificationsettings/alertstyle.md)
  The type of alert that the app may display when the device is unlocked.
- [enum UNAlertStyle](unalertstyle.md)
  Constants indicating the presentation styles for alerts.
- [var showPreviewsSetting: UNShowPreviewsSetting](unnotificationsettings/showpreviewssetting.md)
  The setting that indicates whether the app shows a preview of the notification’s content.
- [var providesAppNotificationSettings: Bool](unnotificationsettings/providesappnotificationsettings.md)
  A Boolean value indicating the system displays a button for in-app notification settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unshowpreviewssetting)*