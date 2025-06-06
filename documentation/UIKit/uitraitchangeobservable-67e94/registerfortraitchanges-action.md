# registerForTraitChanges(_:action:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
@discardableResult
@MainActor func registerForTraitChanges(_ traits: [UITrait], action: Selector) -> any UITraitChangeRegistration
```

#### Return Value

An opaque token you can use to stop observing trait changes by passing to [`unregisterForTraitChanges(_:)`](uitraitchangeobservable-67e94/unregisterfortraitchanges(_:).md). You don’t have to unregister your observations, and you can safely ignore this value.

#### Discussion

This is a convenience method for [`registerForTraitChanges(_:target:action:)`](uitraitchangeobservable-67e94/registerfortraitchanges(_:target:action:).md) when the object receiving the registration is the target of the action. For example, when you register for changes on `self`, the `target` is `self`.

The following example calls [`setNeedsLayout()`](uiview/setneedslayout().md) in response to changes to size traits:

```swift
let sizeTraits: [UITrait] = [UITraitVerticalSizeClass.self, UITraitHorizontalSizeClass.self]

// Register for size class changes on self, and invalidate the layout in response to changes.
registerForTraitChanges(sizeTraits, action: #selector(UIView.setNeedsLayout))
```

## Parameters

- `traits`: An array of traits to observe for changes.
- `action`: A selector identifying the method the system calls when one of the registered trait changes.

## See Also

- [func registerForTraitChanges<TraitEnvironment>([UITrait], handler: Self.TraitChangeHandler<TraitEnvironment>) -> any UITraitChangeRegistration](uitraitchangeobservable-67e94/registerfortraitchanges(_:handler:).md)
  Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [func registerForTraitChanges([UITrait], target: Any, action: Selector) -> any UITraitChangeRegistration](uitraitchangeobservable-67e94/registerfortraitchanges(_:target:action:).md)
  Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [func unregisterForTraitChanges(any UITraitChangeRegistration)](uitraitchangeobservable-67e94/unregisterfortraitchanges(_:).md)
  Tells the system to stop observing previously registered traits.
- [UITraitChangeObservable.TraitChangeHandler](uitraitchangeobservable-67e94/traitchangehandler.md)
  A closure the system executes when observed traits change.
- [protocol UITraitChangeRegistration](uitraitchangeregistration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitchangeobservable-67e94/registerfortraitchanges(_:action:))*