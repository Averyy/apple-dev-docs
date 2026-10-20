# getCookiePolicy(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns a cookie policy that indicates whether the cookie store allows cookie storage.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func getCookiePolicy(_ completionHandler: @escaping @MainActor @Sendable (WKHTTPCookieStore.CookiePolicy) -> Void)
```

```swift
var cookiePolicy: WKHTTPCookieStore.CookiePolicy { get async }
```

```objc
- (void) getCookiePolicy:(void (^)(enum WKCookiePolicy)) completionHandler;
```

## Parameters

- `completionHandler`: The completion handler block to execute asynchronously with the cookie policy. This block has no return value, and takes the following parameter:

  - **cookiePolicy**: A [`WKHTTPCookieStore.CookiePolicy`](./cookiepolicy.md) case that indicates whether the cookie store allows cookie storage.

## See Also

### Permitting cookie storage
- [func setCookiePolicy(WKHTTPCookieStore.CookiePolicy, completionHandler: (() -> Void)?)](./setcookiepolicy%28_,completionhandler%29.md)
  Sets a cookie policy that indicates whether the cookie store allows cookie storage.
- [WKHTTPCookieStore.CookiePolicy](./cookiepolicy.md)
  An enumeration with cases that indicate whether a cookie store allows cookie storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkhttpcookiestore/getcookiepolicy(_:))*