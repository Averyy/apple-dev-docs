# getCookies(for:completionHandler:)

**Framework**: WebKit  
**Kind**: method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func cookies(for url: URL) async -> [HTTPCookie]
```

#### Discussion

Fetches stored cookies that match the passed in URL.

## Parameters

- `url`: The URL to fetch the matching cookies for.
- `completionHandler`: A block to invoke with the fetched cookies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkhttpcookiestore/getcookies(for:completionhandler:))*