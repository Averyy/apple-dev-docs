# delete(_:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Deletes the specified cookie.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func delete(_ cookie: HTTPCookie, completionHandler: (@MainActor @Sendable () -> Void)? = nil)
```

```swift
func deleteCookie(_ cookie: HTTPCookie) async
```

```objc
- (void) deleteCookie:(NSHTTPCookie *) cookie completionHandler:(void (^)(void)) completionHandler;
```

## Parameters

- `cookie`: The cookie to delete.
- `completionHandler`: A completion handler block to execute asynchronously after the method successfully deletes the cookie. This block has no return value and no parameters.

## See Also

### Managing cookies
- [func getAllCookies(([HTTPCookie]) -> Void)](./getallcookies%28_%29.md)
  Fetches all stored cookies asynchronously and delivers them to the specified completion handler.
- [func setCookie(HTTPCookie, completionHandler: (() -> Void)?)](./setcookie%28_,completionhandler%29.md)
  Adds a cookie to the cookie store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkhttpcookiestore/delete(_:completionhandler:))*