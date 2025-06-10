# UIWindowScene.PresentationStyle.prominent

**Framework**: UIKit  
**Kind**: case

Presents prominently above others in the current space.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
case prominent
```

#### Discussion

On iPad, the system displays the window scene modally, centered and elevated above the existing workspace. You should dedicate the scene to specific content within your app, like a document or file, and include buttons to close the scene.

## See Also

- [UIWindowScene.PresentationStyle.automatic](uiwindowscene/presentationstyle/automatic.md)
  The system determines the most appropriate style.
- [UIWindowScene.PresentationStyle.standard](uiwindowscene/presentationstyle/standard.md)
  The default style of the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/presentationstyle/prominent)*