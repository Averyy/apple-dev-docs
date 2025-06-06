# registerForTraitChanges(_:handler:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Registers a list of traits to observe and a closure to execute when one of the observed traits changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
@discardableResult
@MainActor func registerForTraitChanges<TraitEnvironment>(_ traits: [UITrait], handler: @escaping Self.TraitChangeHandler<TraitEnvironment>) -> any UITraitChangeRegistration where TraitEnvironment : UITraitEnvironment
```

#### Return Value

An opaque token you can use to stop observing trait changes by passing to [`unregisterForTraitChanges(_:)`](uitraitchangeobservable-67e94/unregisterfortraitchanges(_:).md). You don’t have to unregister your observations, and you can safely ignore this value.

#### Discussion

The first parameter of the closure provides access to the observed object whose traits have changed, so you don’t need to create a weak reference. When registering for changes on self, use `self` as the name and `Self` as the type of the first parameter.

The following example registers size class traits so that the system executes the closure when a size class trait changes in the view’s trait collection:

```swift
let sizeTraits: [UITrait] = [UITraitVerticalSizeClass.self, UITraitHorizontalSizeClass.self]

// Register for size class changes on self. Declare the first paramteter as `self: Self`.
// Declaring self as the first parameter eliminates the need to capture self from outside the closure, and avoids strong reference cycles.
registerForTraitChanges(sizeTraits) { (self: Self, previousTraitCollection: UITraitCollection) in
    // Handle the trait change.
}

// Register for size class changes on a different view of class MyView.
view.registerForTraitChanges(sizeTraits) { (view: MyView, previousTraitCollection: UITraitCollection) in
    // Handle the trait change.
}
```

## Parameters

- `traits`: An array of traits to observe for changes.
- `handler`: A closure that the system executes when one of the registered traits changes.

## See Also

- [func registerForTraitChanges([UITrait], action: Selector) -> any UITraitChangeRegistration](uitraitchangeobservable-67e94/registerfortraitchanges(_:action:).md)
  Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.
- [func registerForTraitChanges([UITrait], target: Any, action: Selector) -> any UITraitChangeRegistration](uitraitchangeobservable-67e94/registerfortraitchanges(_:target:action:).md)
  Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [func unregisterForTraitChanges(any UITraitChangeRegistration)](uitraitchangeobservable-67e94/unregisterfortraitchanges(_:).md)
  Tells the system to stop observing previously registered traits.
- [UITraitChangeObservable.TraitChangeHandler](uitraitchangeobservable-67e94/traitchangehandler.md)
  A closure the system executes when observed traits change.
- [protocol UITraitChangeRegistration](uitraitchangeregistration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitchangeobservable-67e94/registerfortraitchanges(_:handler:))*