# processPool

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The object that coordinates the processes the web view uses to render its web content and execute scripts.

**Availability**:
- iOS 8.0+ - Deprecated in 15.0
- iPadOS 8.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.10+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Creating and using multiple instances of WKProcessPool no longer has any effect.

## Declaration

```swift
var processPool: WKProcessPool { get set }
```

```objc
@property (nonatomic, strong) WKProcessPool * processPool;
```

#### Discussion

When it initializes a web view, WebKit either creates a new web content process in the specified pool, or uses an existing process from that pool.

## See Also

### Configuring the web view’s behavior
- [var websiteDataStore: WKWebsiteDataStore](./websitedatastore.md)
  The object you use to get and set the site’s cookies and to track the cached data objects.
- [var userContentController: WKUserContentController](./usercontentcontroller.md)
  The object that coordinates interactions between your app’s native code and the webpage’s scripts and other content.
- [var applicationNameForUserAgent: String?](./applicationnameforuseragent.md)
  The app name that appears in the user agent string.
- [var limitsNavigationsToAppBoundDomains: Bool](./limitsnavigationstoappbounddomains.md)
  A Boolean value that indicates whether the web view limits navigation to pages within the app’s domain.
- [var upgradeKnownHostsToHTTPS: Bool](./upgradeknownhoststohttps.md)
  A Boolean value that indicates whether the web view should automatically upgrade supported HTTP requests to HTTPS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/processpool)*