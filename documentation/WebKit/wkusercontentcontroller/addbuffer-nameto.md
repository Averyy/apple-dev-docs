# addBuffer(_:name:to:)

**Framework**: WebKit  
**Kind**: method

Adds a data buffer that will be available to JavaScript through the `window.webkit.buffers` object.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func addBuffer(_ buffer: RawSpan, name: String, to contentWorld: WKContentWorld)
```

## Parameters

- `buffer`: The buffer to add.
- `name`: The name of the buffer to be referenced from JavaScript. e.g. with a `name` parameter of `"mybuffer"`, JavaScript can reference the buffer via `window.webkit.buffers.mybuffer`.
- `contentWorld`: The `WKContentWorld` to add the buffer to. The buffer will only be visible to JavaScript executing in that content world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/addbuffer(_:name:to:))*