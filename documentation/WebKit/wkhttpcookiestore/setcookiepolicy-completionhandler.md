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