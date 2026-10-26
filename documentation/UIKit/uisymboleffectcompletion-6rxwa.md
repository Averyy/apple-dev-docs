# UISymbolEffectCompletion

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

A completion handler for adding and removing symbol effects and transitions.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```c
typedef void (^)(UISymbolEffectCompletionContext *) UISymbolEffectCompletion;
```

## See Also

### Configuring symbol effects
- [- addSymbolEffect:](./uiimageview/addsymboleffect_.md)
  Adds a symbol effect to the image view with default options and animation.
- [- addSymbolEffect:options:](./uiimageview/addsymboleffect_options_.md)
  Adds a symbol effect to the image view with the specified options and default animation.
- [- addSymbolEffect:options:animated:](./uiimageview/addsymboleffect_options_animated_.md)
  Adds a symbol effect to the image view with the specified options and animation.
- [- addSymbolEffect:options:animated:completion:](./uiimageview/addsymboleffect_options_animated_completion_.md)
  Adds a symbol effect to the image view with the specified options, animation, and completion handler.
- [- setSymbolImage:withContentTransition:](./uiimageview/setsymbolimage_withcontenttransition_.md)
  Sets a symbol image using the specified content-transition effect.
- [- setSymbolImage:withContentTransition:options:](./uiimageview/setsymbolimage_withcontenttransition_options_.md)
  Sets a symbol image using the specified content-transition effect and options.
- [- setSymbolImage:withContentTransition:options:completion:](./uiimageview/setsymbolimage_withcontenttransition_options_completion_.md)
  Sets a symbol image using the specified content-transition effect, options, and completion handler.
- [- removeSymbolEffectOfType:](./uiimageview/removesymboleffectoftype_.md)
  Removes the symbol effect that matches the specified effect type.
- [- removeSymbolEffectOfType:options:](./uiimageview/removesymboleffectoftype_options_.md)
  Removes the symbol effect that matches the specified effect type, using the specified options.
- [- removeSymbolEffectOfType:options:animated:](./uiimageview/removesymboleffectoftype_options_animated_.md)
  Removes the symbol effect that matches the specified effect type, using the specified options and animation setting.
- [- removeSymbolEffectOfType:options:animated:completion:](./uiimageview/removesymboleffectoftype_options_animated_completion_.md)
  Removes the symbol effect that matches the specified effect type, using the specified options, animation setting, and completion handler.
- [- removeAllSymbolEffects](./uiimageview/removeallsymboleffects.md)
  Removes all symbol effects from the image view.
- [- removeAllSymbolEffectsWithOptions:](./uiimageview/removeallsymboleffectswithoptions_.md)
  Removes all symbol effects from the image view, using the specified options.
- [- removeAllSymbolEffectsWithOptions:animated:](./uiimageview/removeallsymboleffectswithoptions_animated_.md)
  Removes all symbol effects from the image view, using the specified options and animation setting.
- [UISymbolEffectCompletionContext](./uisymboleffectcompletioncontext-c.class.md)
  Information about a symbol effect’s addition or removal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisymboleffectcompletion-6rxwa)*