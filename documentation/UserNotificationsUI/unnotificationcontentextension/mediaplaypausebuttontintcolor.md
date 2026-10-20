# mediaPlayPauseButtonTintColor

**Framework**: User Notifications UI  
**Kind**: property  
**Role**: Instance Property

The tint color for the media playback button.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
@NSCopying
optional var mediaPlayPauseButtonTintColor: UIColor { get }
```

*macOS*

```swift
@NSCopying
optional var mediaPlayPauseButtonTintColor: NSColor { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) UIColor * mediaPlayPauseButtonTintColor;
```

*macOS*

```objc
@property (nonatomic, copy, readonly) NSColor * mediaPlayPauseButtonTintColor;
```

#### Discussion

If you implement the [`mediaPlayPauseButtonFrame`](./mediaplaypausebuttonframe.md) property, you can also implement this property and use it to specify the tint color to apply to the button. If you don’t implement this property, the system uses a default color for the tint color.

## See Also

### Supporting Media Playback
- [var mediaPlayPauseButtonType: UNNotificationContentExtensionMediaPlayPauseButtonType](./mediaplaypausebuttontype.md)
  The type of media button type to display.
- [enum UNNotificationContentExtensionMediaPlayPauseButtonType](../unnotificationcontentextensionmediaplaypausebuttontype.md)
  Constants indicating the type of media button to display.
- [var mediaPlayPauseButtonFrame: CGRect](./mediaplaypausebuttonframe.md)
  The frame rectangle to use for displaying a media playback button.
- [func mediaPlay()](./mediaplay%28%29.md)
  Tells you to begin playback of your media content.
- [func mediaPause()](./mediapause%28%29.md)
  Tells you to pause playback of your media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextension/mediaplaypausebuttontintcolor)*