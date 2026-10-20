# focusSystem

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The focus system that’s responsible for the window scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var focusSystem: UIFocusSystem? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIFocusSystem * focusSystem;
```

#### Discussion

The value of this property is `nil` if the window scene doesn’t support focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/focussystem)*