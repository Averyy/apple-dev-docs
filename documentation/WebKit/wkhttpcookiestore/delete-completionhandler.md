# delete(_:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Deletes the specified cookie.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func deleteCookie(_ cookie: HTTPCookie) async
```

## Parameters

- `cookie`: The cookie to delete.
- `completionHandler`: A completion handler block to execute asynchronously after the method successfully deletes the cookie. This block has no return value and no parameters.

## See Also

- [func getAllCookies(([HTTPCookie]) -> Void)](wkhttpcookiestore/getallcookies(_:).md)
  Fetches all stored cookies asynchronously and delivers them to the specified completion handler.
- [func setCookie(HTTPCookie, completionHandler: (() -> Void)?)](wkhttpcookiestore/setcookie(_:completionhandler:).md)
  Adds a cookie to the cookie store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkhttpcookiestore/delete(_:completionhandler:))*