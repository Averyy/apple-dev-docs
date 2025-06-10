# remove(_:)

**Framework**: WebKit  
**Kind**: method

Removes an observer from the cookie store.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func remove(_ observer: any WKHTTPCookieStoreObserver)
```

## Parameters

- `observer`: The observer object to remove.

## See Also

- [func add(any WKHTTPCookieStoreObserver)](wkhttpcookiestore/add(_:).md)
  Adds an observer to the cookie store.
- [protocol WKHTTPCookieStoreObserver](wkhttpcookiestoreobserver.md)
  The methods to adopt in an object that monitors changes to a webpage’s cookies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkhttpcookiestore/remove(_:))*