# childForDirectTouchSystemGesturesDisabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A child view controller to query for the preference to disable direct-touch system gestures.

**Availability**:
- Mac Catalyst 27.3+ (Beta)

## Declaration

```swift
var childForDirectTouchSystemGesturesDisabled: UIViewController? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UIViewController * childViewControllerForDirectTouchSystemGesturesDisabled;
```

## Discussion

Return `nil` to use the receiver as the view controller to query. Defaults to `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/childfordirecttouchsystemgesturesdisabled)*