# direction

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The orientation of the selection handle.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var direction: NSDirectionalRectEdge { get set }
```

```objc
@property (nonatomic, assign) NSDirectionalRectEdge direction;
```

#### Discussion

Specify [`leading`](../nsdirectionalrectedge/leading.md) if this view represents the leading selection handle or [`trailing`](../nsdirectionalrectedge/trailing.md) if it represents the trailing selection handle. The system uses this information to determine where to differentiate the selection handles visually.

## See Also

### Specifying the handle details
- [var customShape: UIBezierPath?](./customshape.md)
  The custom shape to draw for the stem of the selection handle.
- [var isVertical: Bool](./isvertical.md)
  Convenience accessor for @c direction calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextselectionhandleview/direction)*