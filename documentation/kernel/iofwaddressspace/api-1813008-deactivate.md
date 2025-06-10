# deactivate

**Framework**: Kernel  
**Kind**: instm

Address space request handler is disabled.

## Declaration

```swift
virtual void deactivate();
```

#### Return_value

none

## See Also

- [activate](iofwaddressspace/1812970-activate.md)
  Address space is ready for handling requests.
- [addTrustedNode](iofwaddressspace/1812980-addtrustednode.md)
  Add a trusted node.
- [contains](iofwaddressspace/1812994-contains.md)
  returns number of bytes starting at addr in this space
- [doLock](iofwaddressspace/1813019-dolock.md)
  A method for processing a lock request.
- [doRead](iofwaddressspace/1813035-doread.md)
  An abstract method for processing an address space read request
- [doWrite](iofwaddressspace/1813050-dowrite.md)
  An abstract method for processing an address space write request
- [intersects](iofwaddressspace/1813068-intersects.md)
  Checks this address space intersects with the given address range. Currently only supports IOFWPsuedoAddressSpaces.
- [isExclusive](iofwaddressspace/1813086-isexclusive.md)
  Checks if an address space wants exclusive control of its address range
- [isTrustedNode](iofwaddressspace/1813105-istrustednode.md)
  returns true if the node is added as a trusted node
- [removeAllTrustedNodes](iofwaddressspace/1813134-removealltrustednodes.md)
  Remove all trusted nodes.
- [removeTrustedNode](iofwaddressspace/1813152-removetrustednode.md)
  Remove a trusted node.
- [setExclusive](iofwaddressspace/1813180-setexclusive.md)
  Sets if this address space requires exclusive control of its address range. Exclusivity should be set before an address space is activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwaddressspace/1813008-deactivate)*