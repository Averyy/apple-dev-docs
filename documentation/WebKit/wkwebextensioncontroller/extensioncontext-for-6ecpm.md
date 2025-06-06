# extensionContext(for:)

**Framework**: Webkit  
**Kind**: method

Returns a loaded extension context for the specified extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func extensionContext(for extension: WKWebExtension) -> WKWebExtensionContext?
```

#### Return Value

An extension context or `nil` if no match was found.

## Parameters

- `extension`: An extension to lookup.

## See Also

- [var extensions: Set<WKWebExtension>](wkwebextensioncontroller/extensions.md)
  A set of all the currently loaded extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/extensioncontext(for:)-6ecpm)*