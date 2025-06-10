# getAllCookies(_:)

**Framework**: WebKit  
**Kind**: method

Fetches all stored cookies asynchronously and delivers them to the specified completion handler.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func allCookies() async -> [HTTPCookie]
```

#### Discussion

Use this method to get the set of cookies currently associated with your web view. Iterate over the contents of the provided array to retrieve the specific cookie you need for your code.

## Parameters

- `completionHandler`: A completion handler block to execute asynchronously with the results. This block has no return value and takes the following parameter:

## See Also

- [func setCookie(HTTPCookie, completionHandler: (() -> Void)?)](wkhttpcookiestore/setcookie(_:completionhandler:).md)
  Adds a cookie to the cookie store.
- [func delete(HTTPCookie, completionHandler: (() -> Void)?)](wkhttpcookiestore/delete(_:completionhandler:).md)
  Deletes the specified cookie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkhttpcookiestore/getallcookies(_:))*