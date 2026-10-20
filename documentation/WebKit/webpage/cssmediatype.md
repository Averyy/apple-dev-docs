# WebPage.CSSMediaType

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

A CSS media type as defined by the [CSS specification](https://www.w3.org/TR/mediaqueries-4/#media-types), or an arbitrary media type value.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct CSSMediaType
```

#### Overview

Media types are one of several media queries that influence the `@media` CSS at-rule; this rule is used by webpages to apply parts of a style sheet depending on the media properties specified.

You can customize the media type of a [`WebPage`](../webpage.md) by using the [`mediaType`](./mediatype.md) property.

## Topics

### Initializers
- [init(rawValue: String)](./cssmediatype/init%28rawvalue%29.md)
  Create a media type with an arbitrary value.
### Instance Properties
- [let rawValue: String](./cssmediatype/rawvalue.md)
  The raw value of the media type.
### Type Properties
- [static let all: WebPage.CSSMediaType](./cssmediatype/all.md)
  Corresponds to the “all” media type.
- [static let print: WebPage.CSSMediaType](./cssmediatype/print.md)
  Corresponds to the “print” media type.
- [static let screen: WebPage.CSSMediaType](./cssmediatype/screen.md)
  Corresponds to the “screen” media type.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting page information
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
- [var isInspectable: Bool](./isinspectable.md)
  Indicates whether you can inspect the page with Safari Web Inspector.
- [var isWritingToolsActive: Bool](./iswritingtoolsactive.md)
  Indicates whether Writing Tools is active for the page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/cssmediatype)*