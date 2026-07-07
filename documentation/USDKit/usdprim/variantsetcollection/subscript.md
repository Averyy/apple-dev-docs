# subscript(_:)

**Framework**: USDKit  
**Kind**: subscript

Returns the variant set with the specified name, or `nil` if no variant set with that name exists on the prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
subscript(name: String) -> USDPrim.VariantSet? { get }
```

#### Return Value

The variant set, or `nil` if no variant set with that name exists on the prim.

## Parameters

- `name`: The name of the variant set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/variantsetcollection/subscript(_:))*