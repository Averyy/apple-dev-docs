# websiteDataStore

**Framework**: WebKit  
**Kind**: property

The object you use to get and set the site’s cookies and to track the cached data objects.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
var websiteDataStore: WKWebsiteDataStore
```

#### Discussion

To create a private web-browsing session, create a non-persistent data store using the `nonPersistent()` method and assign it to this property. For more information, see `WKWebsiteDataStore`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/configuration/websitedatastore)*