# WKHTTPCookieStore.CookiePolicy

**Framework**: Webkit  
**Kind**: enum

An enumeration with cases that indicate whether a cookie store allows cookie storage.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum CookiePolicy
```

## Topics

### Specifying a cookie policy
- [WKHTTPCookieStore.CookiePolicy.allow](wkhttpcookiestore/cookiepolicy/allow.md)
  A case that indicates the cookie store allows cookie storage.
- [WKHTTPCookieStore.CookiePolicy.disallow](wkhttpcookiestore/cookiepolicy/disallow.md)
  A case that indicates the cookie store does not allow cookie storage.
### Initializers
- [init?(rawValue: Int)](wkhttpcookiestore/cookiepolicy/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func getCookiePolicy((WKHTTPCookieStore.CookiePolicy) -> Void)](wkhttpcookiestore/getcookiepolicy(_:).md)
  Returns a cookie policy that indicates whether the cookie store allows cookie storage.
- [func setCookiePolicy(WKHTTPCookieStore.CookiePolicy, completionHandler: (() -> Void)?)](wkhttpcookiestore/setcookiepolicy(_:completionhandler:).md)
  Sets a cookie policy that indicates whether the cookie store allows cookie storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkhttpcookiestore/cookiepolicy)*