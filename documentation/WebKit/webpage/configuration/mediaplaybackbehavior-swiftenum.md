# WebPage.Configuration.MediaPlaybackBehavior

**Framework**: WebKit  
**Kind**: enum

The behavior used when playing HTML video within a page.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- visionOS 26.0+

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
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [WebPage.Configuration](webpage/configuration.md)
  A configuration type that specifies the preferences and behaviors of a webpage.
- [WebPage.DeviceSensorAuthorization](webpage/devicesensorauthorization.md)
  A type that describes the authorization permissions policy for the device’s sensors a web resource may access.
- [struct URLScheme](urlscheme.md)
  A type representing a valid URL scheme.
- [protocol URLSchemeHandler](urlschemehandler.md)
  A protocol for loading resources with URL schemes that WebKit doesn’t handle.
- [enum URLSchemeTaskResult](urlschemetaskresult.md)
  A value used as part of a sequence of results from a [`URLSchemeHandler`](urlschemehandler.md), which can either be a `Data` or a `URLResponse`.
- [WebPage.DeviceSensorAuthorization.Permission](webpage/devicesensorauthorization/permission.md)
  The kind of sensor permission a web resource may request to access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/configuration/mediaplaybackbehavior-swift.enum)*