# mediaType

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The media type for the contents of the webpage.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
final var mediaType: WebPage.CSSMediaType? { get set }
```

#### Discussion

When the value of this property is `nil`, the webpage derives the current media type from the CSS media property of its content. If you assign a value other than `nil` to this property, the webpage uses the value you provide instead.

For example, you can use this property to configure a page for viewing as a print preview by setting it to [`print`](./cssmediatype/print.md).

The default value of this property is `nil`.

## See Also

### Inspecting page information
- [WebPage.CSSMediaType](./cssmediatype.md)
  A CSS media type as defined by the [CSS specification](https://www.w3.org/TR/mediaqueries-4/#media-types), or an arbitrary media type value.
- [var title: String](./title.md)
  The page title.
- [var url: URL?](./url.md)
  The URL for the current webpage.
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

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/mediatype)*