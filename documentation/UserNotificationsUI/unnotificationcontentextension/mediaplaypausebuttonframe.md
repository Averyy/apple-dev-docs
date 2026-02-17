# mediaPlayPauseButtonFrame

**Framework**: User Notifications UI  
**Kind**: property

The frame rectangle to use for displaying a media playback button.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var mediaPlayPauseButtonFrame: CGRect { get }
```

## Mentions

- [Customizing the Appearance of Notifications](customizing-the-appearance-of-notifications.md)

#### Discussion

If you support the playback of media directly from your notification interface, implement this property and use it to return a nonempty rectangle specified in the coordinate system of your view controller’s view. The system draws a button in the provided rectangle that lets the user play and pause your media content. The system handles the drawing of the button for you and calls the [`mediaPlay()`](unnotificationcontentextension/mediaplay().md) and [`mediaPause()`](unnotificationcontentextension/mediapause().md) methods in response to user interactions. You can place this button anywhere in your view controller’s view.

If you don’t implement this property, the system doesn’t draw a media playback button.

## See Also

- [var mediaPlayPauseButtonType: UNNotificationContentExtensionMediaPlayPauseButtonType](unnotificationcontentextension/mediaplaypausebuttontype.md)
  The type of media button type to display.
- [enum UNNotificationContentExtensionMediaPlayPauseButtonType](unnotificationcontentextensionmediaplaypausebuttontype.md)
  Constants indicating the type of media button to display.
- [var mediaPlayPauseButtonTintColor: UIColor](unnotificationcontentextension/mediaplaypausebuttontintcolor.md)
  The tint color for the media playback button.
- [func mediaPlay()](unnotificationcontentextension/mediaplay.md)
  Tells you to begin playback of your media content.
- [func mediaPause()](unnotificationcontentextension/mediapause.md)
  Tells you to pause playback of your media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextension/mediaplaypausebuttonframe)*