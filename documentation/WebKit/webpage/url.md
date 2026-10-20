# url

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The URL for the current webpage.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
final var url: URL? { get }
```

#### Discussion

This property contains the URL for the webpage currently being presented. Use this URL in places where you reflect the webpage address in your app’s user interface. If the webpage has not loaded any content yet, this value will be `nil`.

## See Also

### Inspecting page information
- [WebPage.CSSMediaType](./cssmediatype.md)
  A CSS media type as defined by the [CSS specification](https://www.w3.org/TR/mediaqueries-4/#media-types), or an arbitrary media type value.
- [var title: String](./title.md)
  The page title.
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
- [var isInspectable: Bool](./isinspectable.md)
  Indicates whether you can inspect the page with Safari Web Inspector.
- [var isWritingToolsActive: Bool](./iswritingtoolsactive.md)
  Indicates whether Writing Tools is active for the page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/url)*