# navigationTransitionMetric

**Framework**: XCTest  
**Kind**: property  
**Role**: Type Property

A metric that records the duration of navigation transitions between views.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class var navigationTransitionMetric: any XCTMetric { get }
```

```objc
@property (class, readonly) id<XCTMetric> navigationTransitionMetric;
```

## See Also

### Measuring Navigation Transitions
- [class var customNavigationTransitionMetric: any XCTMetric](./customnavigationtransitionmetric.md)
  A metric that records the duration of custom navigation transitions between views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctossignpostmetric/navigationtransitionmetric)*