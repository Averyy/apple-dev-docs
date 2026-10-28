# isInspectable

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

Indicates whether you can inspect the page with Safari Web Inspector.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
final var isInspectable: Bool { get set }
```

## Discussion

Set to `true` at any point in the page’s lifetime to allow Safari Web Inspector access to inspect the view’s content. Then, select your view in Safari’s Develop menu for either your computer or an attached device to inspect it.

If you set this value to false during inspection, the system immediately closes Safari Web Inspector and does not provide any further information about the web content.

The default value of this property is `false`.

## See Also

### Inspecting page information
- [WebPage.CSSMediaType](./cssmediatype.md)
  A CSS media type as defined by the [CSS specification](https://www.w3.org/TR/mediaqueries-4/#media-types), or an arbitrary media type value.
- [var title: String](./title.md)
  The page title.
- [var url: URL?](./url.md)
  The URL for the current webpage.
- [var mediaType: WebPage.CSSMediaType?](./mediatype.md)
  The media type for the contents of the webpage.
- [var customUserAgent: String?](./customuseragent.md)
  The custom user agent string.
- [var serverTrust: SecTrust?](./servertrust.md)
  The trust management object you use to evaluate trust for the current webpage.
- [var hasOnlySecureContent: Bool](./hasonlysecurecontent.md)
  Indicates whether the webpage loaded all resources on the page through securely encrypted connections.
- [var themeColor: Color?](./themecolor.md)
  The theme color that the system gets from the first valid meta tag in the webpage.
- [var isBlockedByScreenTime: Bool](./isblockedbyscreentime.md)
  Indicates whether Screen Time blocking has occurred.
- [var isWritingToolsActive: Bool](./iswritingtoolsactive.md)
  Indicates whether Writing Tools is active for the page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/isinspectable)*