# supportsAdaptiveImageGlyph

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the document supports adaptive images in the input.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
optional var supportsAdaptiveImageGlyph: Bool { get set }
```

#### Discussion

When this property is [`false`](https://developer.apple.com/documentation/swift/false), the input system doesn’t allow the text input to contain adaptive images. Set the value of this property to [`true`](https://developer.apple.com/documentation/swift/true) only if your document supports adaptive images and handles them properly. For more information, see [`NSAdaptiveImageGlyph`](nsadaptiveimageglyph.md)

## See Also

- [func insert(NSAdaptiveImageGlyph, replacementRange: UITextRange)](uitextinput/insert(_:replacementrange:).md)
  Inserts an adaptive image into the text at the specifed location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/supportsadaptiveimageglyph)*