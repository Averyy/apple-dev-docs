# gestureRecognizers

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The gesture recognizers that are receiving the touch object.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var gestureRecognizers: [UIGestureRecognizer]? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<UIGestureRecognizer *> * gestureRecognizers;
```

#### Discussion

The objects in the array are instances of a subclass of the abstract base class [`UIGestureRecognizer`](../uigesturerecognizer.md). If there are no gesture recognizers currently receiving the touch, this property contains an empty array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitouch/gesturerecognizers)*