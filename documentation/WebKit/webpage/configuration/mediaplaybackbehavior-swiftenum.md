# WebPage.Configuration.MediaPlaybackBehavior

**Framework**: WebKit  
**Kind**: enum

The behavior used when playing HTML video within a page.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- visionOS 2.4+

## Declaration

```swift
enum MediaPlaybackBehavior
```

## Topics

### Enumeration Cases
- [WebPage.Configuration.MediaPlaybackBehavior.allowsInlinePlayback](webpage/configuration/mediaplaybackbehavior-swift.enum/allowsinlineplayback.md)
  Allows videos to play inline. When adding a video element to an HTML document on iPhone, you must also include the `playsinline` attribute.
- [WebPage.Configuration.MediaPlaybackBehavior.alwaysFullscreen](webpage/configuration/mediaplaybackbehavior-swift.enum/alwaysfullscreen.md)
  Use the native fullscreen controller.
- [WebPage.Configuration.MediaPlaybackBehavior.automatic](webpage/configuration/mediaplaybackbehavior-swift.enum/automatic.md)
  Use the default system value, which is `alwaysFullscreen` for iPhone and `allowsInlinePlayback` for iPad.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/configuration/mediaplaybackbehavior-swift.enum)*