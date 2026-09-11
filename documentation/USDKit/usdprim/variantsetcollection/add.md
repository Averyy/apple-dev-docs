# add(_:)

**Framework**: USDKit  
**Kind**: method

Adds a new variant set to the prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@discardableResult
func add(_ variantSetName: String) throws -> USDPrim.VariantSet
```

#### Return Value

The newly added variant set.

#### Discussion

> **Note**: An error if the variant set cannot be added.

## Parameters

- `variantSetName`: The name of the variant set to add.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/variantsetcollection/add(_:))*