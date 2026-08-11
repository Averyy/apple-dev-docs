# USDStage.Object.MetadataCollection

**Framework**: USDKit  
**Kind**: protocol

A scene graph object that possesses metadata.

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

#### Overview

Prims, attributes, and relationships may have associated metadata. Metadata on an object is accessed by its name, which is a [`USDToken`](usdtoken.md).

> ❗ **Important**: Don’t declare new conformances to MetadataCollection. Only the types provided by the USDStageKit framework are valid conforming types.

## Topics

### Instance Properties
- [var allAuthoredMetadata: Dictionary<USDToken, USDValue>](usdstage/object/metadatacollection/allauthoredmetadata.md)
  Every authored metadata value on this object.
- [var allMetadata: Dictionary<USDToken, USDValue>](usdstage/object/metadatacollection/allmetadata.md)
  Every metadata value on this object, including fallbacks.
- [var assetInfo: Dictionary<String, USDValue>](usdstage/object/metadatacollection/assetinfo.md)
  A dictionary of asset information authored on this object.
- [var customData: Dictionary<String, USDValue>](usdstage/object/metadatacollection/customdata.md)
  A dictionary of custom data authored on this object.
- [var displayName: String](usdstage/object/metadatacollection/displayname.md)
  A non-unique display name authored on this object.
- [var documentation: String](usdstage/object/metadatacollection/documentation.md)
  A human-readable description authored on this object.
- [var hasAssetInfo: Bool](usdstage/object/metadatacollection/hasassetinfo.md)
  A Boolean value that indicates whether this object has asset information.
- [var hasAuthoredAssetInfo: Bool](usdstage/object/metadatacollection/hasauthoredassetinfo.md)
  A Boolean value that indicates whether this object has authored asset information.
- [var hasAuthoredCustomData: Bool](usdstage/object/metadatacollection/hasauthoredcustomdata.md)
  A Boolean value that indicates whether this object has authored custom data.
- [var hasAuthoredDisplayName: Bool](usdstage/object/metadatacollection/hasauthoreddisplayname.md)
  A Boolean value that indicates whether this object has an authored display name.
- [var hasAuthoredDocumentation: Bool](usdstage/object/metadatacollection/hasauthoreddocumentation.md)
  A Boolean value that indicates whether this object has authored documentation.
- [var hasAuthoredHidden: Bool](usdstage/object/metadatacollection/hasauthoredhidden.md)
  A Boolean value that indicates whether this object has an authored `isHidden` opinion.
- [var hasCustomData: Bool](usdstage/object/metadatacollection/hascustomdata.md)
  A Boolean value that indicates whether this object has custom data.
- [var isHidden: Bool](usdstage/object/metadatacollection/ishidden.md)
  A Boolean value that indicates whether this object is hidden from browsing UI.
### Instance Methods
- [func assetInfoByKey(USDToken) -> USDValue?](usdstage/object/metadatacollection/assetinfobykey(_:).md)
  Returns the asset information value at the given key path.
- [func clearAssetInfo()](usdstage/object/metadatacollection/clearassetinfo.md)
  Removes all authored asset information on this object.
- [func clearAssetInfoByKey(USDToken)](usdstage/object/metadatacollection/clearassetinfobykey(_:).md)
  Removes the authored asset information value at the given key path.
- [func clearCustomData()](usdstage/object/metadatacollection/clearcustomdata.md)
  Removes all authored custom data on this object.
- [func clearCustomDataByKey(USDToken)](usdstage/object/metadatacollection/clearcustomdatabykey(_:).md)
  Removes the authored custom data value at the given key path.
- [func clearDisplayName()](usdstage/object/metadatacollection/cleardisplayname.md)
  Removes the authored display name on this object.
- [func clearDocumentation()](usdstage/object/metadatacollection/cleardocumentation.md)
  Removes the authored documentation on this object.
- [func clearHidden()](usdstage/object/metadatacollection/clearhidden.md)
  Removes the authored `isHidden` opinion on this object.
- [func clearMetadata(USDToken) throws](usdstage/object/metadatacollection/clearmetadata(_:).md)
  Removes the authored metadata value for the given key.
- [func clearMetadata(USDToken, keyPath: USDToken) throws](usdstage/object/metadatacollection/clearmetadata(_:keypath:).md)
  Removes the authored value at `keyPath` within the dictionary-valued metadata for the given key.
- [func customDataByKey(USDToken) -> USDValue?](usdstage/object/metadatacollection/customdatabykey(_:).md)
  Returns the custom data value at the given key path.
