# WKWebsiteDataRecord

**Framework**: WebKit  
**Kind**: class

A record of the data that a particular website stores persistently.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKWebsiteDataRecord
```

#### Overview

Use [`WKWebsiteDataRecord`](wkwebsitedatarecord.md) objects to discover the types of information that a website stores. Records identify the data types a website stores, but don’t identify the actual data. You might use this information to help the user manage website data. For example, Safari provides a way for users to view and remove website data. The domain name of each record contains the website’s domain name and suffix.

You don’t create [`WKWebsiteDataRecord`](wkwebsitedatarecord.md) objects directly. WebKit creates these records and stores them in the web view’s data store. Use the [`fetchDataRecords(ofTypes:completionHandler:)`](wkwebsitedatastore/fetchdatarecords(oftypes:completionhandler:).md) of that data store to retrieve the current record objects. You also use that object to remove unwanted records.

## Topics

### Getting the Record Information
- [var displayName: String](wkwebsitedatarecord/displayname.md)
  The display name for the data record.
### Getting the Data Type
- [var dataTypes: Set<String>](wkwebsitedatarecord/datatypes.md)
  The types of data associated with the record.
- [Data Store Record Types](data-store-record-types.md)
  Explore the constants that identify the types of data that websites store.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class WKWebsiteDataStore](wkwebsitedatastore.md)
  An object that manages cookies, disk and memory caches, and other types of data for a web view.
- [class WKHTTPCookieStore](wkhttpcookiestore.md)
  An object that manages the HTTP cookies associated with a particular web view.
- [protocol WKURLSchemeHandler](wkurlschemehandler.md)
  A protocol for loading resources with URL schemes that WebKit doesn’t handle.
- [protocol WKURLSchemeTask](wkurlschemetask.md)
  An interface that WebKit uses to request custom resources from your app.
- [static let readAccessURL: NSAttributedString.DocumentReadingOptionKey](../Foundation/NSAttributedString/DocumentReadingOptionKey/readAccessURL.md)
  The local files WebKit can access when loading content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatarecord)*