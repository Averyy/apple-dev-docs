# setCookies(_:completionHandler:)

**Framework**: WebKit  
**Kind**: method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
func setCookies(_ cookies: [HTTPCookie]) async
```

#### Discussion

Set multiple cookies.

## Parameters

- `cookies`: An array of cookies to set.
- `completionHandler`: A block to invoke once the cookies have been stored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkhttpcookiestore/setcookies(_:completionhandler:))*