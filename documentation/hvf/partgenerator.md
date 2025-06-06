# PartGenerator

**Framework**: hvf  
**Kind**: protocol

Protocol for returning a writer object to create Shape or Composite data

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
protocol PartGenerator
```

## Topics

### Instance Methods
- [func makeComposite(Int) -> any CompositeWriter](partgenerator/makecomposite(_:).md)
  Create a new Composite, and return a CompositeWriter to fill it in
- [func makeShape(Int) -> any ShapeWriter](partgenerator/makeshape(_:).md)
  Create a new Shape, and return a ShapeWriter to fill it in


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partgenerator)*