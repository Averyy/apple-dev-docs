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
var preferredPresentationStyle: UIWindowScene.PresentationStyle { get set }
```

#### Discussion

The presentation style determines how the system displays the new window scene relative to other scenes in the workspace. The default style is [`UIWindowScene.PresentationStyle.automatic`](uiwindowscene/presentationstyle/automatic.md).

## See Also

- [var placement: (any UIWindowScenePlacement)?](uiwindowscene/activationrequestoptions/placement.md)
  The placement you prefer when the system activates the window scene.
- [protocol UIWindowScenePlacement](uiwindowsceneplacement-swift.protocol.md)
  The placement of a window scene in the workspace.
- [struct UIWindowSceneProminentPlacement](uiwindowsceneprominentplacement-swift.struct.md)
  A placement that indicates the system should present the window more prominently than others in the space.
- [struct UIWindowSceneStandardPlacement](uiwindowscenestandardplacement-swift.struct.md)
  A placement that indicates the system should present the window using the default style of the system in the space.
- [struct UIWindowScenePushPlacement](uiwindowscenepushplacement-swift.struct.md)
  A placement that indicates the system needs to present the window by pushing it onto another window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/activationrequestoptions/preferredpresentationstyle)*