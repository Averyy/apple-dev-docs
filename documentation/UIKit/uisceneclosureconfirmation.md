# UISceneClosureConfirmation

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A configuration specifying a confirmation dialog that will be shown before a user action will result in destruction of the scene session and the disconnection of the scene.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
class UISceneClosureConfirmation
```

```objc
@interface UISceneClosureConfirmation : NSObject
```

## Overview

By default, the confirmation dialog includes a “Close” button (which closes the scene) and a “Cancel” button (which keeps the scene open). You can replace either of these default buttons by providing custom actions. Use a `UIAlertAction` with style `.destructive` to replace the “Close” button, or style `.cancel` to replace the “Cancel” button.

Example:

A property of this type is found on `UIWindowScene`. A scene setting its `closureConfirmation` may look something like

```
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
- [init?(coder: NSCoder)](./uisceneclosureconfirmation/init%28coder%29.md)
- [convenience init(title: String?, message: String?, actions: [UIAlertAction])](./uisceneclosureconfirmation/init%28title,message,actions%29.md)
  Creates a scene closure confirmation with the provided parameters.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Activation and destruction
- [class UISceneActivationConditions](./uisceneactivationconditions.md)
  The set of conditions that define when UIKit activates the current scene.
- [UIScene.ActivationRequestOptions](./uiscene/activationrequestoptions.md)
  An object that contains information you want the system to use when activating the session associated with a scene.
- [class UIWindowSceneDestructionRequestOptions](./uiwindowscenedestructionrequestoptions.md)
  An object that contains information to use when removing a window scene from your app.
- [class UISceneDestructionRequestOptions](./uiscenedestructionrequestoptions.md)
  An object you pass to UIKit to permanently remove a scene and its associated session from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneclosureconfirmation)*