# displayName

**Framework**: USDKit  
**Kind**: property  
**Role**: Instance Property

A human-readable name for the layer, derived from its identifier. Suitable for display in UI.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var displayName: String { get }
```

## See Also

### Inspecting identity and state
- [var identifier: String](./identifier.md)
  The layer’s identifier — typically a file path, URL, or anonymous identifier string. Identifies the layer in OpenUSD’s global registry.
- [var resolvedPath: FilePath?](./resolvedpath.md)
  The resolved filesystem location of the layer’s source, or `nil` for anonymous layers.
- [var isAnonymous: Bool](./isanonymous.md)
  Whether the layer is anonymous (in-memory, no file backing).
- [var isValid: Bool](./isvalid.md)
  Whether the layer is still valid. Returns `false` if the underlying data has been released.
- [var isDirty: Bool](./isdirty.md)
  Whether the layer has unsaved changes.
- [var isMuted: Bool](./ismuted.md)
  Whether the layer is muted from composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/displayname)*