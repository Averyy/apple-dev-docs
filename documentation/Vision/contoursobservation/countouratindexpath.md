# countourAtIndexPath(_:)

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
func countourAtIndexPath(_ indexPath: IndexPath) -> ContoursObservation.Contour?
```

#### Return Value

The contour object at the specified index path, or `nil` if the index path is invalid.

## Parameters

- `indexPath`: The index of the contour to retrieve. Valid values are in the range of   to  .

## See Also

- [ContoursObservation.Contour](contoursobservation/contour.md)
  An object that represents a detected contour in an image.
- [func contourAtIndex(Int) -> ContoursObservation.Contour?](contoursobservation/contouratindex(_:).md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/contoursobservation/countouratindexpath(_:))*