# providesAppNotificationSettings

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating the system displays a button for in-app notification settings.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var providesAppNotificationSettings: Bool { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) BOOL providesAppNotificationSettings;
```

*macOS*

```objc
@property (atomic, readonly) BOOL providesAppNotificationSettings;
```

## See Also

### Getting Interface Settings
- [var alertStyle: UNAlertStyle](./alertstyle.md)
  The type of alert that the app may display when the device is unlocked.
- [enum UNAlertStyle](../unalertstyle.md)
  Constants indicating the presentation styles for alerts.
- [var showPreviewsSetting: UNShowPreviewsSetting](./showpreviewssetting.md)
  The setting that indicates whether the app shows a preview of the notification’s content.
- [enum UNShowPreviewsSetting](../unshowpreviewssetting.md)
  Constants indicating the style previewing a notification’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationsettings/providesappnotificationsettings)*