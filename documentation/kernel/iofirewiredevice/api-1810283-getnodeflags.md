# getNodeFlags

**Framework**: Kernel  
**Kind**: instm

Retrieves the node's characteristics.

## Declaration

```cpp
virtual UInt32 getNodeFlags(
 flags );
```

#### Return Value

UInt32 The flags set for a particular node.

## Parameters

- `flags`: Refer to "node flags" in IOFireWireFamilyCommon.h.

## See Also

### Miscellaneous
- [clearNodeFlags](./api-1810239-clearnodeflags.md)
  Resets the node's characteristics.
- [createPhysicalAddressSpace](./api-1810254-createphysicaladdressspace.md)
  Creates local physical FireWire address spaces for the device to access.
- [createPseudoAddressSpace](./api-1810271-createpseudoaddressspace.md)
  Creates local pseudo FireWire address spaces for the device to access.
- [getUnitCount](./api-1810297-getunitcount.md)
  Returns number of units attached to this device.
- [init](./api-1810312-init.md)
  Initializes the nub.
- [setMaxSpeed](./api-1810324-setmaxspeed.md)
  Sets the maximum speed for this node.
- [setNodeFlags](./api-1810338-setnodeflags.md)
  Sets the node's characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiredevice/1810283-getnodeflags)*