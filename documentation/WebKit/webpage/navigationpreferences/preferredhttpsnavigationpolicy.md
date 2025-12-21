# preferredHTTPSNavigationPolicy

**Framework**: WebKit  
**Kind**: property

Used when performing a top-level navigation to a webpage.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var preferredHTTPSNavigationPolicy: WebPage.NavigationPreferences.UpgradeToHTTPSPolicy
```

#### Discussion

The default value is `.keepAsRequested`. The stated preference is ignored on subframe navigation, and it may be ignored based on system configuration. The `WebPage.Configuration.upgradeKnownHostsToHTTPS` property supersedes this property for known hosts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationpreferences/preferredhttpsnavigationpolicy)*