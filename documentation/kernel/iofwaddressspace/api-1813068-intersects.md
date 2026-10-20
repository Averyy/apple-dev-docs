# intersects

**Framework**: Kernel  
**Kind**: instm

Checks this address space intersects with the given address range. Currently only supports IOFWPsuedoAddressSpaces.

## Declaration

```c
inline bool intersects(
 IOFWAddressSpace *space )
```

#### Return Value

True if the address spaces intersect false otherwise

## Parameters

- `space`: An address space to compare against

## See Also

### Miscellaneous
- [activate](./api-1812970-activate.md)
  Address space is ready for handling requests.
- [addTrustedNode](./api-1812980-addtrustednode.md)
  Add a trusted node.
- [contains](./api-1812994-contains.md)
  returns number of bytes starting at addr in this space
- [deactivate](./api-1813008-deactivate.md)
  Address space request handler is disabled.
- [doLock](./api-1813019-dolock.md)
  A method for processing a lock request.
- [doRead](./api-1813035-doread.md)
  An abstract method for processing an address space read request
- [doWrite](./api-1813050-dowrite.md)
  An abstract method for processing an address space write request
- [isExclusive](./api-1813086-isexclusive.md)
  Checks if an address space wants exclusive control of its address range
- [isTrustedNode](./api-1813105-istrustednode.md)
  returns true if the node is added as a trusted node
- [removeAllTrustedNodes](./api-1813134-removealltrustednodes.md)
  Remove all trusted nodes.
- [removeTrustedNode](./api-1813152-removetrustednode.md)
  Remove a trusted node.
- [setExclusive](./api-1813180-setexclusive.md)
  Sets if this address space requires exclusive control of its address range. Exclusivity should be set before an address space is activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwaddressspace/1813068-intersects)*