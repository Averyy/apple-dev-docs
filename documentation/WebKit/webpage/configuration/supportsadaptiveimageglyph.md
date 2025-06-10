# supportsAdaptiveImageGlyph

**Framework**: WebKit  
**Kind**: property

Indicates whether insertion of adaptive image glyphs is allowed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var supportsAdaptiveImageGlyph: Bool
```

#### Discussion

The default value is `false`. If `false`, adaptive image glyphs are inserted as regular images. If `true`, they are inserted with the full adaptive sizing behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/configuration/supportsadaptiveimageglyph)*