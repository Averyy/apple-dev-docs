# displayName

**Framework**: USDKit  
**Kind**: property

A human-readable name for the layer, derived from its identifier. Suitable for display in UI.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var displayName: String { get }
```

## See Also

- [var identifier: String](usdlayer/identifier.md)
  The layer’s identifier — typically a file path, URL, or anonymous identifier string. Identifies the layer in OpenUSD’s global registry.
- [var resolvedPath: FilePath?](usdlayer/resolvedpath.md)
  The resolved filesystem location of the layer’s source, or `nil` for anonymous layers.
- [var isAnonymous: Bool](usdlayer/isanonymous.md)
  Whether the layer is anonymous (in-memory, no file backing).
- [var isValid: Bool](usdlayer/isvalid.md)
  Whether the layer is still valid. Returns `false` if the underlying data has been released.
- [var isDirty: Bool](usdlayer/isdirty.md)
  Whether the layer has unsaved changes.
- [var isMuted: Bool](usdlayer/ismuted.md)
  Whether the layer is muted from composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/displayname)*