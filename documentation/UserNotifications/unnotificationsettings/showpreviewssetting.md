# showPreviewsSetting

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

The setting that indicates whether the app shows a preview of the notification’s content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var showPreviewsSetting: UNShowPreviewsSetting { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) UNShowPreviewsSetting showPreviewsSetting;
```

*macOS*

```objc
@property (atomic, readonly) UNShowPreviewsSetting showPreviewsSetting;
```

## See Also

### Getting Interface Settings
- [var alertStyle: UNAlertStyle](./alertstyle.md)
  The type of alert that the app may display when the device is unlocked.
- [enum UNAlertStyle](../unalertstyle.md)
  Constants indicating the presentation styles for alerts.
- [enum UNShowPreviewsSetting](../unshowpreviewssetting.md)
  Constants indicating the style previewing a notification’s content.
- [var providesAppNotificationSettings: Bool](./providesappnotificationsettings.md)
  A Boolean value indicating the system displays a button for in-app notification settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationsettings/showpreviewssetting)*