# UNNotificationContentExtensionMediaPlayPauseButtonType

**Framework**: User Notifications UI  
**Kind**: enum

Constants indicating the type of media button to display.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum UNNotificationContentExtensionMediaPlayPauseButtonType
```

## Topics

### Button Types
- [UNNotificationContentExtensionMediaPlayPauseButtonType.none](unnotificationcontentextensionmediaplaypausebuttontype/none.md)
  No media button.
- [UNNotificationContentExtensionMediaPlayPauseButtonType.default](unnotificationcontentextensionmediaplaypausebuttontype/default.md)
  A standard play/pause button.
- [UNNotificationContentExtensionMediaPlayPauseButtonType.overlay](unnotificationcontentextensionmediaplaypausebuttontype/overlay.md)
  A partially transparent play/pause button that is layered on top of your media content.
### Initializers
- [init?(rawValue: UInt)](unnotificationcontentextensionmediaplaypausebuttontype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var mediaPlayPauseButtonType: UNNotificationContentExtensionMediaPlayPauseButtonType](unnotificationcontentextension/mediaplaypausebuttontype.md)
  The type of media button type to display.
- [var mediaPlayPauseButtonFrame: CGRect](unnotificationcontentextension/mediaplaypausebuttonframe.md)
  The frame rectangle to use for displaying a media playback button.
- [var mediaPlayPauseButtonTintColor: UIColor](unnotificationcontentextension/mediaplaypausebuttontintcolor.md)
  The tint color for the media playback button.
- [func mediaPlay()](unnotificationcontentextension/mediaplay.md)
  Tells you to begin playback of your media content.
- [func mediaPause()](unnotificationcontentextension/mediapause.md)
  Tells you to pause playback of your media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextensionmediaplaypausebuttontype)*