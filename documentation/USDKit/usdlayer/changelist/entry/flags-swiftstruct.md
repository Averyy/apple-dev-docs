# USDLayer.ChangeList.Entry.Flags

**Framework**: USDKit  
**Kind**: struct

Boolean flags describing structural changes to a spec.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Flags
```

## Topics

### Instance Properties
- [var didAddInertPrim: Bool](usdlayer/changelist/entry/flags-swift.struct/didaddinertprim.md)
  Whether an inert prim spec was added.
- [var didAddNonInertPrim: Bool](usdlayer/changelist/entry/flags-swift.struct/didaddnoninertprim.md)
  Whether a non-inert prim spec was added.
- [var didAddProperty: Bool](usdlayer/changelist/entry/flags-swift.struct/didaddproperty.md)
  Whether a property was added.
- [var didAddPropertyWithOnlyRequiredFields: Bool](usdlayer/changelist/entry/flags-swift.struct/didaddpropertywithonlyrequiredfields.md)
  Whether a property with only required fields was added.
- [var didAddTarget: Bool](usdlayer/changelist/entry/flags-swift.struct/didaddtarget.md)
  Whether a target was added to a relationship.
- [var didChangeAttributeConnection: Bool](usdlayer/changelist/entry/flags-swift.struct/didchangeattributeconnection.md)
  Whether an attribute’s connection targets changed.
- [var didChangeAttributeTimeSamples: Bool](usdlayer/changelist/entry/flags-swift.struct/didchangeattributetimesamples.md)
  Whether an attribute’s time samples changed.
- [var didChangeIdentifier: Bool](usdlayer/changelist/entry/flags-swift.struct/didchangeidentifier.md)
  Whether the layer’s identifier changed.
- [var didChangePrimInheritPaths: Bool](usdlayer/changelist/entry/flags-swift.struct/didchangepriminheritpaths.md)
  Whether a prim’s inherit paths list changed.
- [var didChangePrimReferences: Bool](usdlayer/changelist/entry/flags-swift.struct/didchangeprimreferences.md)
  Whether a prim’s references list changed.
- [var didChangePrimSpecializes: Bool](usdlayer/changelist/entry/flags-swift.struct/didchangeprimspecializes.md)
  Whether a prim’s specializes list changed.
- [var didChangePrimVariantSets: Bool](usdlayer/changelist/entry/flags-swift.struct/didchangeprimvariantsets.md)
  Whether a prim’s variant sets list changed.
- [var didChangeRelationshipTargets: Bool](usdlayer/changelist/entry/flags-swift.struct/didchangerelationshiptargets.md)
  Whether a relationship’s target list changed.
- [var didChangeResolvedPath: Bool](usdlayer/changelist/entry/flags-swift.struct/didchangeresolvedpath.md)
  Whether the layer’s resolved path changed.
- [var didReloadContent: Bool](usdlayer/changelist/entry/flags-swift.struct/didreloadcontent.md)
  Whether the layer was reloaded from its source.
- [var didRemoveInertPrim: Bool](usdlayer/changelist/entry/flags-swift.struct/didremoveinertprim.md)
  Whether an inert prim spec was removed.
- [var didRemoveNonInertPrim: Bool](usdlayer/changelist/entry/flags-swift.struct/didremovenoninertprim.md)
  Whether a non-inert prim spec was removed.
- [var didRemoveProperty: Bool](usdlayer/changelist/entry/flags-swift.struct/didremoveproperty.md)
  Whether a property was removed.
- [var didRemovePropertyWithOnlyRequiredFields: Bool](usdlayer/changelist/entry/flags-swift.struct/didremovepropertywithonlyrequiredfields.md)
  Whether a property with only required fields was removed.
- [var didRemoveTarget: Bool](usdlayer/changelist/entry/flags-swift.struct/didremovetarget.md)
  Whether a target was removed from a relationship.
- [var didRename: Bool](usdlayer/changelist/entry/flags-swift.struct/didrename.md)
  Whether a spec was renamed.
- [var didReorderChildren: Bool](usdlayer/changelist/entry/flags-swift.struct/didreorderchildren.md)
  Whether the children list of a prim was reordered.
- [var didReorderProperties: Bool](usdlayer/changelist/entry/flags-swift.struct/didreorderproperties.md)
  Whether the properties list of a prim was reordered.
- [var didReplaceContent: Bool](usdlayer/changelist/entry/flags-swift.struct/didreplacecontent.md)
  Whether the layer’s content was replaced.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Escapable](../swift/escapable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/changelist/entry/flags-swift.struct)*