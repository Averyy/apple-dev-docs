# load(_:)

**Framework**: WebKit  
**Kind**: method

Loads the specified extension context.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func load(_ extensionContext: WKWebExtensionContext) throws
```

#### Discussion

Causes the context to start, loading any background content, and injecting any content into relevant tabs.

## See Also

- [func load(WKWebExtensionContext) throws](wkwebextensioncontroller/load(_:).md)
  Loads the specified extension context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/load(_:))*