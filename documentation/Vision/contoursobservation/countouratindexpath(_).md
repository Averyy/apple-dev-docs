# countourAtIndexPath(_:)

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
func countourAtIndexPath(_ indexPath: IndexPath) -> ContoursObservation.Contour?
```

## Return Value

The contour object at the specified index path, or `nil` if the index path is invalid.

## Parameters

- `indexPath`: The index of the contour to retrieve. Valid values are in the range of `0` to `contourCount - 1`.

## See Also

### Getting the contours
- [ContoursObservation.Contour](./contour.md)
  An object that represents a detected contour in an image.
- [func contourAtIndex(Int) -> ContoursObservation.Contour?](./contouratindex%28_%29.md)
  Retrieves the contour object at the specified index, irrespective of hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/contoursobservation/countouratindexpath(_:))*