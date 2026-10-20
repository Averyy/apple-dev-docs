# default()

**Framework**: WebKit  
**Kind**: method  
**Role**: Type Method

Returns the default data store, which stores data persistently to disk.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class func `default`() -> WKWebsiteDataStore
```

```objc
+ (WKWebsiteDataStore *) defaultDataStore;
```

#### Return Value

The default data store for websites.

#### Discussion

A web view configured with the default data store saves website data persistenly to disk. Use this data store to retain the state of web content between browsing sessions.

## See Also

### Creating a data store object
- [class func nonPersistent() -> WKWebsiteDataStore](./nonpersistent%28%29.md)
  Creates a new data store object that stores website data in memory, and doesn’t write that data to disk.
- [init(forIdentifier: UUID)](./init%28foridentifier%29.md)
  Returns the persistent data store with the unique identifier you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/default())*