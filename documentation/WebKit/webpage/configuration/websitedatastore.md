# websiteDataStore

**Framework**: WebKit  
**Kind**: property

The object you use to get and set the site’s cookies and to track the cached data objects.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var websiteDataStore: WKWebsiteDataStore
```

#### Discussion

To create a private web-browsing session, create a non-persistent data store using the `nonPersistent()` method and assign it to this property. For more information, see `WKWebsiteDataStore`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/configuration/websitedatastore)*