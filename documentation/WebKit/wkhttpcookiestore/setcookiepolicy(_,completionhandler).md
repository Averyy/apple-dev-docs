# setCookiePolicy(_:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sets a cookie policy that indicates whether the cookie store allows cookie storage.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func setCookiePolicy(_ policy: WKHTTPCookieStore.CookiePolicy, completionHandler: (@MainActor @Sendable () -> Void)? = nil)
```

```swift
func setCookiePolicy(_ policy: WKHTTPCookieStore.CookiePolicy) async
```

```objc
- (void) setCookiePolicy:(WKCookiePolicy) policy completionHandler:(void (^)(void)) completionHandler;
```

## Parameters

- `policy`: A cookie policy that indicates whether the cookie store allows cookie storage.
- `completionHandler`: A block the system invokes after it sets the cookie policy.

## See Also

### Permitting cookie storage
- [func getCookiePolicy((WKHTTPCookieStore.CookiePolicy) -> Void)](./getcookiepolicy%28_%29.md)
  Returns a cookie policy that indicates whether the cookie store allows cookie storage.
- [WKHTTPCookieStore.CookiePolicy](./cookiepolicy.md)
  An enumeration with cases that indicate whether a cookie store allows cookie storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkhttpcookiestore/setcookiepolicy(_:completionhandler:))*