# getCookiePolicy(_:)

**Framework**: Webkit  
**Kind**: method

Returns a cookie policy that indicates whether the cookie store allows cookie storage.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var cookiePolicy: WKHTTPCookieStore.CookiePolicy { get async }
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
var cookiePolicy: WKHTTPCookieStore.CookiePolicy { get async }
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
var cookiePolicy: WKHTTPCookieStore.CookiePolicy { get async }
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `completionHandler`: The completion handler block to execute asynchronously with the cookie policy. This block has no return value, and takes the following parameter:

## See Also

- [func setCookiePolicy(WKHTTPCookieStore.CookiePolicy, completionHandler: (() -> Void)?)](wkhttpcookiestore/setcookiepolicy(_:completionhandler:).md)
  Sets a cookie policy that indicates whether the cookie store allows cookie storage.
- [WKHTTPCookieStore.CookiePolicy](wkhttpcookiestore/cookiepolicy.md)
  An enumeration with cases that indicate whether a cookie store allows cookie storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkhttpcookiestore/getcookiepolicy(_:))*