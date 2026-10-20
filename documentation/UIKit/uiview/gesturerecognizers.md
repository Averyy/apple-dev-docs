# gestureRecognizers

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The gesture-recognizer objects currently attached to the view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var gestureRecognizers: [UIGestureRecognizer]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<__kindof UIGestureRecognizer *> * gestureRecognizers;
```

#### Discussion

Each of these objects is an instance of a subclass of the abstract base class [`UIGestureRecognizer`](../uigesturerecognizer.md). The default value of this property is `nil`. If you add a gesture recognizer and then remove it, the value of the property is an empty array.

## See Also

### Managing gesture recognizers
- [func addGestureRecognizer(UIGestureRecognizer)](./addgesturerecognizer%28_%29.md)
  Attaches a gesture recognizer to the view.
- [func removeGestureRecognizer(UIGestureRecognizer)](./removegesturerecognizer%28_%29.md)
  Detaches a gesture recognizer from the receiving view.
- [func gestureRecognizerShouldBegin(UIGestureRecognizer) -> Bool](./gesturerecognizershouldbegin%28_%29.md)
  Asks the view if the gesture recognizer should continue tracking touch events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/gesturerecognizers)*