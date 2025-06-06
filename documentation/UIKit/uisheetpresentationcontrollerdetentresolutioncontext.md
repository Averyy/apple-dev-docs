# UISheetPresentationControllerDetentResolutionContext

**Framework**: UIKit  
**Kind**: protocol

A context for resolving custom detent values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
@MainActor
protocol UISheetPresentationControllerDetentResolutionContext : NSObjectProtocol
```

#### Overview

A context of this type is available in the `resolver` closure of [`custom(identifier:resolver:)`](uisheetpresentationcontroller/detent/custom(identifier:resolver:).md) (Swift) or  [`customDetentWithIdentifier:resolver:`](uisheetpresentationcontrollerdetent/customdetentwithidentifier:resolver:.md) (Objective-C).

## Topics

### Accessing the properties of the context
- [var containerTraitCollection: UITraitCollection](uisheetpresentationcontrollerdetentresolutioncontext/containertraitcollection.md)
  The trait collection of the sheet’s container view.
- [var maximumDetentValue: CGFloat](uisheetpresentationcontrollerdetentresolutioncontext/maximumdetentvalue.md)
  The maximum value of a detent.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [static func custom(identifier: UISheetPresentationController.Detent.Identifier?, resolver: (any UISheetPresentationControllerDetentResolutionContext) -> CGFloat?) -> UISheetPresentationController.Detent](uisheetpresentationcontroller/detent/custom(identifier:resolver:).md)
  Creates a custom detent for a sheet by computing its value according to the properties of the provided context.
- [func resolvedValue(in: any UISheetPresentationControllerDetentResolutionContext) -> CGFloat?](uisheetpresentationcontroller/detent/resolvedvalue(in:).md)
  Resolves a detent to its value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontrollerdetentresolutioncontext)*