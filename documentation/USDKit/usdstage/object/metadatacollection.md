# USDStage.Object.MetadataCollection

**Framework**: USDKit  
**Kind**: protocol  
**Role**: Protocol

A scene graph object that possesses metadata.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol MetadataCollection
```

## Overview

Prims, attributes, and relationships may have associated metadata. Metadata on an object is accessed by its name, which is a [`USDToken`](../../usdtoken.md).

> ❗ **Important**: Don’t declare new conformances to MetadataCollection. Only the types provided by the USDStageKit framework are valid conforming types.

## Topics

### Instance Properties
- [var allAuthoredMetadata: Dictionary<USDToken, USDValue>](./metadatacollection/allauthoredmetadata.md)
  Every authored metadata value on this object.
- [var allMetadata: Dictionary<USDToken, USDValue>](./metadatacollection/allmetadata.md)
  Every metadata value on this object, including fallbacks.
- [var assetInfo: Dictionary<String, USDValue>](./metadatacollection/assetinfo.md)
  A dictionary of asset information authored on this object.
- [var customData: Dictionary<String, USDValue>](./metadatacollection/customdata.md)
  A dictionary of custom data authored on this object.
- [var displayName: String](./metadatacollection/displayname.md)
  A non-unique display name authored on this object.
- [var documentation: String](./metadatacollection/documentation.md)
  A human-readable description authored on this object.
- [var hasAssetInfo: Bool](./metadatacollection/hasassetinfo.md)
  A Boolean value that indicates whether this object has asset information.
- [var hasAuthoredAssetInfo: Bool](./metadatacollection/hasauthoredassetinfo.md)
  A Boolean value that indicates whether this object has authored asset information.
- [var hasAuthoredCustomData: Bool](./metadatacollection/hasauthoredcustomdata.md)
  A Boolean value that indicates whether this object has authored custom data.
- [var hasAuthoredDisplayName: Bool](./metadatacollection/hasauthoreddisplayname.md)
  A Boolean value that indicates whether this object has an authored display name.
- [var hasAuthoredDocumentation: Bool](./metadatacollection/hasauthoreddocumentation.md)
  A Boolean value that indicates whether this object has authored documentation.
- [var hasAuthoredHidden: Bool](./metadatacollection/hasauthoredhidden.md)
  A Boolean value that indicates whether this object has an authored `isHidden` opinion.
- [var hasCustomData: Bool](./metadatacollection/hascustomdata.md)
  A Boolean value that indicates whether this object has custom data.
- [var isHidden: Bool](./metadatacollection/ishidden.md)
  A Boolean value that indicates whether this object is hidden from browsing UI.
### Instance Methods
- [func assetInfoByKey(USDToken) -> USDValue?](./metadatacollection/assetinfobykey%28_%29.md)
  Returns the asset information value at the given key path.
- [func clearAssetInfo()](./metadatacollection/clearassetinfo%28%29.md)
  Removes all authored asset information on this object.
- [func clearAssetInfoByKey(USDToken)](./metadatacollection/clearassetinfobykey%28_%29.md)
  Removes the authored asset information value at the given key path.
- [func clearCustomData()](./metadatacollection/clearcustomdata%28%29.md)
  Removes all authored custom data on this object.
- [func clearCustomDataByKey(USDToken)](./metadatacollection/clearcustomdatabykey%28_%29.md)
  Removes the authored custom data value at the given key path.
- [func clearDisplayName()](./metadatacollection/cleardisplayname%28%29.md)
  Removes the authored display name on this object.
- [func clearDocumentation()](./metadatacollection/cleardocumentation%28%29.md)
  Removes the authored documentation on this object.
- [func clearHidden()](./metadatacollection/clearhidden%28%29.md)
  Removes the authored `isHidden` opinion on this object.
- [func clearMetadata(USDToken) throws](./metadatacollection/clearmetadata%28_%29.md)
  Removes the authored metadata value for the given key.
- [func clearMetadata(USDToken, keyPath: USDToken) throws](./metadatacollection/clearmetadata%28_,keypath%29.md)
  Removes the authored value at `keyPath` within the dictionary-valued metadata for the given key.
- [func customDataByKey(USDToken) -> USDValue?](./metadatacollection/customdatabykey%28_%29.md)
  Returns the custom data value at the given key path.
- [func hasAssetInfoByKey(USDToken) -> Bool](./metadatacollection/hasassetinfobykey%28_%29.md)
  Returns a Boolean value that indicates whether asset information exists at the given key path.
- [func hasAuthoredAssetInfoByKey(USDToken) -> Bool](./metadatacollection/hasauthoredassetinfobykey%28_%29.md)
  Returns a Boolean value that indicates whether authored asset information exists at the given key path.
- [func hasAuthoredCustomDataByKey(USDToken) -> Bool](./metadatacollection/hasauthoredcustomdatabykey%28_%29.md)
  Returns a Boolean value that indicates whether authored custom data exists at the given key path.
- [func hasAuthoredMetadata(USDToken) -> Bool](./metadatacollection/hasauthoredmetadata%28_%29.md)
  Returns a Boolean value that indicates whether metadata for the given key has an authored value.
- [func hasAuthoredMetadata(USDToken, keyPath: USDToken) -> Bool](./metadatacollection/hasauthoredmetadata%28_,keypath%29.md)
  Returns a Boolean value that indicates whether the dictionary-valued metadata for the given key has an authored value at `keyPath`.
- [func hasCustomDataByKey(USDToken) -> Bool](./metadatacollection/hascustomdatabykey%28_%29.md)
  Returns a Boolean value that indicates whether custom data exists at the given key path.
- [func hasMetadata(USDToken) -> Bool](./metadatacollection/hasmetadata%28_%29.md)
  Returns a Boolean value that indicates whether metadata for the given key has a value, including its fallback.
- [func hasMetadata(USDToken, keyPath: USDToken) -> Bool](./metadatacollection/hasmetadata%28_,keypath%29.md)
  Returns a Boolean value that indicates whether the dictionary-valued metadata for the given key has a value at `keyPath`.
- [func metadata(USDToken) -> UInt?](./metadatacollection/metadata%28_%29-136hk.md)
- [func metadata<T>(USDToken) -> T?](./metadatacollection/metadata%28_%29-574ho.md)
  Returns the metadata value for the given key.
- [func metadata(USDToken) -> Int?](./metadatacollection/metadata%28_%29-8jz5b.md)
- [func metadata(USDToken, keyPath: USDToken) -> UInt?](./metadatacollection/metadata%28_,keypath%29-5pid3.md)
- [func metadata<T>(USDToken, keyPath: USDToken) -> T?](./metadatacollection/metadata%28_,keypath%29-62uj1.md)
  Returns the value at `keyPath` within the dictionary-valued metadata for the given key.
- [func metadata(USDToken, keyPath: USDToken) -> Int?](./metadatacollection/metadata%28_,keypath%29-8isq8.md)
- [func setAssetInfoByKey(USDToken, value: USDValue)](./metadatacollection/setassetinfobykey%28_,value%29.md)
  Sets the asset information value at the given key path.
- [func setCustomDataByKey(USDToken, value: USDValue)](./metadatacollection/setcustomdatabykey%28_,value%29.md)
  Modifies the custom data value at the given key path.
- [func setMetadata(USDToken, keyPath: USDToken, value: UInt) throws](./metadatacollection/setmetadata%28_,keypath,value%29-1ri3i.md)
- [func setMetadata<T>(USDToken, keyPath: USDToken, value: T) throws](./metadatacollection/setmetadata%28_,keypath,value%29-62b48.md)
  Sets the value at `keyPath` within the dictionary-valued metadata for the given key.
- [func setMetadata(USDToken, keyPath: USDToken, value: Int) throws](./metadatacollection/setmetadata%28_,keypath,value%29-8isk6.md)
- [func setMetadata(USDToken, value: Int) throws](./metadatacollection/setmetadata%28_,value%29-22f8j.md)
- [func setMetadata(USDToken, value: UInt) throws](./metadatacollection/setmetadata%28_,value%29-8hsn7.md)
- [func setMetadata<T>(USDToken, value: T) throws](./metadatacollection/setmetadata%28_,value%29-r1j8.md)
  Sets the metadata value for the given key.

## Relationships

### Conforming Types
- [USDPrim](../../usdprim.md)
- [USDPrim.Attribute](../../usdprim/attribute.md)
- [USDPrim.Property](../../usdprim/property.md)
- [USDPrim.Relationship](../../usdprim/relationship.md)
- [USDStage.Object](../object.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/object/metadatacollection)*