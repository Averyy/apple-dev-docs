# PartRenderer.AxisValues

**Framework**: hvf  
**Kind**: class

All the axis values applied to a part. The index is the axis number (determined by the loader). Axis values are in design space (-1.0…1.0)

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
class AxisValues
```

## Topics

### Instance Properties
- [var isNested: Bool](partrenderer/axisvalues/isnested.md)
  Whether the axis values apply to a nested subpart or not
### Instance Methods
- [func blendedValue(axis: Int) -> Double](partrenderer/axisvalues/blendedvalue(axis:).md)
  The final axis values applied to this subpart after the part has been rendered This is useful for detecting axes going out of range (-1.0…1.0)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partrenderer/axisvalues)*