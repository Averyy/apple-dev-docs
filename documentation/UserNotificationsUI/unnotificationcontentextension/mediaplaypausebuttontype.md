# mediaPlayPauseButtonType

**Framework**: User Notifications UI  
**Kind**: property

The type of media button type to display.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var mediaPlayPauseButtonType: UNNotificationContentExtensionMediaPlayPauseButtonType { get }
```

## Mentions

- [Customizing the Appearance of Notifications](customizing-the-appearance-of-notifications.md)

#### Discussion

Implement this property when you want the system to display a media playback button in your notification interface. Return an appropriate constant indicating the type of button you want. If you don’t implement this property, the system behaves as if you set the value to [`UNNotificationContentExtensionMediaPlayPauseButtonType.none`](unnotificationcontentextensionmediaplaypausebuttontype/none.md).

## See Also

- [enum UNNotificationContentExtensionMediaPlayPauseButtonType](unnotificationcontentextensionmediaplaypausebuttontype.md)
  Constants indicating the type of media button to display.
- [var mediaPlayPauseButtonFrame: CGRect](unnotificationcontentextension/mediaplaypausebuttonframe.md)
  The frame rectangle to use for displaying a media playback button.
- [var mediaPlayPauseButtonTintColor: UIColor](unnotificationcontentextension/mediaplaypausebuttontintcolor.md)
  The tint color for the media playback button.
- [func mediaPlay()](unnotificationcontentextension/mediaplay.md)
  Tells you to begin playback of your media content.
- [func mediaPause()](unnotificationcontentextension/mediapause.md)
  Tells you to pause playback of your media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextension/mediaplaypausebuttontype)*