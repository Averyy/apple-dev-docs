# delegate

**Framework**: UIKit  
**Kind**: property

The object you use to receive life-cycle events associated with the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var delegate: (any UISceneDelegate)? { get set }
```

#### Discussion

The system creates a default delegate object based on the the class name you provide in your app’s `Info.plist` file, or that your app delegate specifies when configuring the scene. You can change this default delegate object later, as needed.

## See Also

- [protocol UISceneDelegate](uiscenedelegate.md)
  The core methods you use to respond to life-cycle events occurring within a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/delegate)*