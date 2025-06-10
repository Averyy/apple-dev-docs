# nonPersistent()

**Framework**: WebKit  
**Kind**: method

Creates a new data store object that stores website data in memory, and doesn’t write that data to disk.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func nonPersistent() -> WKWebsiteDataStore
```

#### Return Value

A new data store object that doesn’t save data to disk.

#### Discussion

Use a nonpersistent data store to implement private browsing in your web view. This method creates a new data store that stores data only in memory, and doesn’t write that data to disk.

## See Also

- [class func `default`() -> WKWebsiteDataStore](wkwebsitedatastore/default.md)
  Returns the default data store, which stores data persistently to disk.
- [init(forIdentifier: UUID)](wkwebsitedatastore/init(foridentifier:).md)
  Returns the persistent data store with the unique identifier you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/nonpersistent())*