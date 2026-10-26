# customDetentWithIdentifier:resolver:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a custom detent for a sheet by computing its value according to the properties of the provided context.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```objc
+ (instancetype) customDetentWithIdentifier:(UISheetPresentationControllerDetentIdentifier) identifier resolver:(CGFloat (^)(id<UISheetPresentationControllerDetentResolutionContext>context)) resolver;
```

## Parameters

- `identifier`: An identifier for the detent. Specify a unique identifier for each custom detent for a sheet. If you don’t specify an identifier, the system generates a random identifier.
- `resolver`: A block for resolving the detent value with an input of type [`UISheetPresentationControllerDetentResolutionContext`](../uisheetpresentationcontrollerdetentresolutioncontext.md). The value you return from this block is a height within the safe area of the sheet. For example, return `200` for a detent with a height of `200` plus [`safeAreaInsets`](../uiview/safeareainsets.md).[`bottom`](../uiedgeinsets/bottom.md) when the sheet is edge-attached, or `200` when the sheet is floating. Return [`UISheetPresentationControllerDetentInactive`](../uisheetpresentationcontrollerdetentinactive.md) to specify that the detent is inactive according to the provided context.

  If the block depends on any external inputs, call [`invalidateDetents()`](../uisheetpresentationcontroller/invalidatedetents%28%29.md) on the sheet when the external inputs change.

  Don’t set any properties on [`UISheetPresentationController`](../uisheetpresentationcontroller.md) during the execution of this block.

## See Also

### Creating a custom detent
- [- resolvedValueInContext:](./resolvedvalueincontext_.md)
  Resolves a detent to its value.
- [protocol UISheetPresentationControllerDetentResolutionContext](../uisheetpresentationcontrollerdetentresolutioncontext.md)
  A context for resolving custom detent values.
- [UISheetPresentationControllerDetentInactive](../uisheetpresentationcontrollerdetentinactive.md)
  A value that represents an inactive detent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontrollerdetent/customdetentwithidentifier:resolver:)*