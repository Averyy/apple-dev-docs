# registerForTraitChanges(_:target:action:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS

## Declaration

```swift
@discardableResult
@MainActor func registerForTraitChanges(_ traits: [UITrait], target: Any, action: Selector) -> any UITraitChangeRegistration
```

## Return Value

An opaque token you can use to stop observing trait changes by passing to [`unregisterForTraitChanges(_:)`](./unregisterfortraitchanges%28_%29.md). You don’t have to unregister your observations, and you can safely ignore this value.

## Discussion

The method specified by the selector can take zero, one, or two arguments. If the method takes one argument, the system passes the object whose trait collection is changing. If the method takes two arguments, the system passes the trait collection prior to the observed changes as the second argument.

The following example registers size class traits so that the system executes the closure when a size class trait changes in the view’s trait collection:

```swift
@objc func sizeClassChanged(view: UIView, previousTraitCollection: UITraitCollection) {
    // Perform invalidation in response to the size class changing.
}

let sizeTraits: [UITrait] = [UITraitVerticalSizeClass.self, UITraitHorizontalSizeClass.self]

view.registerForTraitChanges(sizeTraits, target: self, action: #selector(sizeClassChanged(view:
previousTraitCollection:)))

```

## Parameters

- `traits`: An array of traits to observe for changes.
- `target`: The object that receives the method call passed in the action parameter.
- `action`: A selector identifying the method the system calls when one of the registered trait changes.

## See Also

### Observing trait changes
- [func registerForTraitChanges([UITrait], action: Selector) -> any UITraitChangeRegistration](./registerfortraitchanges%28_,action%29.md)
  Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.
- [func registerForTraitChanges<TraitEnvironment>([UITrait], handler: Self.TraitChangeHandler<TraitEnvironment>) -> any UITraitChangeRegistration](./registerfortraitchanges%28_,handler%29.md)
  Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [func unregisterForTraitChanges(any UITraitChangeRegistration)](./unregisterfortraitchanges%28_%29.md)
  Tells the system to stop observing previously registered traits.
- [UITraitChangeObservable.TraitChangeHandler](./traitchangehandler.md)
  A closure the system executes when observed traits change.
- [protocol UITraitChangeRegistration](../uitraitchangeregistration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitchangeobservable-67e94/registerfortraitchanges(_:target:action:))*