# resolvedValueInContext:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Resolves a detent to its value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```objc
- (CGFloat) resolvedValueInContext:(id<UISheetPresentationControllerDetentResolutionContext>) context;
```

#### Return Value

A [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md) that represents the value of the detent, or [`UISheetPresentationControllerDetentInactive`](../uisheetpresentationcontrollerdetentinactive.md) if the detent is inactive in the provided context.

#### Discussion

You can use this method to get the values of the system [`medium`](../uisheetpresentationcontroller/detent/identifier-swift.struct/medium.md) and [`large`](../uisheetpresentationcontroller/detent/identifier-swift.struct/large.md) detents, or the value of a custom detent. Use this method inside [`customDetentWithIdentifier:resolver:`](./customdetentwithidentifier_resolver_.md) to construct a custom detent according to the values of known detents.

## Parameters

- `context`: A context for resolving custom detent values. This context is available in the `resolver` block of [`customDetentWithIdentifier:resolver:`](./customdetentwithidentifier_resolver_.md).

## See Also

### Creating a custom detent
- [+ customDetentWithIdentifier:resolver:](./customdetentwithidentifier_resolver_.md)
  Creates a custom detent for a sheet by computing its value according to the properties of the provided context.
- [protocol UISheetPresentationControllerDetentResolutionContext](../uisheetpresentationcontrollerdetentresolutioncontext.md)
  A context for resolving custom detent values.
- [UISheetPresentationControllerDetentInactive](../uisheetpresentationcontrollerdetentinactive.md)
  A value that represents an inactive detent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontrollerdetent/resolvedvalueincontext:)*