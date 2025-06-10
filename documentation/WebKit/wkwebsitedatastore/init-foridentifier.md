# init(forIdentifier:)

**Framework**: WebKit  
**Kind**: init

Returns the persistent data store with the unique identifier you provide.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(forIdentifier identifier: UUID)
```

#### Discussion

If the data store for the unique identifier you provide does not exist, the system creates and returns it. Use this method to get a data store for a profile.

This method throws an exception if the identifier is not valid.

## Parameters

- `identifier`: An identifier that uniquely identifies a data store.

## See Also

- [class func `default`() -> WKWebsiteDataStore](wkwebsitedatastore/default.md)
  Returns the default data store, which stores data persistently to disk.
- [class func nonPersistent() -> WKWebsiteDataStore](wkwebsitedatastore/nonpersistent.md)
  Creates a new data store object that stores website data in memory, and doesn’t write that data to disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/init(foridentifier:))*