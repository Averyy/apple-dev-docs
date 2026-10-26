# unregisterForTraitChanges:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the system to stop observing previously registered traits.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
- (void) unregisterForTraitChanges:(id<UITraitChangeRegistration>) registration;
```

#### Discussion

Use this method if you want the system to stop observing trait changes for a previous registration. UIKit doesn’t require you to unregister for trait changes at the end of the view lifecycle. Unregister only if you need to dynamically change which traits you observe.

## Parameters

- `registration`: A token that identifies the registration, obtained from one of the trait registration method calls.

## See Also

### Observing trait changes
- [- registerForTraitChanges:withAction:](./registerfortraitchanges_withaction_.md)
  Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.
- [- registerForTraitChanges:withHandler:](./registerfortraitchanges_withhandler_.md)
  Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [- registerForTraitChanges:withTarget:action:](./registerfortraitchanges_withtarget_action_.md)
  Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [UITraitChangeHandler](../uitraitchangehandler.md)
- [protocol UITraitChangeRegistration](../uitraitchangeregistration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitchangeobservable-7qoet/unregisterfortraitchanges:)*