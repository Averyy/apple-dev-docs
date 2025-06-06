# UITraitChangeObservable.TraitChangeHandler

**Framework**: UIKit  
**Kind**: typealias

A closure the system executes when observed traits change.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
typealias TraitChangeHandler<TraitEnvironment> = (TraitEnvironment, UITraitCollection) -> Void where TraitEnvironment : UITraitEnvironment
```

#### Discussion

Use [`registerForTraitChanges(_:handler:)`](uitraitchangeobservable-67e94/registerfortraitchanges(_:handler:).md) to register a list of traits to observe and a handler to execute.

If the closure captures a strong reference to the object receiving the registration, it creates a strong reference cycle. Use the `traitEnvironment` parameter to refer to the observed object inside the closure.

## Parameters

- `traitEnvironment`: The observed object containing the updated trait collection.
- `previousTraitCollection`: The trait collection prior to the changes that triggered the execution of the handler.

## See Also

- [func registerForTraitChanges([UITrait], action: Selector) -> any UITraitChangeRegistration](uitraitchangeobservable-67e94/registerfortraitchanges(_:action:).md)
  Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.
- [func registerForTraitChanges<TraitEnvironment>([UITrait], handler: Self.TraitChangeHandler<TraitEnvironment>) -> any UITraitChangeRegistration](uitraitchangeobservable-67e94/registerfortraitchanges(_:handler:).md)
  Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [func registerForTraitChanges([UITrait], target: Any, action: Selector) -> any UITraitChangeRegistration](uitraitchangeobservable-67e94/registerfortraitchanges(_:target:action:).md)
  Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [func unregisterForTraitChanges(any UITraitChangeRegistration)](uitraitchangeobservable-67e94/unregisterfortraitchanges(_:).md)
  Tells the system to stop observing previously registered traits.
- [protocol UITraitChangeRegistration](uitraitchangeregistration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitchangeobservable-67e94/traitchangehandler)*