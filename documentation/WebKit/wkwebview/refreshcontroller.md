# refreshController

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- macOS 27.0+

## Declaration

```swift
var refreshController: NSRefreshController? { get set }
```

```objc
@property (strong, nullable) NSRefreshController * refreshController;
```

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
- [var hasOnlySecureContent: Bool](./hasonlysecurecontent.md)
  A Boolean value that indicates whether the web view loaded all resources on the page through securely encrypted connections.
- [var themeColor: UIColor?](./themecolor.md)
  The theme color that the system gets from the first valid meta tag in the webpage.
- [var underPageBackgroundColor: UIColor!](./underpagebackgroundcolor.md)
  The color the web view displays behind the active page, visible when the user scrolls beyond the bounds of the page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/refreshcontroller)*