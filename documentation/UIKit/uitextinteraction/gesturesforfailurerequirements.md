# gesturesForFailureRequirements

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The list of gestures that the text interaction adds to the view hierarchy.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var gesturesForFailureRequirements: [UIGestureRecognizer] { get }
```

```objc
@property (nonatomic, readonly) NSArray<UIGestureRecognizer *> * gesturesForFailureRequirements;
```

#### Discussion

If your app provides other gestures in the same view hierarchy, you may want to set up failure requirements between your app’s gestures and the gestures added by the text interaction. To do this, use the [`require(toFail:)`](../uigesturerecognizer/require%28tofail%29.md) method to relate your gestures to those listed in [`gesturesForFailureRequirements`](./gesturesforfailurerequirements.md).

## See Also

### Getting interaction information
- [var textInteractionMode: UITextInteractionMode](./textinteractionmode.md)
  The mode of the text interaction.
- [enum UITextInteractionMode](../uitextinteractionmode.md)
  Modes that determine the selection behaviors that a text interaction provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinteraction/gesturesforfailurerequirements)*