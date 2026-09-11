# removeBuffer(named:from:)

**Framework**: WebKit  
**Kind**: method

Removes a previously added data buffer from the given `WKContentWorld`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

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