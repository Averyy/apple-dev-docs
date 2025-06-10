# response

**Framework**: WebKit  
**Kind**: property

The frame’s response.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var response: URLResponse { get }
```

#### Discussion

Allowing a navigation response with a MIME type that WebKit can’t display causes the navigation to fail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wknavigationresponse/response)*