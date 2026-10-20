# UITraitChangeRegistration

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol UITraitChangeRegistration <NSObject, NSCopying>
```

## Mentions

- [Adapting your app when traits change](./adapting-your-app-when-traits-change.md)
- [Building a desktop-class iPad app](./building-a-desktop-class-ipad-app.md)

## Relationships

### Inherits From
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Observing trait changes
- [func registerForTraitChanges([UITrait], action: Selector) -> any UITraitChangeRegistration](./uitraitchangeobservable-67e94/registerfortraitchanges%28_,action%29.md)
  Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.
- [func registerForTraitChanges<TraitEnvironment>([UITrait], handler: Self.TraitChangeHandler<TraitEnvironment>) -> any UITraitChangeRegistration](./uitraitchangeobservable-67e94/registerfortraitchanges%28_,handler%29.md)
  Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [func registerForTraitChanges([UITrait], target: Any, action: Selector) -> any UITraitChangeRegistration](./uitraitchangeobservable-67e94/registerfortraitchanges%28_,target,action%29.md)
  Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [func unregisterForTraitChanges(any UITraitChangeRegistration)](./uitraitchangeobservable-67e94/unregisterfortraitchanges%28_%29.md)
  Tells the system to stop observing previously registered traits.
- [UITraitChangeObservable.TraitChangeHandler](./uitraitchangeobservable-67e94/traitchangehandler.md)
  A closure the system executes when observed traits change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitchangeregistration)*