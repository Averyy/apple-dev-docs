# contains(_:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Determines if this circle, including its boundary, contains the specified point.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func contains(_ point: VNPoint) -> Bool
```

```objc
- (BOOL) containsPoint:(VNPoint *) point;
```

#### Return Value

[`true`](../../Foundation/nsexpression/true.md) if the point is contained within this circle, otherwise [`false`](../../Swift/false.md).

## Parameters

- `point`: The point to test.

## See Also

### Inspecting a Circle
- [var center: VNPoint](./center.md)
  The circle’s center point.
- [var diameter: Double](./diameter.md)
  The circle’s diameter.
- [var radius: Double](./radius.md)
  The circle’s radius.
- [func contains(VNPoint, inCircumferentialRingOfWidth: Double) -> Bool](./contains%28_,incircumferentialringofwidth%29.md)
  Determines if a ring around this circle’s circumference contains the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncircle/contains(_:))*