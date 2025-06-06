# underPageBackgroundColor

**Framework**: Webkit  
**Kind**: property

The color the web view displays behind the active page, visible when the user scrolls beyond the bounds of the page.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var underPageBackgroundColor: UIColor! { get set }
```

#### Discussion

The web view derives the default value of this property from the content of the page, using the background colors of the `<html>` and `<body>` elements with the background color of the web view. To override the default color, set this property to a new color.

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
- [var hasOnlySecureContent: Bool](wkwebview/hasonlysecurecontent.md)
  A Boolean value that indicates whether the web view loaded all resources on the page through securely encrypted connections.
- [var themeColor: UIColor?](wkwebview/themecolor.md)
  The theme color that the system gets from the first valid meta tag in the webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/underpagebackgroundcolor)*