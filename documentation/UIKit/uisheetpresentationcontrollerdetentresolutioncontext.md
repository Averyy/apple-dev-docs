# UISheetPresentationControllerDetentResolutionContext

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol UISheetPresentationControllerDetentResolutionContext <NSObject>
```

#### Overview

A context of this type is available in the `resolver` closure of [`custom(identifier:resolver:)`](./uisheetpresentationcontroller/detent/custom%28identifier,resolver%29.md) (Swift) or  [`customDetentWithIdentifier:resolver:`](./uisheetpresentationcontrollerdetent/customdetentwithidentifier_resolver_.md) (Objective-C).

## Topics

### Accessing the properties of the context
- [var containerTraitCollection: UITraitCollection](./uisheetpresentationcontrollerdetentresolutioncontext/containertraitcollection.md)
  The trait collection of the sheet’s container view.
- [var maximumDetentValue: CGFloat](./uisheetpresentationcontrollerdetentresolutioncontext/maximumdetentvalue.md)
  The maximum value of a detent.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating a custom detent
- [static func custom(identifier: UISheetPresentationController.Detent.Identifier?, resolver: (any UISheetPresentationControllerDetentResolutionContext) -> CGFloat?) -> UISheetPresentationController.Detent](./uisheetpresentationcontroller/detent/custom%28identifier,resolver%29.md)
  Creates a custom detent for a sheet by computing its value according to the properties of the provided context.
- [func resolvedValue(in: any UISheetPresentationControllerDetentResolutionContext) -> CGFloat?](./uisheetpresentationcontroller/detent/resolvedvalue%28in%29.md)
  Resolves a detent to its value.
- [+ customDetentWithIdentifier:resolver:](./uisheetpresentationcontrollerdetent/customdetentwithidentifier_resolver_.md)
  Creates a custom detent for a sheet by computing its value according to the properties of the provided context.
- [- resolvedValueInContext:](./uisheetpresentationcontrollerdetent/resolvedvalueincontext_.md)
  Resolves a detent to its value.
- [UISheetPresentationControllerDetentInactive](./uisheetpresentationcontrollerdetentinactive.md)
  A value that represents an inactive detent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontrollerdetentresolutioncontext)*