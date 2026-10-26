# UIWindowScenePlacement

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

The placement of a window scene in the workspace.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
@interface UIWindowScenePlacement : NSObject
```

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [UIWindowSceneProminentPlacement](./uiwindowsceneprominentplacement-c.class.md)
- [UIWindowScenePushPlacement](./uiwindowscenepushplacement-c.class.md)
- [UIWindowSceneReplacePlacement](./uiwindowscenereplaceplacement-c.class.md)
- [UIWindowSceneStandardPlacement](./uiwindowscenestandardplacement-c.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Positioning windows
- [placement](./uiwindowsceneactivationrequestoptions/placement.md)
  The placement you prefer when the system activates the window scene.
- [UIWindowSceneProminentPlacement](./uiwindowsceneprominentplacement-c.class.md)
  A placement that indicates the system should present the window more prominently than others in the space.
- [UIWindowSceneStandardPlacement](./uiwindowscenestandardplacement-c.class.md)
  A placement that indicates the system should present the window using the default style of the system in the space.
- [UIWindowScenePushPlacement](./uiwindowscenepushplacement-c.class.md)
  A placement that indicates the system needs to present the window by pushing it onto another window.
- [var preferredPresentationStyle: UIWindowScene.PresentationStyle](./uiwindowscene/activationrequestoptions/preferredpresentationstyle.md)
  The presentation style of the window scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowsceneplacement-c.class)*