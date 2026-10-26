# WKWebsiteDataStore

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface WKWebsiteDataStore : NSObject
```

#### Overview

Use a [`WKWebsiteDataStore`](./wkwebsitedatastore.md) object to configure and manage web site data. Specifically, use this object to:

- Manage cookies that your web site uses
- Learn about the types of data that websites store
- Remove unwanted web site data

Create a data store object and assign it to the [`websiteDataStore`](./wkwebviewconfiguration/websitedatastore.md) property of a [`WKWebViewConfiguration`](./wkwebviewconfiguration.md) object before you create your web view.

By default, `WKWebViewConfiguration` uses the default data store returned by the [`default()`](./wkwebsitedatastore/default%28%29.md) method, which saves website data persistently to disk.

To implement private browsing, create a nonpersistent data store using the [`nonPersistent()`](./wkwebsitedatastore/nonpersistent%28%29.md) method instead.

To implement profile browsing, create a persistent data store using the [`init(forIdentifier:)`](./wkwebsitedatastore/init%28foridentifier%29.md) method, passing an identifier that you use to identify the data store.

## Topics

### Creating a data store object
- [class func `default`() -> WKWebsiteDataStore](./wkwebsitedatastore/default%28%29.md)
  Returns the default data store, which stores data persistently to disk.
- [class func nonPersistent() -> WKWebsiteDataStore](./wkwebsitedatastore/nonpersistent%28%29.md)
  Creates a new data store object that stores website data in memory, and doesn’t write that data to disk.
- [init(forIdentifier: UUID)](./wkwebsitedatastore/init%28foridentifier%29.md)
  Returns the persistent data store with the unique identifier you provide.
### Finding data stores
- [class func fetchAllDataStoreIdentifiers(([UUID]) -> Void)](./wkwebsitedatastore/fetchalldatastoreidentifiers%28_%29.md)
  Fetches an array of identifiers from existing data stores that have identifiers.
### Inspecting data store properties
- [var identifier: UUID?](./wkwebsitedatastore/identifier.md)
  An identifier that uniquely identifies a data store.
- [var isPersistent: Bool](./wkwebsitedatastore/ispersistent.md)
  A Boolean value that indicates whether this object stores data to disk.
### Retrieving a cookie store
- [var httpCookieStore: WKHTTPCookieStore](./wkwebsitedatastore/httpcookiestore.md)
  The object that manages the HTTP cookies for your website.
### Retrieving specific types of data
- [func fetchDataRecords(ofTypes: Set<String>, completionHandler: ([WKWebsiteDataRecord]) -> Void)](./wkwebsitedatastore/fetchdatarecords%28oftypes,completionhandler%29.md)
  Fetches the specified types of records from the data store.
- [class func allWebsiteDataTypes() -> Set<String>](./wkwebsitedatastore/allwebsitedatatypes%28%29.md)
  Returns the set of all the available data types.
### Removing specific types of data
- [func removeData(ofTypes: Set<String>, for: [WKWebsiteDataRecord], completionHandler: () -> Void)](./wkwebsitedatastore/removedata%28oftypes,for,completionhandler%29.md)
  Removes the specified types of website data from one or more data records.
- [func removeData(ofTypes: Set<String>, modifiedSince: Date, completionHandler: () -> Void)](./wkwebsitedatastore/removedata%28oftypes,modifiedsince,completionhandler%29.md)
  Removes website data that changed after the specified date.
### Removing a data store
- [class func remove(forIdentifier: UUID, completionHandler: ((any Error)?) -> Void)](./wkwebsitedatastore/remove%28foridentifier,completionhandler%29.md)
  Removes the data store that matches the identifier you provide.
### Initializers
- [init?(coder: NSCoder)](./wkwebsitedatastore/init%28coder%29.md)
### Instance Properties
- [var proxyConfigurations: [ProxyConfiguration]](./wkwebsitedatastore/proxyconfigurations-cdc1.md)
- [proxyConfigurations](./wkwebsitedatastore/proxyconfigurations-6g21z.md)
### Instance Methods
- [func fetchData(of: Set<String>, completionHandler: (Data?, (any Error)?) -> Void)](./wkwebsitedatastore/fetchdata%28of,completionhandler%29.md)
- [func restoreData(Data, completionHandler: ((any Error)?) -> Void)](./wkwebsitedatastore/restoredata%28_,completionhandler%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Web data management
- [class WKWebsiteDataRecord](./wkwebsitedatarecord.md)
  A record of the data that a particular website stores persistently.
- [class WKHTTPCookieStore](./wkhttpcookiestore.md)
  An object that manages the HTTP cookies associated with a particular web view.
- [protocol WKURLSchemeHandler](./wkurlschemehandler.md)
  A protocol for loading resources with URL schemes that WebKit doesn’t handle.
- [protocol WKURLSchemeTask](./wkurlschemetask.md)
  An interface that WebKit uses to request custom resources from your app.
- [static let readAccessURL: NSAttributedString.DocumentReadingOptionKey](../Foundation/nsattributedstring/documentreadingoptionkey/readaccessurl.md)
  The local files WebKit can access when loading content.
- [NSReadAccessURLDocumentOption](./nsreadaccessurldocumentoption.md)
- [WKCookiePolicy](./wkhttpcookiestore/cookiepolicy.md)
  An enumeration with cases that indicate whether a cookie store allows cookie storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatastore)*