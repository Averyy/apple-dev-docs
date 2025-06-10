# setCookiePolicy(_:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Sets a cookie policy that indicates whether the cookie store allows cookie storage.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setCookiePolicy(_ policy: WKHTTPCookieStore.CookiePolicy) async
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func setCookiePolicy(_ policy: WKHTTPCookieStore.CookiePolicy) async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `policy`: A cookie policy that indicates whether the cookie store allows cookie storage.
- `completionHandler`: A block the system invokes after it sets the cookie policy.

## See Also

- [func getCookiePolicy((WKHTTPCookieStore.CookiePolicy) -> Void)](wkhttpcookiestore/getcookiepolicy(_:).md)
  Returns a cookie policy that indicates whether the cookie store allows cookie storage.
- [WKHTTPCookieStore.CookiePolicy](wkhttpcookiestore/cookiepolicy.md)
  An enumeration with cases that indicate whether a cookie store allows cookie storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkhttpcookiestore/setcookiepolicy(_:completionhandler:))*