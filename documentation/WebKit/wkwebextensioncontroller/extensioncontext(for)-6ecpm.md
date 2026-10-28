# extensionContext(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns a loaded extension context for the specified extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
func extensionContext(for extension: WKWebExtension) -> WKWebExtensionContext?
```

```objc
- (WKWebExtensionContext *) extensionContextForExtension:(WKWebExtension *) extension;
```

## Return Value

An extension context or `nil` if no match was found.

## Parameters

- `extension`: An extension to lookup.

## See Also

### Related Documentation
- [var extensions: Set<WKWebExtension>](./extensions.md)
  A set of all the currently loaded extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextensioncontroller/extensioncontext(for:)-6ecpm)*