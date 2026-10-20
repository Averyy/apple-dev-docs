# prefersToActivateForTargetContentIdentifierPredicate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The set of conditions for which UIKit chooses to activate this scene over others.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var prefersToActivateForTargetContentIdentifierPredicate: NSPredicate { get set }
```

```objc
@property (nonatomic, copy) NSPredicate * prefersToActivateForTargetContentIdentifierPredicate;
```

#### Discussion

Use this property to specify which tasks you want this scene to handle. UIKit evaluates your predicate against the [`targetContentIdentifier`](../../Foundation/nsuseractivity/targetcontentidentifier.md) property of the object causing the activation of the scene. Many different objects contain target content identifiers, including [`NSUserActivity`](../../Foundation/nsuseractivity.md), [`UNNotificationContent`](../../UserNotifications/unnotificationcontent.md), and [`UIApplicationShortcutItem`](../uiapplicationshortcutitem.md).

UIKit must be able to evaluate your predicate’s conditions outside the scope of your app, so don’t include conditions that require dynamic evaluation. For example, don’t include key paths in your predicate and don’t create predicates that evaluate conditions using selectors or blocks. The default value of this property is a predicate that always evaluates to the value [`false`](../../Swift/false.md).

## See Also

### Specifying the conditions
- [var canActivateForTargetContentIdentifierPredicate: NSPredicate](./canactivatefortargetcontentidentifierpredicate.md)
  Conditions for which UIKit can activate the scene if a better alternative doesn’t exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneactivationconditions/preferstoactivatefortargetcontentidentifierpredicate)*