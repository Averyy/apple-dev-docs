# UNAlertStyle

**Framework**: User Notifications  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the presentation styles for alerts.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
enum UNAlertStyle
```

```c
enum UNAlertStyle : NSInteger;
```

## Topics

### Presentation Styles
- [UNAlertStyle.none](./unalertstyle/none.md)
  No alert.
- [UNAlertStyle.banner](./unalertstyle/banner.md)
  Banner alerts.
- [UNAlertStyle.alert](./unalertstyle/alert.md)
  Modal alerts.
### Initializers
- [init?(rawValue: Int)](./unalertstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting Interface Settings
- [var alertStyle: UNAlertStyle](./unnotificationsettings/alertstyle.md)
  The type of alert that the app may display when the device is unlocked.
- [var showPreviewsSetting: UNShowPreviewsSetting](./unnotificationsettings/showpreviewssetting.md)
  The setting that indicates whether the app shows a preview of the notification’s content.
- [enum UNShowPreviewsSetting](./unshowpreviewssetting.md)
  Constants indicating the style previewing a notification’s content.
- [var providesAppNotificationSettings: Bool](./unnotificationsettings/providesappnotificationsettings.md)
  A Boolean value indicating the system displays a button for in-app notification settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unalertstyle)*