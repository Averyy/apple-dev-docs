# supportsAdaptiveImageGlyph

**Framework**: WebKit  
**Kind**: property

Indicates whether insertion of adaptive image glyphs is allowed.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
var supportsAdaptiveImageGlyph: Bool
```

#### Discussion

The default value is `false`. If `false`, adaptive image glyphs are inserted as regular images. If `true`, they are inserted with the full adaptive sizing behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/configuration/supportsadaptiveimageglyph)*