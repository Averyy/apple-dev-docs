# prefersDirectTouchSystemGesturesDisabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Indicates that the view controller prefers to disable direct-touch system gestures that land on its scene.

**Availability**:
- Mac Catalyst 27.3+ (Beta)

## Declaration

```swift
var prefersDirectTouchSystemGesturesDisabled: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL prefersDirectTouchSystemGesturesDisabled;
```

## Discussion

> **Note**: This property indicates a preference; the system may or may not honor it.

Defaults to `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/prefersdirecttouchsystemgesturesdisabled)*