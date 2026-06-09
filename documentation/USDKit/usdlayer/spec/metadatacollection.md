# USDLayer.Spec.MetadataCollection

**Framework**: USDKit  
**Kind**: protocol

Read/write access to metadata stored on a spec.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol MetadataCollection
```

## Topics

### Instance Properties
- [var infoKeys: [USDToken]](usdlayer/spec/metadatacollection/infokeys.md)
  All authored info keys on this spec, including structural fields (child specifier lists, type info, etc.).
- [var isDormant: Bool](usdlayer/spec/metadatacollection/isdormant.md)
  Whether the spec is dormant (the underlying data has been removed).
- [var layer: USDLayer?](usdlayer/spec/metadatacollection/layer.md)
  The layer containing this spec, or `nil` if dormant.
- [var metadataInfoKeys: [USDToken]](usdlayer/spec/metadatacollection/metadatainfokeys.md)
  The subset of info keys an inspector should treat as user-visible metadata. Excludes structural fields.
- [var path: USDLayer.Path](usdlayer/spec/metadatacollection/path.md)
  The path identifying this spec within its layer.
- [var specType: USDLayer.SpecType?](usdlayer/spec/metadatacollection/spectype.md)
  The kind of spec, or `nil` if the spec is dormant.
### Instance Methods
- [func clearInfo(USDToken)](usdlayer/spec/metadatacollection/clearinfo(_:).md)
  Clears the authored value for `key`.
- [func info(USDToken) -> USDValue?](usdlayer/spec/metadatacollection/info(_:).md)
  Returns the value of `key`, or `nil` if the key is unauthored.
- [func setInfo(USDToken, to: USDValue)](usdlayer/spec/metadatacollection/setinfo(_:to:).md)
  Sets `key` to `value`.

## Relationships

### Conforming Types
- [USDLayer.Spec](usdlayer/spec.md)
- [USDPrim.Attribute.Spec](usdprim/attribute/spec.md)
- [USDPrim.Property.Spec](usdprim/property/spec.md)
- [USDPrim.PseudoRootSpec](usdprim/pseudorootspec.md)
- [USDPrim.Relationship.Spec](usdprim/relationship/spec.md)
- [USDPrim.Spec](usdprim/spec.md)
- [USDPrim.VariantSetSpec](usdprim/variantsetspec.md)
- [USDPrim.VariantSpec](usdprim/variantspec.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/spec/metadatacollection)*