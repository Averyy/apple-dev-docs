# preferredHTTPSNavigationPolicy

**Framework**: WebKit  
**Kind**: property

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- visionOS 2.2+

## Declaration

```swift
@MainActor
var preferredHTTPSNavigationPolicy: WKWebpagePreferences.UpgradeToHTTPSPolicy { get set }
```

#### Discussion

A WKWebpagePreferencesUpgradeToHTTPSPolicy indicating the desired mode used when performing a top-level navigation to a webpage.

The default value is WKWebpagePreferencesUpgradeToHTTPSPolicyKeepAsRequested. The stated preference is ignored on subframe navigation, and it may be ignored based on system configuration. The upgradeKnownHostsToHTTPS property on WKWebViewConfiguration supercedes this policy for known hosts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebpagepreferences/preferredhttpsnavigationpolicy)*