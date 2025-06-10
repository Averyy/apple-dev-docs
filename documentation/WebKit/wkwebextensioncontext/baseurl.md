# baseURL

**Framework**: WebKit  
**Kind**: property

The base URL the context uses for loading extension resources or injecting content into webpages.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var baseURL: URL { get set }
```

#### Discussion

The default value is a unique URL using the `webkit-extension` scheme. The base URL can be set to any URL, but only the scheme and host will be used. The scheme cannot be a scheme that is already supported by [`WKWebView`](wkwebview.md) (e.g. http, https, etc.). Setting is only allowed when the context is not loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontext/baseurl)*