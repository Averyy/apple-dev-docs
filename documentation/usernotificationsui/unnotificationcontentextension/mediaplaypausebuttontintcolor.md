# mediaPlayPauseButtonTintColor

**Framework**: User Notifications UI  
**Kind**: property

The tint color for the media playback button.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
optional var mediaPlayPauseButtonTintColor: UIColor { get }
```

#### Discussion

If you implement the [`mediaPlayPauseButtonFrame`](unnotificationcontentextension/mediaplaypausebuttonframe.md) property, you can also implement this property and use it to specify the tint color to apply to the button. If you don’t implement this property, the system uses a default color for the tint color.

## See Also

- [var mediaPlayPauseButtonType: UNNotificationContentExtensionMediaPlayPauseButtonType](unnotificationcontentextension/mediaplaypausebuttontype.md)
  The type of media button type to display.
- [enum UNNotificationContentExtensionMediaPlayPauseButtonType](unnotificationcontentextensionmediaplaypausebuttontype.md)
  Constants indicating the type of media button to display.
- [var mediaPlayPauseButtonFrame: CGRect](unnotificationcontentextension/mediaplaypausebuttonframe.md)
  The frame rectangle to use for displaying a media playback button.
- [func mediaPlay()](unnotificationcontentextension/mediaplay.md)
  Tells you to begin playback of your media content.
- [func mediaPause()](unnotificationcontentextension/mediapause.md)
  Tells you to pause playback of your media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextension/mediaplaypausebuttontintcolor)*