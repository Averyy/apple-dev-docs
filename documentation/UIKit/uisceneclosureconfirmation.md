# UISceneClosureConfirmation

**Framework**: UIKit  
**Kind**: class

A configuration specifying a confirmation dialog that will be shown before a user action will result in destruction of the scene session and the disconnection of the scene.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
class UISceneClosureConfirmation
```

#### Overview

By default, the confirmation dialog includes a “Close” button (which closes the scene) and a “Cancel” button (which keeps the scene open). You can replace either of these default buttons by providing custom actions. Use a `UIAlertAction` with style `.destructive` to replace the “Close” button, or style `.cancel` to replace the “Cancel” button.

Example:

A property of this type is found on `UIWindowScene`. A scene setting its `closureConfirmation` may look something like

```None
let closeAction = UIAlertAction(title:"End meeting for all", style:.destructive, handler: nil)
let cancelAction = UIAlertAction(title:"Stay in meeting", style:.cancel, handler:nil)
let myAction = UIAlertAction(title:"Leave & Assign new host", style:.default) { action in
   // work to do before the window closes
}
var closureConfirmation: UISceneClosureConfirmation =
   UISceneClosureConfirmation(title:"Leave or End meeting?",
                              message:"You are the host. Would you like to end the meeting for all participants?",
                              actions:[closeAction, cancelAction, myAction])

windowScene.closureConfirmation = closureConfirmation
```

With this property set, upon user initiated close, the system will present the closure confirmation dialog.

## Topics

### Initializers
- [init?(coder: NSCoder)](uisceneclosureconfirmation/init(coder:).md)
- [convenience init(title: String?, message: String?, actions: [UIAlertAction])](uisceneclosureconfirmation/init(title:message:actions:).md)
  Creates a scene closure confirmation with the provided parameters.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UISceneActivationConditions](uisceneactivationconditions.md)
  The set of conditions that define when UIKit activates the current scene.
- [UIScene.ActivationRequestOptions](uiscene/activationrequestoptions.md)
  An object that contains information you want the system to use when activating the session associated with a scene.
- [class UIWindowSceneDestructionRequestOptions](uiwindowscenedestructionrequestoptions.md)
  An object that contains information to use when removing a window scene from your app.
- [class UISceneDestructionRequestOptions](uiscenedestructionrequestoptions.md)
  An object you pass to UIKit to permanently remove a scene and its associated session from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneclosureconfirmation)*