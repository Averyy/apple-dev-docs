# registerForTraitChanges:withTarget:action:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
- (id<UITraitChangeRegistration>) registerForTraitChanges:(NSArray<Class<UITraitDefinition>> *) traits withTarget:(id) target action:(SEL) action;
```

## Return Value

An opaque token you can use to stop observing trait changes by passing to [`unregisterForTraitChanges(_:)`](../uitraitchangeobservable-67e94/unregisterfortraitchanges%28_%29.md). You don’t have to unregister your observations, and you can safely ignore this value.

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
- [- registerForTraitChanges:withAction:](./registerfortraitchanges_withaction_.md)
  Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.
- [- registerForTraitChanges:withHandler:](./registerfortraitchanges_withhandler_.md)
  Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [- unregisterForTraitChanges:](./unregisterfortraitchanges_.md)
  Tells the system to stop observing previously registered traits.
- [UITraitChangeHandler](../uitraitchangehandler.md)
- [protocol UITraitChangeRegistration](../uitraitchangeregistration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitchangeobservable-7qoet/registerfortraitchanges:withtarget:action:)*