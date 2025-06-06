# PartResult

**Framework**: hvf  
**Kind**: enum

The result returned from a part loader

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
enum PartResult
```

## Topics

### Enumeration Cases
- [case composite(any CompositeWriter)](partresult/composite(_:).md)
  The result is a Composite; data is in the CompositeWriter
- [PartResult.notFound](partresult/notfound.md)
  The requested part number was not found
- [case shape(any ShapeWriter)](partresult/shape(_:).md)
  The result is a Shape; data is in the ShapeWriter


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partresult)*