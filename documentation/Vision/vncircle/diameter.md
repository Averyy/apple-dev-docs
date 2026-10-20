# diameter

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The circle’s diameter.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var diameter: Double { get }
```

```objc
@property (readonly) double diameter;
```

## See Also

### Inspecting a Circle
- [var center: VNPoint](./center.md)
  The circle’s center point.
- [var radius: Double](./radius.md)
  The circle’s radius.
- [func contains(VNPoint) -> Bool](./contains%28_%29.md)
  Determines if this circle, including its boundary, contains the specified point.
- [func contains(VNPoint, inCircumferentialRingOfWidth: Double) -> Bool](./contains%28_,incircumferentialringofwidth%29.md)
  Determines if a ring around this circle’s circumference contains the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vncircle/diameter)*