# contourAtIndex(_:)

**Framework**: Vision  
**Kind**: method

Retrieves the contour object at the specified index, irrespective of hierarchy.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func contourAtIndex(_ index: Int) -> ContoursObservation.Contour?
```

#### Return Value

The contour object at the specified index, or `nil` if the index is invalid.

## Parameters

- `index`: The index of the contour to retrieve. Valid values are in the range of   to  .

## See Also

- [ContoursObservation.Contour](contoursobservation/contour.md)
  An object that represents a detected contour in an image.
- [func countourAtIndexPath(IndexPath) -> ContoursObservation.Contour?](contoursobservation/countouratindexpath(_:).md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/contoursobservation/contouratindex(_:))*