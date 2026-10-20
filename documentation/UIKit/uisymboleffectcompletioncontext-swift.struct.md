# UISymbolEffectCompletionContext

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Information about a symbol effect’s addition or removal.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS

## Declaration

```swift
@MainActor
struct UISymbolEffectCompletionContext
```

## Topics

### Determining completion status
- [var effect: any SymbolEffect](./uisymboleffectcompletioncontext-swift.struct/effect.md)
  The symbol effect that completed.
- [var isFinished: Bool](./uisymboleffectcompletioncontext-swift.struct/isfinished.md)
  A Boolean value that indicates whether the symbol effect finished completely.
- [var sender: AnyObject?](./uisymboleffectcompletioncontext-swift.struct/sender.md)
  The object, an image view or bar button item, that received the symbol effect.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring symbol effects
- [func addSymbolEffect(some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](./uiimageview/addsymboleffect%28_,options,animated,completion%29-18jqj.md)
  Adds a discrete symbol effect to the image view with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](./uiimageview/addsymboleffect%28_,options,animated,completion%29-2ixnm.md)
  Adds a discrete, indefinite symbol effect to the image view with the specified options and animation.
- [func addSymbolEffect(some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](./uiimageview/addsymboleffect%28_,options,animated,completion%29-896qd.md)
  Adds an indefinite symbol effect to the image view with the specified options and animation.
- [func setSymbolImage(UIImage, contentTransition: some ContentTransitionSymbolEffect & SymbolEffect, options: SymbolEffectOptions, completion: UISymbolEffectCompletion?)](./uiimageview/setsymbolimage%28_,contenttransition,options,completion%29.md)
  Sets a symbol image using the specified content-transition effect, options, and completion handler.
- [func removeSymbolEffect(ofType: some IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](./uiimageview/removesymboleffect%28oftype,options,animated,completion%29-218lh.md)
  Removes the symbol effect that matches the specified indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & IndefiniteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](./uiimageview/removesymboleffect%28oftype,options,animated,completion%29-31zec.md)
  Removes the symbol effect that matches the specified discrete, indefinite effect type, using the specified options and animation setting.
- [func removeSymbolEffect(ofType: some DiscreteSymbolEffect & SymbolEffect, options: SymbolEffectOptions, animated: Bool, completion: UISymbolEffectCompletion?)](./uiimageview/removesymboleffect%28oftype,options,animated,completion%29-2boi2.md)
  Removes the symbol effect that matches the specified discrete effect type, using the specified options and animation setting.
- [func removeAllSymbolEffects(options: SymbolEffectOptions, animated: Bool)](./uiimageview/removeallsymboleffects%28options,animated%29.md)
  Removes all symbol effects from the image view, using the specified options and animation setting.
- [typealias UISymbolEffectCompletion](./uisymboleffectcompletion-7qt7g.md)
  A completion handler for adding and removing symbol effects and transitions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisymboleffectcompletioncontext-swift.struct)*