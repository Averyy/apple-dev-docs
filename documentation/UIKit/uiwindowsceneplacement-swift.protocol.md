# UIWindowScenePlacement

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The placement of a window scene in the workspace.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS

## Declaration

```swift
protocol UIWindowScenePlacement : Hashable
```

## Topics

### Positioning windows
- [static func prominent() -> Self](./uiwindowsceneplacement-swift.protocol/prominent%28%29.md)
  Creates a placement that indicates the system should present the window more prominently than others in the space.
- [static func standard() -> Self](./uiwindowsceneplacement-swift.protocol/standard%28%29.md)
  Creates a placement that indicates the system should present the window using the default style of the system in the space.
### Type Methods
- [static func push(onto: UISceneSession) -> Self](./uiwindowsceneplacement-swift.protocol/push%28onto%29.md)
- [static func replacing(UISceneSession) -> Self](./uiwindowsceneplacement-swift.protocol/replacing%28_%29.md)

## Relationships

### Inherits From
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
### Conforming Types
- [UIWindowSceneProminentPlacement](./uiwindowsceneprominentplacement-swift.struct.md)
- [UIWindowScenePushPlacement](./uiwindowscenepushplacement-swift.struct.md)
- [UIWindowSceneReplacePlacement](./uiwindowscenereplaceplacement-swift.struct.md)
- [UIWindowSceneStandardPlacement](./uiwindowscenestandardplacement-swift.struct.md)

## See Also

### Positioning windows
- [var placement: (any UIWindowScenePlacement)?](./uiwindowscene/activationrequestoptions/placement.md)
  The placement you prefer when the system activates the window scene.
- [struct UIWindowSceneProminentPlacement](./uiwindowsceneprominentplacement-swift.struct.md)
  A placement that indicates the system should present the window more prominently than others in the space.
- [struct UIWindowSceneStandardPlacement](./uiwindowscenestandardplacement-swift.struct.md)
  A placement that indicates the system should present the window using the default style of the system in the space.
- [struct UIWindowScenePushPlacement](./uiwindowscenepushplacement-swift.struct.md)
  A placement that indicates the system needs to present the window by pushing it onto another window.
- [var preferredPresentationStyle: UIWindowScene.PresentationStyle](./uiwindowscene/activationrequestoptions/preferredpresentationstyle.md)
  The presentation style of the window scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowsceneplacement-swift.protocol)*