# addBuffer(_:name:contentWorld:)

**Framework**: WebKit  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func addBuffer(_ buffer: Data, name: String, contentWorld world: WKContentWorld)
```

#### Discussion

Adds a data buffer that will be available to JavaScript through the `window.webkit.buffers` object

## Parameters

- `buffer`: The buffer to add.
- `name`: The name of the buffer to be referenced from JavaScript. e.g. with a `name` parameter of `@"mybuffer"`, JavaScript can reference the buffer via `window.webkit.buffers.mybuffer`


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/addbuffer(_:name:contentworld:))*