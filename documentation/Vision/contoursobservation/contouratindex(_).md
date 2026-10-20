# contourAtIndex(_:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Retrieves the contour object at the specified index, irrespective of hierarchy.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
func contourAtIndex(_ index: Int) -> ContoursObservation.Contour?
```

#### Return Value

The contour object at the specified index, or `nil` if the index is invalid.

## Parameters

- `index`: The index of the contour to retrieve. Valid values are in the range of `0` to `contourCount - 1`.

## See Also

### Getting the contours
- [ContoursObservation.Contour](./contour.md)
  An object that represents a detected contour in an image.
- [func countourAtIndexPath(IndexPath) -> ContoursObservation.Contour?](./countouratindexpath%28_%29.md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/contoursobservation/contouratindex(_:))*