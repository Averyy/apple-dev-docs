# isInspectable

**Framework**: WebKit  
**Kind**: property

Indicates whether you can inspect the view with Safari Web Inspector.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
final var isInspectable: Bool { get set }
```

#### Discussion

Set to true at any point in the view’s lifetime to allow Safari Web Inspector access to inspect the view’s content. Then, select your view in Safari’s Develop menu for either your computer or an attached device to inspect it.

If you set this value to false during inspection, the system immediately closes Safari Web Inspector and does not provide any further information about the web content.

The default value of this property is `false`.

## See Also

- [WebPage.CSSMediaType](webpage/cssmediatype.md)
  A CSS media type as defined by the [`CSS specification`](https://developer.apple.comhttps://www.w3.org/TR/mediaqueries-4/#media-types), or an arbitrary media type value.
- [var title: String](webpage/title.md)
  The page title.
- [var url: URL?](webpage/url.md)
  The URL for the current webpage.
- [var mediaType: WebPage.CSSMediaType?](webpage/mediatype.md)
  The media type for the contents of the web view.
- [var customUserAgent: String?](webpage/customuseragent.md)
  The custom user agent string.
- [var serverTrust: SecTrust?](webpage/servertrust.md)
  The trust management object you use to evaluate trust for the current webpage.
- [var hasOnlySecureContent: Bool](webpage/hasonlysecurecontent.md)
  Indicates whether the webpage loaded all resources on the page through securely encrypted connections.
- [var themeColor: Color?](webpage/themecolor.md)
  The theme color that the system gets from the first valid meta tag in the webpage.
- [var isBlockedByScreenTime: Bool](webpage/isblockedbyscreentime.md)
  Indicates whether Screen Time blocking has occurred.
- [var isWritingToolsActive: Bool](webpage/iswritingtoolsactive.md)
  Indicates whether Writing Tools is active for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/isinspectable)*