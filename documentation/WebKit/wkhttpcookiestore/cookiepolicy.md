# WKHTTPCookieStore.CookiePolicy

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum WKCookiePolicy : NSInteger;
```

## Topics

### Specifying a cookie policy
- [WKHTTPCookieStore.CookiePolicy.allow](./cookiepolicy/allow.md)
  A case that indicates the cookie store allows cookie storage.
- [WKHTTPCookieStore.CookiePolicy.disallow](./cookiepolicy/disallow.md)
  A case that indicates the cookie store does not allow cookie storage.
### Initializers
- [init?(rawValue: Int)](./cookiepolicy/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkhttpcookiestore/cookiepolicy)*