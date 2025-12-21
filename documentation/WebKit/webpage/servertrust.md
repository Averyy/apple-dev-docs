# serverTrust

**Framework**: WebKit  
**Kind**: property

The trust management object you use to evaluate trust for the current webpage.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
final var serverTrust: SecTrust? { get }
```

#### Discussion

Use the object in this property to validate the webpage’s certificate and associated credentials. See [`Evaluating a Trust and Parsing the Result`](https://developer.apple.com/documentation/Security/evaluating-a-trust-and-parsing-the-result) for more details on how to use the trust.

## See Also

- [WebPage.CSSMediaType](webpage/cssmediatype.md)
  A CSS media type as defined by the [`CSS specification`](https://developer.apple.comhttps://www.w3.org/TR/mediaqueries-4/#media-types), or an arbitrary media type value.
- [var title: String](webpage/title.md)
  The page title.
- [var url: URL?](webpage/url.md)
  The URL for the current webpage.
- [var mediaType: WebPage.CSSMediaType?](webpage/mediatype.md)
  The media type for the contents of the webpage.
- [var customUserAgent: String?](webpage/customuseragent.md)
  The custom user agent string.
- [var hasOnlySecureContent: Bool](webpage/hasonlysecurecontent.md)
  Indicates whether the webpage loaded all resources on the page through securely encrypted connections.
- [var themeColor: Color?](webpage/themecolor.md)
  The theme color that the system gets from the first valid meta tag in the webpage.
- [var isBlockedByScreenTime: Bool](webpage/isblockedbyscreentime.md)
  Indicates whether Screen Time blocking has occurred.
- [var isInspectable: Bool](webpage/isinspectable.md)
  Indicates whether you can inspect the page with Safari Web Inspector.
- [var isWritingToolsActive: Bool](webpage/iswritingtoolsactive.md)
  Indicates whether Writing Tools is active for the page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/servertrust)*