# edges

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The acceptable starting edges for the gesture.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var edges: UIRectEdge { get set }
```

```objc
@property (nonatomic, assign, readwrite) UIRectEdge edges;
```

## Mentions

- [Handling pan gestures](../handling-pan-gestures.md)

#### Discussion

The edges you specify are always relative to the app’s current interface orientation. This behavior ensures that the gestures always occur from the same place in your user interface, regardless of the device’s current orientation.

## See Also

### Specifying the starting edges
- [struct UIRectEdge](../uirectedge.md)
  Constants that specify the edges of a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreenedgepangesturerecognizer/edges)*