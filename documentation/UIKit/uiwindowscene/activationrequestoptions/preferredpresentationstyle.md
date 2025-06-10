# preferredPresentationStyle

**Framework**: UIKit  
**Kind**: property

The presentation style of the window scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredPresentationStyle: UIWindowScene.PresentationStyle { get set }
```

#### Discussion

The presentation style determines how the system displays the new window scene relative to other scenes in the workspace. The default style is [`UIWindowScene.PresentationStyle.automatic`](uiwindowscene/presentationstyle/automatic.md).

## See Also

- [struct UIWindowSceneReplacePlacement](uiwindowscenereplaceplacement-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationrequestoptions/preferredpresentationstyle)*