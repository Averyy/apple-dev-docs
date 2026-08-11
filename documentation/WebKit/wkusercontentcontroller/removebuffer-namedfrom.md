# removeBuffer(named:from:)

**Framework**: WebKit  
**Kind**: method

Removes a previously added data buffer from the given `WKContentWorld`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func removeBuffer(named name: String, from contentWorld: WKContentWorld)
```

## Parameters

- `name`: The name of the buffer to remove.
- `contentWorld`: The `WKContentWorld` from which to remove the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/removebuffer(named:from:))*