- [func hasAssetInfoByKey(USDToken) -> Bool](usdstage/object/metadatacollection/hasassetinfobykey(_:).md)
  Returns a Boolean value that indicates whether asset information exists at the given key path.
- [func hasAuthoredAssetInfoByKey(USDToken) -> Bool](usdstage/object/metadatacollection/hasauthoredassetinfobykey(_:).md)
  Returns a Boolean value that indicates whether authored asset information exists at the given key path.
- [func hasAuthoredCustomDataByKey(USDToken) -> Bool](usdstage/object/metadatacollection/hasauthoredcustomdatabykey(_:).md)
  Returns a Boolean value that indicates whether authored custom data exists at the given key path.
- [func hasAuthoredMetadata(USDToken) -> Bool](usdstage/object/metadatacollection/hasauthoredmetadata(_:).md)
  Returns a Boolean value that indicates whether metadata for the given key has an authored value.
- [func hasAuthoredMetadata(USDToken, keyPath: USDToken) -> Bool](usdstage/object/metadatacollection/hasauthoredmetadata(_:keypath:).md)
  Returns a Boolean value that indicates whether the dictionary-valued metadata for the given key has an authored value at `keyPath`.
- [func hasCustomDataByKey(USDToken) -> Bool](usdstage/object/metadatacollection/hascustomdatabykey(_:).md)
  Returns a Boolean value that indicates whether custom data exists at the given key path.
- [func hasMetadata(USDToken) -> Bool](usdstage/object/metadatacollection/hasmetadata(_:).md)
  Returns a Boolean value that indicates whether metadata for the given key has a value, including its fallback.
- [func hasMetadata(USDToken, keyPath: USDToken) -> Bool](usdstage/object/metadatacollection/hasmetadata(_:keypath:).md)
  Returns a Boolean value that indicates whether the dictionary-valued metadata for the given key has a value at `keyPath`.
- [func metadata(USDToken) -> UInt?](usdstage/object/metadatacollection/metadata(_:)-136hk.md)
- [func metadata<T>(USDToken) -> T?](usdstage/object/metadatacollection/metadata(_:)-574ho.md)
  Returns the metadata value for the given key.
- [func metadata(USDToken) -> Int?](usdstage/object/metadatacollection/metadata(_:)-8jz5b.md)
- [func metadata(USDToken, keyPath: USDToken) -> UInt?](usdstage/object/metadatacollection/metadata(_:keypath:)-5pid3.md)
- [func metadata<T>(USDToken, keyPath: USDToken) -> T?](usdstage/object/metadatacollection/metadata(_:keypath:)-62uj1.md)
  Returns the value at `keyPath` within the dictionary-valued metadata for the given key.
- [func metadata(USDToken, keyPath: USDToken) -> Int?](usdstage/object/metadatacollection/metadata(_:keypath:)-8isq8.md)
- [func setAssetInfoByKey(USDToken, value: USDValue)](usdstage/object/metadatacollection/setassetinfobykey(_:value:).md)
  Sets the asset information value at the given key path.
- [func setCustomDataByKey(USDToken, value: USDValue)](usdstage/object/metadatacollection/setcustomdatabykey(_:value:).md)
  Modifies the custom data value at the given key path.
- [func setMetadata(USDToken, keyPath: USDToken, value: UInt) throws](usdstage/object/metadatacollection/setmetadata(_:keypath:value:)-1ri3i.md)
- [func setMetadata<T>(USDToken, keyPath: USDToken, value: T) throws](usdstage/object/metadatacollection/setmetadata(_:keypath:value:)-62b48.md)
  Sets the value at `keyPath` within the dictionary-valued metadata for the given key.
- [func setMetadata(USDToken, keyPath: USDToken, value: Int) throws](usdstage/object/metadatacollection/setmetadata(_:keypath:value:)-8isk6.md)
- [func setMetadata(USDToken, value: Int) throws](usdstage/object/metadatacollection/setmetadata(_:value:)-22f8j.md)
- [func setMetadata(USDToken, value: UInt) throws](usdstage/object/metadatacollection/setmetadata(_:value:)-8hsn7.md)
- [func setMetadata<T>(USDToken, value: T) throws](usdstage/object/metadatacollection/setmetadata(_:value:)-r1j8.md)
  Sets the metadata value for the given key.

## Relationships

### Conforming Types
- [USDPrim](usdprim.md)
- [USDPrim.Attribute](usdprim/attribute.md)
- [USDPrim.Property](usdprim/property.md)
- [USDPrim.Relationship](usdprim/relationship.md)
- [USDStage.Object](usdstage/object.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/object/metadatacollection)*