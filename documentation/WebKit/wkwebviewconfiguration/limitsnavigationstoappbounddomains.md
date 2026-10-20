# limitsNavigationsToAppBoundDomains

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the web view limits navigation to pages within the app’s domain.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var limitsNavigationsToAppBoundDomains: Bool { get set }
```

```objc
@property (nonatomic) BOOL limitsNavigationsToAppBoundDomains;
```

## See Also

### Configuring the web view’s behavior
- [var websiteDataStore: WKWebsiteDataStore](./websitedatastore.md)
  The object you use to get and set the site’s cookies and to track the cached data objects.
- [var userContentController: WKUserContentController](./usercontentcontroller.md)
  The object that coordinates interactions between your app’s native code and the webpage’s scripts and other content.
- [var processPool: WKProcessPool](./processpool.md)
  The object that coordinates the processes the web view uses to render its web content and execute scripts.
- [var applicationNameForUserAgent: String?](./applicationnameforuseragent.md)
  The app name that appears in the user agent string.
- [var upgradeKnownHostsToHTTPS: Bool](./upgradeknownhoststohttps.md)
  A Boolean value that indicates whether the web view should automatically upgrade supported HTTP requests to HTTPS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/limitsnavigationstoappbounddomains)*