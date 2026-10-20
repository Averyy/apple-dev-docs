# insert(_:replacementRange:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Inserts an adaptive image into the text at the specifed location.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
optional func insert(_ adaptiveImageGlyph: NSAdaptiveImageGlyph, replacementRange: UITextRange)
```

```objc
- (void) insertAdaptiveImageGlyph:(NSAdaptiveImageGlyph *) adaptiveImageGlyph replacementRange:(UITextRange *) replacementRange;
```

## Parameters

- `adaptiveImageGlyph`: The adaptive image to add to the text.
- `replacementRange`: The text range at which to insert the image.

## See Also

### Supporting adaptive images
- [var supportsAdaptiveImageGlyph: Bool](./supportsadaptiveimageglyph.md)
  A Boolean value that indicates whether the document supports adaptive images in the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/insert(_:replacementrange:))*