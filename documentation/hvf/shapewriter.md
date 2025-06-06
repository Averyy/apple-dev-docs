# ShapeWriter

**Framework**: hvf  
**Kind**: protocol

A protocol for creating a Shape part for rendering or to build an HVGL table

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
protocol ShapeWriter
```

## Topics

### Instance Properties
- [var axisCount: Int](shapewriter/axiscount.md)
  The number of axes
- [var blendTypes: [SegmentBlendType]](shapewriter/blendtypes.md)
  The blend type of each segment, in path order
- [var denseDeltaMatrix: [Double]](shapewriter/densedeltamatrix.md)
  A dense matrix of segment delta values for extrema, in column order. The columns correspond to the axis extrema, with minimum first, then maximum
- [var masterVector: [Double]](shapewriter/mastervector.md)
  The master point segments, in path order. Each segment is in the order: Curve: parallel factor, zero, off X, off Y Not curve: on X, on Y, off X, off Y
- [var pathSizes: [UInt16]](shapewriter/pathsizes.md)
  The number of segments in each path; must sum to totalSegmentCount
- [var totalSegmentCount: Int](shapewriter/totalsegmentcount.md)
  The total number of segments (on/off pairs) in all paths
### Instance Methods
- [func denseDeltaOffset(axis: Int, extremum: AxisExtremum, segment: Int, point: SegmentPoint, coordinate: PointCoordinate) -> Int](shapewriter/densedeltaoffset(axis:extremum:segment:point:coordinate:).md)
  The offset of a coordinate in the denseDeltaMatrix This function uses totalSegmentCount, which must be set correctly before calling
- [func finalize() -> Bool](shapewriter/finalize.md)
  Call when done writing the Shape
- [func masterOffset(segment: Int, point: SegmentPoint, coordinate: PointCoordinate) -> Int](shapewriter/masteroffset(segment:point:coordinate:).md)
  The offset of a coordinate in the masterVector


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/shapewriter)*