# hasOnlySecureContent

**Framework**: Webkit  
**Kind**: property

A Boolean value that indicates whether the web view loaded all resources on the page through securely encrypted connections.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var hasOnlySecureContent: Bool { get }
```

#### Discussion

[`WKWebView`](wkwebview.md) is key-value observing (KVO) compliant for this property.

## See Also

- [var scrollView: UIScrollView](wkwebview/scrollview.md)
  The scroll view associated with the web view.
- [var title: String?](wkwebview/title.md)
  The page title.
- [var url: URL?](wkwebview/url.md)
  The URL for the current webpage.
- [var mediaType: String?](wkwebview/mediatype.md)
  The media type for the contents of the web view.
- [var customUserAgent: String?](wkwebview/customuseragent.md)
  The custom user agent string.
- [var serverTrust: SecTrust?](wkwebview/servertrust.md)
  The trust management object you use to evaluate trust for the current webpage.
- [var themeColor: UIColor?](wkwebview/themecolor.md)
  The theme color that the system gets from the first valid meta tag in the webpage.
- [var underPageBackgroundColor: UIColor!](wkwebview/underpagebackgroundcolor.md)
  The color the web view displays behind the active page, visible when the user scrolls beyond the bounds of the page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/hasonlysecurecontent)*