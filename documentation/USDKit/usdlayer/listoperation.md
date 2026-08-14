# USDLayer.ListOperation

**Framework**: USDKit  
**Kind**: struct

A non-destructive list of incremental editing operations for list-valued metadata and properties.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ListOperation<T> where T : USDLayer._ListOperationElement
```

## Topics

### Initializers
- [init(explicitItems: [T])](usdlayer/listoperation/init(explicititems:)-4klr9.md)
  Creates an explicit-mode list operation with the given items.
- [init(explicitItems: [Int])](usdlayer/listoperation/init(explicititems:)-6l0al.md)
- [init(explicitItems: [UInt])](usdlayer/listoperation/init(explicititems:)-7iesv.md)
- [init(prependedItems: [T], appendedItems: [T], deletedItems: [T])](usdlayer/listoperation/init(prependeditems:appendeditems:deleteditems:)-1tkyo.md)
  Creates a list operation with the given prepended/appended/deleted items. Pass no arguments for an empty operation with no slots authored.
- [init(prependedItems: [Int], appendedItems: [Int], deletedItems: [Int])](usdlayer/listoperation/init(prependeditems:appendeditems:deleteditems:)-8poys.md)
- [init(prependedItems: [UInt], appendedItems: [UInt], deletedItems: [UInt])](usdlayer/listoperation/init(prependeditems:appendeditems:deleteditems:)-ngyh.md)
### Instance Properties
- [var appliedItems: [T]](usdlayer/listoperation/applieditems.md)
  The composed result of applying all operations from strongest to weakest opinion.
- [var hasKeys: Bool](usdlayer/listoperation/haskeys.md)
  Whether any operation slot has been authored.
- [var isExplicit: Bool](usdlayer/listoperation/isexplicit.md)
  Whether the operation is in explicit mode — i.e., its items replace the entire list during composition.
### Instance Methods
- [func clear()](usdlayer/listoperation/clear.md)
  Removes all authored slots, leaving an empty operation.
- [func clearAndMakeExplicit()](usdlayer/listoperation/clearandmakeexplicit.md)
  Removes all authored slots and switches to explicit mode with no items.
- [func compose(stronger: USDLayer.ListOperation<T>, for: USDLayer.ListOperationType)](usdlayer/listoperation/compose(stronger:for:).md)
  Composes a stronger operation into this one for the given slot.
- [func has(item: T) -> Bool](usdlayer/listoperation/has(item:).md)
  Returns a Boolean value that indicates whether `item` appears in any slot of this operation.
- [func items(for: USDLayer.ListOperationType) -> [T]](usdlayer/listoperation/items(for:).md)
  Returns the items in the given operation’s slot.
- [func replaceItems(in: USDLayer.ListOperationType, at: Int, count: Int, with: [T]) throws](usdlayer/listoperation/replaceitems(in:at:count:with:).md)
  Replaces `count` items in `operation`’s slot starting at `index` with `newItems`.
- [func setItems([T], for: USDLayer.ListOperationType) throws](usdlayer/listoperation/setitems(_:for:).md)
  Sets the items in the given operation’s slot.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [USDValueProtocol](usdvalueprotocol.md)

## See Also

- [func copy(from: USDLayer.Path, to: USDLayer.Path, in: USDLayer?) -> Bool](usdlayer/copy(from:to:in:).md)
  Copies the spec at `srcPath` in this layer (and its children) to `dstPath`.
- [USDLayer.ListOperationType](usdlayer/listoperationtype.md)
  Identifies an operation slot in a [`USDLayer.ListOperation`](usdlayer/listoperation.md).
- [typealias Relocate](usdlayer/relocate.md)
  A single path relocation from source to target.
- [typealias RelocatesMap](usdlayer/relocatesmap.md)
  A mapping from source paths to target paths for relocations.
- [USDLayer.ChangeList](usdlayer/changelist.md)
  A list of changes made to a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/listoperation)*