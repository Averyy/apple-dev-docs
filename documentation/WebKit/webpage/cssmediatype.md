# WebPage.CSSMediaType

**Framework**: WebKit  
**Kind**: struct

A CSS media type as defined by the [`CSS specification`](https://developer.apple.comhttps://www.w3.org/TR/mediaqueries-4/#media-types), or an arbitrary media type value.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
struct CSSMediaType
```

## Topics

### Initializers
- [init(rawValue: String)](webpage/cssmediatype/init(rawvalue:).md)
  Create a media type with an arbitrary value. Use the static type properties for the defined canonical CSS media type options.
### Instance Properties
- [let rawValue: String](webpage/cssmediatype/rawvalue.md)
  The raw value of the media type.
### Type Properties
- [static let all: WebPage.CSSMediaType](webpage/cssmediatype/all.md)
  Corresponds to the “all” media type.
- [static let print: WebPage.CSSMediaType](webpage/cssmediatype/print.md)
  Corresponds to the “print” media type.
- [static let screen: WebPage.CSSMediaType](webpage/cssmediatype/screen.md)
  Corresponds to the “screen” media type.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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
- [var isInspectable: Bool](webpage/isinspectable.md)
  Indicates whether you can inspect the view with Safari Web Inspector.
- [var isWritingToolsActive: Bool](webpage/iswritingtoolsactive.md)
  Indicates whether Writing Tools is active for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/cssmediatype)*