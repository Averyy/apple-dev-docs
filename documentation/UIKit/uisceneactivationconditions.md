# UISceneActivationConditions

**Framework**: UIKit  
**Kind**: class

The set of conditions that define when UIKit activates the current scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UISceneActivationConditions
```

#### Overview

When an event occurs that requires the activation of a scene, UIKit routes the event to the scene best suited to handle it. UIKit determines which scene is the best by evaluating the target content identifier of the event against the predicates in each scene’s [`UISceneActivationConditions`](uisceneactivationconditions.md) object. You create [`UISceneActivationConditions`](uisceneactivationconditions.md) objects for your scenes and use them to prioritize which events each scene handles. Use the [`prefersToActivateForTargetContentIdentifierPredicate`](uisceneactivationconditions/preferstoactivatefortargetcontentidentifierpredicate.md) predicate to designate the scene as the primary handler of an event.

Many different objects contain a [`targetContentIdentifier`](https://developer.apple.com/documentation/Foundation/NSUserActivity/targetContentIdentifier) property, including [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity), [`UNNotificationContent`](https://developer.apple.com/documentation/UserNotifications/UNNotificationContent), and [`UIApplicationShortcutItem`](uiapplicationshortcutitem.md). When creating those objects, fill that property with a value that uniquely describes the event and matches your scenes’ predicates. Every event must match at least one scene.

## Topics

### Creating an activation conditions object
- [init()](uisceneactivationconditions/init.md)
  Creates a new activation conditions object.
- [init?(coder: NSCoder)](uisceneactivationconditions/init(coder:).md)
  Restores an activation conditions object from the specified archive.
### Specifying the conditions
- [var prefersToActivateForTargetContentIdentifierPredicate: NSPredicate](uisceneactivationconditions/preferstoactivatefortargetcontentidentifierpredicate.md)
  The set of conditions for which UIKit chooses to activate this scene over others.
- [var canActivateForTargetContentIdentifierPredicate: NSPredicate](uisceneactivationconditions/canactivatefortargetcontentidentifierpredicate.md)
  Conditions for which UIKit can activate the scene if a better alternative doesn’t exist.

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
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [UIScene.ActivationRequestOptions](uiscene/activationrequestoptions.md)
  An object that contains information you want the system to use when activating the session associated with a scene.
- [class UIWindowSceneDestructionRequestOptions](uiwindowscenedestructionrequestoptions.md)
  An object that contains information to use when removing a window scene from your app.
- [class UISceneDestructionRequestOptions](uiscenedestructionrequestoptions.md)
  An object you pass to UIKit to permanently remove a scene and its associated session from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneactivationconditions)*