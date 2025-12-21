# getCookiePolicy(_:)

**Framework**: WebKit  
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

## Parameters

- `completionHandler`: The completion handler block to execute asynchronously with the cookie policy. This block has no return value, and takes the following parameter:

## See Also

- [func setCookiePolicy(WKHTTPCookieStore.CookiePolicy, completionHandler: (() -> Void)?)](wkhttpcookiestore/setcookiepolicy(_:completionhandler:).md)
  Sets a cookie policy that indicates whether the cookie store allows cookie storage.
- [WKHTTPCookieStore.CookiePolicy](wkhttpcookiestore/cookiepolicy.md)
  An enumeration with cases that indicate whether a cookie store allows cookie storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkhttpcookiestore/getcookiepolicy(_:))*