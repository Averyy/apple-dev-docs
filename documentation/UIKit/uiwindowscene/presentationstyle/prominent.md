# UIWindowScene.PresentationStyle.prominent

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

Presents prominently above others in the current space.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- tvOS 15.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: For more information, see [`UIWindowScene.PresentationStyle`](../presentationstyle.md).

## Declaration

```swift
case prominent
```

```c
UIWindowScenePresentationStyleProminent
```

#### Discussion

On iPad, the system displays the window scene modally, centered and elevated above the existing workspace. You should dedicate the scene to specific content within your app, like a document or file, and include buttons to close the scene.

## See Also

### Constants
- [UIWindowScene.PresentationStyle.automatic](./automatic.md)
  The system determines the most appropriate style.
- [UIWindowScene.PresentationStyle.standard](./standard.md)
  The default style of the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/presentationstyle/prominent)*