# UITraitChangeRegistration

**Framework**: UIKit  
**Kind**: protocol

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITraitChangeRegistration : NSCopying, NSObjectProtocol
```

## Mentions

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

## Relationships

### Inherits From
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func registerForTraitChanges([UITrait], action: Selector) -> any UITraitChangeRegistration](uitraitchangeobservable-67e94/registerfortraitchanges(_:action:).md)
  Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.
- [func registerForTraitChanges<TraitEnvironment>([UITrait], handler: Self.TraitChangeHandler<TraitEnvironment>) -> any UITraitChangeRegistration](uitraitchangeobservable-67e94/registerfortraitchanges(_:handler:).md)
  Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [func registerForTraitChanges([UITrait], target: Any, action: Selector) -> any UITraitChangeRegistration](uitraitchangeobservable-67e94/registerfortraitchanges(_:target:action:).md)
  Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [func unregisterForTraitChanges(any UITraitChangeRegistration)](uitraitchangeobservable-67e94/unregisterfortraitchanges(_:).md)
  Tells the system to stop observing previously registered traits.
- [UITraitChangeObservable.TraitChangeHandler](uitraitchangeobservable-67e94/traitchangehandler.md)
  A closure the system executes when observed traits change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitchangeregistration)*