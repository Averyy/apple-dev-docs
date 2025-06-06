# mediaPause()

**Framework**: User Notifications UI  
**Kind**: method

Tells you to pause playback of your media content.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func mediaPause()
```

## Mentions

- [Customizing the Appearance of Notifications](customizing-the-appearance-of-notifications.md)

#### Discussion

Don’t call this method yourself. If you implement the [`mediaPlayPauseButtonFrame`](unnotificationcontentextension/mediaplaypausebuttonframe.md) property in your view controller, the system calls this method when the user wants to stop playback of your media. Use your implementation of this method to pause playback at the current location.

## See Also

- [var mediaPlayPauseButtonType: UNNotificationContentExtensionMediaPlayPauseButtonType](unnotificationcontentextension/mediaplaypausebuttontype.md)
  The type of media button type to display.
- [enum UNNotificationContentExtensionMediaPlayPauseButtonType](unnotificationcontentextensionmediaplaypausebuttontype.md)
  Constants indicating the type of media button to display.
- [var mediaPlayPauseButtonFrame: CGRect](unnotificationcontentextension/mediaplaypausebuttonframe.md)
  The frame rectangle to use for displaying a media playback button.
- [var mediaPlayPauseButtonTintColor: UIColor](unnotificationcontentextension/mediaplaypausebuttontintcolor.md)
  The tint color for the media playback button.
- [func mediaPlay()](unnotificationcontentextension/mediaplay.md)
  Tells you to begin playback of your media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextension/mediapause())*