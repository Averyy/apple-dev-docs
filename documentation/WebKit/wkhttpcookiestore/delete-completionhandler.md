# delete(_:completionHandler:)

**Framework**: Webkit  
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

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func deleteCookie(_ cookie: HTTPCookie) async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func deleteCookie(_ cookie: HTTPCookie) async
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

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