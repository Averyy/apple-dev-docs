# setCookie(_:completionHandler:)

**Framework**: Webkit  
**Kind**: method

Adds a cookie to the cookie store.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setCookie(_ cookie: HTTPCookie) async
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func setCookie(_ cookie: HTTPCookie) async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func setCookie(_ cookie: HTTPCookie) async
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `cookie`: The cookie to add.
- `completionHandler`: A completion handler block to execute asynchronously after the method successfully stores the cookie. This block has no return value and no parameters.

## See Also

- [func getAllCookies(([HTTPCookie]) -> Void)](wkhttpcookiestore/getallcookies(_:).md)
  Fetches all stored cookies asynchronously and delivers them to the specified completion handler.
- [func delete(HTTPCookie, completionHandler: (() -> Void)?)](wkhttpcookiestore/delete(_:completionhandler:).md)
  Deletes the specified cookie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkhttpcookiestore/setcookie(_:completionhandler:))*