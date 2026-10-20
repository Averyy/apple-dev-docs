# setCookies(_:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setCookies(_ cookies: [HTTPCookie], completionHandler: (@MainActor @Sendable () -> Void)? = nil)
```

```swift
func setCookies(_ cookies: [HTTPCookie]) async
```

```objc
- (void) setCookies:(NSArray<NSHTTPCookie *> *) cookies completionHandler:(void (^)(void)) completionHandler;
```

#### Discussion

Set multiple cookies.

## Parameters

- `cookies`: An array of cookies to set.
- `completionHandler`: A block to invoke once the cookies have been stored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkhttpcookiestore/setcookies(_:completionhandler:))*