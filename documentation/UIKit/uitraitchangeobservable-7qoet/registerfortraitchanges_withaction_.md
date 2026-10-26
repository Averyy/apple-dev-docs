# registerForTraitChanges:withAction:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
- (id<UITraitChangeRegistration>) registerForTraitChanges:(NSArray<Class<UITraitDefinition>> *) traits withAction:(SEL) action;
```

#### Return Value

An opaque token you can use to stop observing trait changes by passing to [`unregisterForTraitChanges(_:)`](../uitraitchangeobservable-67e94/unregisterfortraitchanges%28_%29.md). You don’t have to unregister your observations, and you can safely ignore this value.

#### Discussion

This is a convenience method for [`registerForTraitChanges(_:target:action:)`](../uitraitchangeobservable-67e94/registerfortraitchanges%28_,target,action%29.md) when the object receiving the registration is the target of the action. For example, when you register for changes on `self`, the `target` is `self`.

The following example calls [`setNeedsLayout()`](../uiview/setneedslayout%28%29.md) in response to changes to size traits:

```swift
let sizeTraits: [UITrait] = [UITraitVerticalSizeClass.self, UITraitHorizontalSizeClass.self]

// Register for size class changes on self, and invalidate the layout in response to changes.
registerForTraitChanges(sizeTraits, action: #selector(UIView.setNeedsLayout))
```

## Parameters

- `traits`: An array of traits to observe for changes.
- `action`: A selector identifying the method the system calls when one of the registered trait changes.

## See Also

### Observing trait changes
- [- registerForTraitChanges:withHandler:](./registerfortraitchanges_withhandler_.md)
  Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [- registerForTraitChanges:withTarget:action:](./registerfortraitchanges_withtarget_action_.md)
  Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [- unregisterForTraitChanges:](./unregisterfortraitchanges_.md)
  Tells the system to stop observing previously registered traits.
- [UITraitChangeHandler](../uitraitchangehandler.md)
- [protocol UITraitChangeRegistration](../uitraitchangeregistration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitchangeobservable-7qoet/registerfortraitchanges:withaction:)*