# init(effect:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a new visual effect view with the designated visual effect.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(effect: UIVisualEffect?)
```

```objc
- (instancetype) initWithEffect:(UIVisualEffect *) effect;
```

#### Return Value

The new view containing the designated visual effect.

## Parameters

- `effect`: The [`UIVisualEffect`](../uivisualeffect.md) you provide for the view. This can be a [`UIBlurEffect`](../uiblureffect.md) or a [`UIVibrancyEffect`](../uivibrancyeffect.md).

## See Also

### Creating a visual effect view
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a visual effect view from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivisualeffectview/init(effect:))*