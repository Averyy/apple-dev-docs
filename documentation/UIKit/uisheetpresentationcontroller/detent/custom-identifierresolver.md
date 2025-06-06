# custom(identifier:resolver:)

**Framework**: UIKit  
**Kind**: method

Creates a custom detent for a sheet by computing its value according to the properties of the provided context.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+

## Declaration

```swift
@MainActor
@preconcurrency static func custom(identifier: UISheetPresentationController.Detent.Identifier? = nil, resolver: @escaping (any UISheetPresentationControllerDetentResolutionContext) -> CGFloat?) -> UISheetPresentationController.Detent
```

## Parameters

- `identifier`: An identifier for the detent. Specify a unique identifier for each custom detent for a sheet. If you don’t specify an identifier, the system generates a random identifier.
- `resolver`: Don’t set any properties on   during the execution of this closure.

## See Also

- [func resolvedValue(in: any UISheetPresentationControllerDetentResolutionContext) -> CGFloat?](uisheetpresentationcontroller/detent/resolvedvalue(in:).md)
  Resolves a detent to its value.
- [protocol UISheetPresentationControllerDetentResolutionContext](uisheetpresentationcontrollerdetentresolutioncontext.md)
  A context for resolving custom detent values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/detent/custom(identifier:resolver:))*