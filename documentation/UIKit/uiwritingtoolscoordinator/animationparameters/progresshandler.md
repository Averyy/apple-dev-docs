# progressHandler

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A custom block that runs at the same time as the system animations.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.4+

## Declaration

```swift
var progressHandler: ((Float) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^progressHandler)(float progress);
```

#### Discussion

If you have animations you want to run at the same time as the system animations, assign a block to this property and use it to run your animations. The block you provide must have no return value and take a floating-point value as a parameter. The parameter indicates the current progress of the animations as a percentage value between `0.0` to `1.0`. The system executes your block multiple times during the course of the animations, providing an updated completion value each time.

## See Also

### Creating custom animations
- [var completionHandler: (() -> Void)?](./completionhandler.md)
  A custom block to run when the system animations finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/animationparameters/progresshandler)*