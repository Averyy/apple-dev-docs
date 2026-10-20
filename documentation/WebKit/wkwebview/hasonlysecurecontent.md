# hasOnlySecureContent

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the web view loaded all resources on the page through securely encrypted connections.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var hasOnlySecureContent: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasOnlySecureContent;
```

#### Discussion

[`WKWebView`](../wkwebview.md) is key-value observing (KVO) compliant for this property.

## See Also

### Inspecting the view information
- [var scrollView: UIScrollView](./scrollview.md)
  The scroll view associated with the web view.
- [var title: String?](./title.md)
  The page title.
- [var url: URL?](./url.md)
  The URL for the current webpage.
- [var mediaType: String?](./mediatype.md)
  The media type for the contents of the web view.
- [var customUserAgent: String?](./customuseragent.md)
  The custom user agent string.
- [var serverTrust: SecTrust?](./servertrust.md)
  The trust management object you use to evaluate trust for the current webpage.
- [var themeColor: UIColor?](./themecolor.md)
  The theme color that the system gets from the first valid meta tag in the webpage.
- [var underPageBackgroundColor: UIColor!](./underpagebackgroundcolor.md)
  The color the web view displays behind the active page, visible when the user scrolls beyond the bounds of the page.
- [var refreshController: NSRefreshController?](./refreshcontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/hasonlysecurecontent)*