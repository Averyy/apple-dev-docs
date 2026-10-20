# RecognizedItem.Bounds

**Framework**: VisionKit  
**Kind**: struct  
**Role**: Structure

An object that represents the four corners of a recognized item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct Bounds
```

## Topics

### Getting the corners of items
- [var topLeft: CGPoint](./bounds-swift.struct/topleft.md)
  The upper-left corner of the recognized item in view coordinates.
- [var topRight: CGPoint](./bounds-swift.struct/topright.md)
  The upper-right corner of the recognized item in view coordinates.
- [var bottomRight: CGPoint](./bounds-swift.struct/bottomright.md)
  The lower-right corner of the recognized item in view coordinates.
- [var bottomLeft: CGPoint](./bounds-swift.struct/bottomleft.md)
  The lower-left corner of the recognized item in view coordinates.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Item location
- [var bounds: RecognizedItem.Bounds](./bounds-swift.property.md)
  The four corners of the recognized item in view coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/recognizeditem/bounds-swift.struct)*