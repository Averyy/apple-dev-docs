# WKHTTPCookieStore

**Framework**: WebKit  
**Kind**: class

An object that manages the HTTP cookies associated with a particular web view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKHTTPCookieStore
```

#### Overview

Use a [`WKHTTPCookieStore`](wkhttpcookiestore.md) to specify the initial cookies for your webpages, and to manage cookies for your web content. For example, you might use this object to delete the cookie for the current session when the user logs out. To detect when the webpage changes a cookie, install a cookie observer using the [`add(_:)`](wkhttpcookiestore/add(_:).md) method.

You don’t create a [`WKHTTPCookieStore`](wkhttpcookiestore.md) object directly. Instead, retrieve this object from the [`WKWebsiteDataStore`](wkwebsitedatastore.md) object in your web view’s configuration object.

## Topics

### Managing cookies
- [func getAllCookies(([HTTPCookie]) -> Void)](wkhttpcookiestore/getallcookies(_:).md)
  Fetches all stored cookies asynchronously and delivers them to the specified completion handler.
- [func setCookie(HTTPCookie, completionHandler: (() -> Void)?)](wkhttpcookiestore/setcookie(_:completionhandler:).md)
  Adds a cookie to the cookie store.
- [func delete(HTTPCookie, completionHandler: (() -> Void)?)](wkhttpcookiestore/delete(_:completionhandler:).md)
  Deletes the specified cookie.
### Permitting cookie storage
- [func getCookiePolicy((WKHTTPCookieStore.CookiePolicy) -> Void)](wkhttpcookiestore/getcookiepolicy(_:).md)
  Returns a cookie policy that indicates whether the cookie store allows cookie storage.
- [func setCookiePolicy(WKHTTPCookieStore.CookiePolicy, completionHandler: (() -> Void)?)](wkhttpcookiestore/setcookiepolicy(_:completionhandler:).md)
  Sets a cookie policy that indicates whether the cookie store allows cookie storage.
- [WKHTTPCookieStore.CookiePolicy](wkhttpcookiestore/cookiepolicy.md)
  An enumeration with cases that indicate whether a cookie store allows cookie storage.
### Observing cookie store changes
- [func add(any WKHTTPCookieStoreObserver)](wkhttpcookiestore/add(_:).md)
  Adds an observer to the cookie store.
- [func remove(any WKHTTPCookieStoreObserver)](wkhttpcookiestore/remove(_:).md)
  Removes an observer from the cookie store.
- [protocol WKHTTPCookieStoreObserver](wkhttpcookiestoreobserver.md)
  The methods to adopt in an object that monitors changes to a webpage’s cookies.

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
- [class WKWebsiteDataRecord](wkwebsitedatarecord.md)
  A record of the data that a particular website stores persistently.
- [protocol WKURLSchemeHandler](wkurlschemehandler.md)
  A protocol for loading resources with URL schemes that WebKit doesn’t handle.
- [protocol WKURLSchemeTask](wkurlschemetask.md)
  An interface that WebKit uses to request custom resources from your app.
- [static let readAccessURL: NSAttributedString.DocumentReadingOptionKey](../Foundation/NSAttributedString/DocumentReadingOptionKey/readAccessURL.md)
  The local files WebKit can access when loading content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkhttpcookiestore)*