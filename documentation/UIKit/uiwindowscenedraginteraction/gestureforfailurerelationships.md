# gestureForFailureRelationships

**Framework**: UIKit  
**Kind**: property

The gesture that the drag interaction adds to the view hierarchy.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var gestureForFailureRelationships: UIGestureRecognizer { get }
```

#### Discussion

If your app provides other gestures in the same view hierarchy, you may want to set up failure requirements between your app’s gestures and the drag interaction’s gesture. To do this, use the [`require(toFail:)`](uigesturerecognizer/require(tofail:).md) method to relate your gestures to this gesture. For example:


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscenedraginteraction/gestureforfailurerelationships)*