# custom(identifier:resolver:)

**Framework**: UIKit  
**Kind**: method

Creates a custom detent for a sheet by computing its value according to the properties of the provided context.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
@MainActor
@preconcurrency static func custom(identifier: UISheetPresentationController.Detent.Identifier? = nil, resolver: @escaping (any UISheetPresentationControllerDetentResolutionContext) -> CGFloat?) -> UISheetPresentationController.Detent
```

## Parameters

- `identifier`: An identifier for the detent. Specify a unique identifier for each custom detent for a sheet. If you don’t specify an identifier, the system generates a random identifier.
- `resolver`: A closure for resolving the detent value with an input of type [`UISheetPresentationControllerDetentResolutionContext`](uisheetpresentationcontrollerdetentresolutioncontext.md). The value you return from this closure is a height within the safe area of the sheet. For example, return `200` for a detent with a height of `200` plus [`safeAreaInsets`](uiview/safeareainsets.md).[`bottom`](uiedgeinsets/bottom.md) when the sheet is edge-attached, or `200` when the sheet is floating. Return `nil` to specify that the detent is inactive according to the provided context. If the closure depends on any external inputs, call [`invalidateDetents()`](uisheetpresentationcontroller/invalidatedetents().md) on the sheet when the external inputs change. Don’t set any properties on [`UISheetPresentationController`](uisheetpresentationcontroller.md) during the execution of this closure.

## See Also

- [func resolvedValue(in: any UISheetPresentationControllerDetentResolutionContext) -> CGFloat?](uisheetpresentationcontroller/detent/resolvedvalue(in:).md)
  Resolves a detent to its value.
- [protocol UISheetPresentationControllerDetentResolutionContext](uisheetpresentationcontrollerdetentresolutioncontext.md)
  A context for resolving custom detent values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/detent/custom(identifier:resolver:))*