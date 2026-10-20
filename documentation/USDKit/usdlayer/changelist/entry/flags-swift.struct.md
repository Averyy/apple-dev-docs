# USDLayer.ChangeList.Entry.Flags

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

Boolean flags describing structural changes to a spec.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Flags
```

## Topics

### Instance Properties
- [var didAddInertPrim: Bool](./flags-swift.struct/didaddinertprim.md)
  Whether an inert prim spec was added.
- [var didAddNonInertPrim: Bool](./flags-swift.struct/didaddnoninertprim.md)
  Whether a non-inert prim spec was added.
- [var didAddProperty: Bool](./flags-swift.struct/didaddproperty.md)
  Whether a property was added.
- [var didAddPropertyWithOnlyRequiredFields: Bool](./flags-swift.struct/didaddpropertywithonlyrequiredfields.md)
  Whether a property with only required fields was added.
- [var didAddTarget: Bool](./flags-swift.struct/didaddtarget.md)
  Whether a target was added to a relationship.
- [var didChangeAttributeConnection: Bool](./flags-swift.struct/didchangeattributeconnection.md)
  Whether an attribute’s connection targets changed.
- [var didChangeAttributeTimeSamples: Bool](./flags-swift.struct/didchangeattributetimesamples.md)
  Whether an attribute’s time samples changed.
- [var didChangeIdentifier: Bool](./flags-swift.struct/didchangeidentifier.md)
  Whether the layer’s identifier changed.
- [var didChangePrimInheritPaths: Bool](./flags-swift.struct/didchangepriminheritpaths.md)
  Whether a prim’s inherit paths list changed.
- [var didChangePrimReferences: Bool](./flags-swift.struct/didchangeprimreferences.md)
  Whether a prim’s references list changed.
- [var didChangePrimSpecializes: Bool](./flags-swift.struct/didchangeprimspecializes.md)
  Whether a prim’s specializes list changed.
- [var didChangePrimVariantSets: Bool](./flags-swift.struct/didchangeprimvariantsets.md)
  Whether a prim’s variant sets list changed.
- [var didChangeRelationshipTargets: Bool](./flags-swift.struct/didchangerelationshiptargets.md)
  Whether a relationship’s target list changed.
- [var didChangeResolvedPath: Bool](./flags-swift.struct/didchangeresolvedpath.md)
  Whether the layer’s resolved path changed.
- [var didReloadContent: Bool](./flags-swift.struct/didreloadcontent.md)
  Whether the layer was reloaded from its source.
- [var didRemoveInertPrim: Bool](./flags-swift.struct/didremoveinertprim.md)
  Whether an inert prim spec was removed.
- [var didRemoveNonInertPrim: Bool](./flags-swift.struct/didremovenoninertprim.md)
  Whether a non-inert prim spec was removed.
- [var didRemoveProperty: Bool](./flags-swift.struct/didremoveproperty.md)
  Whether a property was removed.
- [var didRemovePropertyWithOnlyRequiredFields: Bool](./flags-swift.struct/didremovepropertywithonlyrequiredfields.md)
  Whether a property with only required fields was removed.
- [var didRemoveTarget: Bool](./flags-swift.struct/didremovetarget.md)
  Whether a target was removed from a relationship.
- [var didRename: Bool](./flags-swift.struct/didrename.md)
  Whether a spec was renamed.
- [var didReorderChildren: Bool](./flags-swift.struct/didreorderchildren.md)
  Whether the children list of a prim was reordered.
- [var didReorderProperties: Bool](./flags-swift.struct/didreorderproperties.md)
  Whether the properties list of a prim was reordered.
- [var didReplaceContent: Bool](./flags-swift.struct/didreplacecontent.md)
  Whether the layer’s content was replaced.

## Relationships

### Conforms To
- [Copyable](../../../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../../../Swift/customstringconvertible.md)
- [Escapable](../../../../Swift/escapable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/changelist/entry/flags-swift.struct)*