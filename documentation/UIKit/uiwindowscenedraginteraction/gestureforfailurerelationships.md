# gestureForFailureRelationships

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The gesture that the drag interaction adds to the view hierarchy.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
var gestureForFailureRelationships: UIGestureRecognizer { get }
```

```objc
@property (nonatomic, readonly) UIGestureRecognizer * gestureForFailureRelationships;
```

#### Discussion

If your app provides other gestures in the same view hierarchy, you may want to set up failure requirements between your app’s gestures and the drag interaction’s gesture. To do this, use the [`require(toFail:)`](../uigesturerecognizer/require%28tofail%29.md) method to relate your gestures to this gesture. For example:

**Swift**:

```swift
windowDragInteraction.gestureForFailureRelationships.require(toFail: swipeGesture)
```

**Objective-C**:

```objc
[windowDragInteraction.gestureForFailureRelationships requireGestureRecognizerToFail:self.swipeGesture];
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscenedraginteraction/gestureforfailurerelationships)*