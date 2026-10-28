# UIView.ReservedRegion.QueryOptions

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Options for querying reserved regions.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
struct QueryOptions
```

## Overview

Pass query options to [`reservedRegions(kind:options:)`](../reservedregions%28kind,options%29.md) to change which regions you get.

## Topics

### Setting query options
- [static let includeInactive: UIView.ReservedRegion.QueryOptions](./queryoptions/includeinactive.md)
  An option that includes inactive reserved regions in the results.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../../Swift/optionset.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [SetAlgebra](../../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/reservedregion/queryoptions)*