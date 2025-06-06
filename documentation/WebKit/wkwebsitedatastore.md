# WKWebsiteDataStore

**Framework**: Webkit  
**Kind**: class

An object that manages cookies, disk and memory caches, and other types of data for a web view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKWebsiteDataStore
```

#### Overview

Use a [`WKWebsiteDataStore`](wkwebsitedatastore.md) object to configure and manage web site data. Specifically, use this object to:

- Manage cookies that your web site uses
- Learn about the types of data that websites store
- Remove unwanted web site data

Create a data store object and assign it to the [`websiteDataStore`](wkwebviewconfiguration/websitedatastore.md) property of a [`WKWebViewConfiguration`](wkwebviewconfiguration.md) object before you create your web view.

By default, `WKWebViewConfiguration` uses the default data store returned by the [`default()`](wkwebsitedatastore/default().md) method, which saves website data persistently to disk.

To implement private browsing, create a nonpersistent data store using the [`nonPersistent()`](wkwebsitedatastore/nonpersistent().md) method instead.

To implement profile browsing, create a persistent data store using the [`init(forIdentifier:)`](wkwebsitedatastore/init(foridentifier:).md) method, passing an identifier that you use to identify the data store.

## Topics

### Creating a data store object
- [class func `default`() -> WKWebsiteDataStore](wkwebsitedatastore/default.md)
  Returns the default data store, which stores data persistently to disk.
- [class func nonPersistent() -> WKWebsiteDataStore](wkwebsitedatastore/nonpersistent.md)
  Creates a new data store object that stores website data in memory, and doesn’t write that data to disk.
- [init(forIdentifier: UUID)](wkwebsitedatastore/init(foridentifier:).md)
  Returns the persistent data store with the unique identifier you provide.
### Finding data stores
- [class func fetchAllDataStoreIdentifiers(([UUID]) -> Void)](wkwebsitedatastore/fetchalldatastoreidentifiers(_:).md)
  Fetches an array of identifiers from existing data stores that have identifiers.
### Inspecting data store properties
- [var identifier: UUID?](wkwebsitedatastore/identifier.md)
  An identifier that uniquely identifies a data store.
- [var isPersistent: Bool](wkwebsitedatastore/ispersistent.md)
  A Boolean value that indicates whether this object stores data to disk.
### Retrieving a cookie store
- [var httpCookieStore: WKHTTPCookieStore](wkwebsitedatastore/httpcookiestore.md)
  The object that manages the HTTP cookies for your website.
### Retrieving specific types of data
- [func fetchDataRecords(ofTypes: Set<String>, completionHandler: ([WKWebsiteDataRecord]) -> Void)](wkwebsitedatastore/fetchdatarecords(oftypes:completionhandler:).md)
  Fetches the specified types of records from the data store.
- [class func allWebsiteDataTypes() -> Set<String>](wkwebsitedatastore/allwebsitedatatypes.md)
  Returns the set of all the available data types.
### Removing specific types of data
- [func removeData(ofTypes: Set<String>, for: [WKWebsiteDataRecord], completionHandler: () -> Void)](wkwebsitedatastore/removedata(oftypes:for:completionhandler:).md)
  Removes the specified types of website data from one or more data records.
- [func removeData(ofTypes: Set<String>, modifiedSince: Date, completionHandler: () -> Void)](wkwebsitedatastore/removedata(oftypes:modifiedsince:completionhandler:).md)
  Removes website data that changed after the specified date.
### Removing a data store
- [class func remove(forIdentifier: UUID, completionHandler: ((any Error)?) -> Void)](wkwebsitedatastore/remove(foridentifier:completionhandler:).md)
  Removes the data store that matches the identifier you provide.
### Instance Properties
- [var proxyConfigurations: [ProxyConfiguration]](wkwebsitedatastore/proxyconfigurations-cdc1.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class WKWebsiteDataRecord](wkwebsitedatarecord.md)
  A record of the data that a particular website stores persistently.
- [class WKHTTPCookieStore](wkhttpcookiestore.md)
  An object that manages the HTTP cookies associated with a particular web view.
- [protocol WKURLSchemeHandler](wkurlschemehandler.md)
  A protocol for loading resources with URL schemes that WebKit doesn’t handle.
- [protocol WKURLSchemeTask](wkurlschemetask.md)
  An interface that WebKit uses to request custom resources from your app.
- [static let readAccessURL: NSAttributedString.DocumentReadingOptionKey](../foundation/nsattributedstring/documentreadingoptionkey/3182829-readaccessurl.md)
  The local files WebKit can access when loading content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatastore)*