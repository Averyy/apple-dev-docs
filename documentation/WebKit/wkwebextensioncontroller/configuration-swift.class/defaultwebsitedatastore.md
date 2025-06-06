# defaultWebsiteDataStore

**Framework**: Webkit  
**Kind**: property

The default data store for website data and cookie access in extension contexts.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var defaultWebsiteDataStore: WKWebsiteDataStore! { get set }
```

#### Discussion

This property sets the primary data store for managing website data, including cookies, which extensions can access, subject to the granted permissions within the extension contexts. Defaults to [`default()`](wkwebsitedatastore/default().md).

> **Note**: In addition to this data store, extensions can also access other data stores, such as non-persistent ones, for any open tabs.

In addition to this data store, extensions can also access other data stores, such as non-persistent ones, for any open tabs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/configuration-swift.class/defaultwebsitedatastore)*