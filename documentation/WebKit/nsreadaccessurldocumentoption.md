# NSReadAccessURLDocumentOption

**Framework**: WebKit  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```c
extern NSAttributedStringDocumentReadingOptionKey const NSReadAccessURLDocumentOption;
```

#### Discussion

Indicates which local files WebKit can access when loading content.

If NSReadAccessURLDocumentOption references a single file, only that file may be loaded by WebKit. If NSReadAccessURLDocumentOption references a directory, files inside that directory may be loaded by WebKit.

## See Also

### Web data management
- [class WKWebsiteDataStore](./wkwebsitedatastore.md)
  An object that manages cookies, disk and memory caches, and other types of data for a web view.
- [class WKWebsiteDataRecord](./wkwebsitedatarecord.md)
  A record of the data that a particular website stores persistently.
- [class WKHTTPCookieStore](./wkhttpcookiestore.md)
  An object that manages the HTTP cookies associated with a particular web view.
- [protocol WKURLSchemeHandler](./wkurlschemehandler.md)
  A protocol for loading resources with URL schemes that WebKit doesn’t handle.
- [protocol WKURLSchemeTask](./wkurlschemetask.md)
  An interface that WebKit uses to request custom resources from your app.
- [WKHTTPCookieStore.CookiePolicy](./wkhttpcookiestore/cookiepolicy.md)
  An enumeration with cases that indicate whether a cookie store allows cookie storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/nsreadaccessurldocumentoption)*