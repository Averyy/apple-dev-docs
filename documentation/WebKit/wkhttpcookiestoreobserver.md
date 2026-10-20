# WKHTTPCookieStoreObserver

**Framework**: WebKit  
**Kind**: protocol  
**Role**: Protocol

The methods to adopt in an object that monitors changes to a webpage’s cookies.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol WKHTTPCookieStoreObserver : NSObjectProtocol
```

```objc
@protocol WKHTTPCookieStoreObserver <NSObject>
```

#### Overview

Adopt the methods of the [`WKHTTPCookieStoreObserver`](./wkhttpcookiestoreobserver.md) protocol to track changes to cookies associated with a webpage. To observe the actual cookie changes, call the [`add(_:)`](./wkhttpcookiestore/add%28_%29.md) method of the [`WKHTTPCookieStore`](./wkhttpcookiestore.md) you use to manage cookies. When a cookie changes, the cookie store notifies all observers of the changes.

## Topics

### Responding to Cookie Changes
- [func cookiesDidChange(in: WKHTTPCookieStore)](./wkhttpcookiestoreobserver/cookiesdidchange%28in%29.md)
  Tells the delegate that the cookies in the specified cookie store changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Observing cookie store changes
- [func add(any WKHTTPCookieStoreObserver)](./wkhttpcookiestore/add%28_%29.md)
  Adds an observer to the cookie store.
- [func remove(any WKHTTPCookieStoreObserver)](./wkhttpcookiestore/remove%28_%29.md)
  Removes an observer from the cookie store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkhttpcookiestoreobserver)*