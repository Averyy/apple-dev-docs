# contains(_:)

**Framework**: Vision  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/Foundation/NSExpression/true) if the point is contained within this circle, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `point`: The point to test.

## See Also

- [var center: VNPoint](vncircle/center.md)
  The circle’s center point.
- [var diameter: Double](vncircle/diameter.md)
  The circle’s diameter.
- [var radius: Double](vncircle/radius.md)
  The circle’s radius.
- [func contains(VNPoint, inCircumferentialRingOfWidth: Double) -> Bool](vncircle/contains(_:incircumferentialringofwidth:).md)
  Determines if a ring around this circle’s circumference contains the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncircle/contains(_:))*