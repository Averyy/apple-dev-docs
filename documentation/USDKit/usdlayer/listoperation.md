# USDLayer.ListOperation

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A non-destructive list of incremental editing operations for list-valued metadata and properties.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ListOperation<T> where T : USDLayer._ListOperationElement
```

## Topics

### Initializers
- [init(explicitItems: [T])](./listoperation/init%28explicititems%29-4klr9.md)
  Creates an explicit-mode list operation with the given items.
- [init(explicitItems: [Int])](./listoperation/init%28explicititems%29-6l0al.md)
- [init(explicitItems: [UInt])](./listoperation/init%28explicititems%29-7iesv.md)
- [init(prependedItems: [T], appendedItems: [T], deletedItems: [T])](./listoperation/init%28prependeditems,appendeditems,deleteditems%29-1tkyo.md)
  Creates a list operation with the given prepended/appended/deleted items. Pass no arguments for an empty operation with no slots authored.
- [init(prependedItems: [Int], appendedItems: [Int], deletedItems: [Int])](./listoperation/init%28prependeditems,appendeditems,deleteditems%29-8poys.md)
- [init(prependedItems: [UInt], appendedItems: [UInt], deletedItems: [UInt])](./listoperation/init%28prependeditems,appendeditems,deleteditems%29-ngyh.md)
### Instance Properties
- [var appliedItems: [T]](./listoperation/applieditems.md)
  The composed result of applying all operations from strongest to weakest opinion.
- [var hasKeys: Bool](./listoperation/haskeys.md)
  Whether any operation slot has been authored.
- [var isExplicit: Bool](./listoperation/isexplicit.md)
  Whether the operation is in explicit mode — i.e., its items replace the entire list during composition.
### Instance Methods
- [func clear()](./listoperation/clear%28%29.md)
  Removes all authored slots, leaving an empty operation.
- [func clearAndMakeExplicit()](./listoperation/clearandmakeexplicit%28%29.md)
  Removes all authored slots and switches to explicit mode with no items.
- [func compose(stronger: USDLayer.ListOperation<T>, for: USDLayer.ListOperationType)](./listoperation/compose%28stronger,for%29.md)
  Composes a stronger operation into this one for the given slot.
- [func has(item: T) -> Bool](./listoperation/has%28item%29.md)
  Returns a Boolean value that indicates whether `item` appears in any slot of this operation.
- [func items(for: USDLayer.ListOperationType) -> [T]](./listoperation/items%28for%29.md)
  Returns the items in the given operation’s slot.
- [func replaceItems(in: USDLayer.ListOperationType, at: Int, count: Int, with: [T]) throws](./listoperation/replaceitems%28in,at,count,with%29.md)
  Replaces `count` items in `operation`’s slot starting at `index` with `newItems`.
- [func setItems([T], for: USDLayer.ListOperationType) throws](./listoperation/setitems%28_,for%29.md)
  Sets the items in the given operation’s slot.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [USDValueProtocol](../usdvalueprotocol.md)

## See Also

### Editing scene description
- [func copy(from: USDLayer.Path, to: USDLayer.Path, in: USDLayer?) -> Bool](./copy%28from,to,in%29.md)
  Copies the spec at `srcPath` in this layer (and its children) to `dstPath`.
- [USDLayer.ListOperationType](./listoperationtype.md)
  Identifies an operation slot in a [`USDLayer.ListOperation`](./listoperation.md).
- [typealias Relocate](./relocate.md)
  A single path relocation from source to target.
- [typealias RelocatesMap](./relocatesmap.md)
  A mapping from source paths to target paths for relocations.
- [USDLayer.ChangeList](./changelist.md)
  A list of changes made to a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/listoperation)*