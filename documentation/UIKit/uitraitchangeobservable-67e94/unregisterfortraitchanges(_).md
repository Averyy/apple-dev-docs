# unregisterForTraitChanges(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the system to stop observing previously registered traits.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS

## Declaration

```swift
@MainActor
func unregisterForTraitChanges(_ registration: any UITraitChangeRegistration)
```

## Mentions

- [Adapting your app when traits change](../adapting-your-app-when-traits-change.md)

## Discussion

Use this method if you want the system to stop observing trait changes for a previous registration. UIKit doesn’t require you to unregister for trait changes at the end of the view lifecycle. Unregister only if you need to dynamically change which traits you observe.

## Parameters

- `registration`: A token that identifies the registration, obtained from one of the trait registration method calls.

## See Also

### Observing trait changes
- [func registerForTraitChanges([UITrait], action: Selector) -> any UITraitChangeRegistration](./registerfortraitchanges%28_,action%29.md)
  Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.
- [func registerForTraitChanges<TraitEnvironment>([UITrait], handler: Self.TraitChangeHandler<TraitEnvironment>) -> any UITraitChangeRegistration](./registerfortraitchanges%28_,handler%29.md)
  Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [func registerForTraitChanges([UITrait], target: Any, action: Selector) -> any UITraitChangeRegistration](./registerfortraitchanges%28_,target,action%29.md)
  Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [UITraitChangeObservable.TraitChangeHandler](./traitchangehandler.md)
  A closure the system executes when observed traits change.
- [protocol UITraitChangeRegistration](../uitraitchangeregistration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitchangeobservable-67e94/unregisterfortraitchanges(_:))*