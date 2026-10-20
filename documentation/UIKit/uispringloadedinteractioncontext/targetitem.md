# targetItem

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The specific subview, or associated model object, of the target view to use for the spring-loaded interaction.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var targetItem: Any? { get set }
```

```objc
@property (nonatomic, strong, nullable) id targetItem;
```

## See Also

### Managing state
- [var state: UISpringLoadedInteractionEffectState](./state.md)
  The current view style for the spring-loaded interaction.
- [var targetView: UIView?](./targetview.md)
  The view to which the current spring-loaded interaction view style is applied.
- [enum UISpringLoadedInteractionEffectState](../uispringloadedinteractioneffectstate.md)
  The spring-loaded interaction states that determine the style of the interaction view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringloadedinteractioncontext/targetitem)*