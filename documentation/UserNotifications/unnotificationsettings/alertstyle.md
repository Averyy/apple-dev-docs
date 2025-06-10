# alertStyle

**Framework**: User Notifications  
**Kind**: property

The type of alert that the app may display when the device is unlocked.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var alertStyle: UNAlertStyle { get }
```

#### Discussion

When alerts are authorized, this property specifies the presentation style for alerts when the device is unlocked. The user may choose to display alerts as automatically disappearing banners or as modal windows that require explicit dismissal. The user may also choose not to display alerts at all.

## See Also

- [enum UNAlertStyle](unalertstyle.md)
  Constants indicating the presentation styles for alerts.
- [var showPreviewsSetting: UNShowPreviewsSetting](unnotificationsettings/showpreviewssetting.md)
  The setting that indicates whether the app shows a preview of the notification’s content.
- [enum UNShowPreviewsSetting](unshowpreviewssetting.md)
  Constants indicating the style previewing a notification’s content.
- [var providesAppNotificationSettings: Bool](unnotificationsettings/providesappnotificationsettings.md)
  A Boolean value indicating the system displays a button for in-app notification settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationsettings/alertstyle)*