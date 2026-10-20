# setMaxSpeed

**Framework**: Kernel  
**Kind**: instm

Sets the maximum speed for this node.

## Declaration

```c
inline void setMaxSpeed(
 IOFWSpeedspeed )
```

## Parameters

- `speed`: Maximum speed. Refer to "bus speed numbers" in IOFireWireFamilyCommon.h.

## See Also

### Miscellaneous
- [clearNodeFlags](./api-1810239-clearnodeflags.md)
  Resets the node's characteristics.
- [createPhysicalAddressSpace](./api-1810254-createphysicaladdressspace.md)
  Creates local physical FireWire address spaces for the device to access.
- [createPseudoAddressSpace](./api-1810271-createpseudoaddressspace.md)
  Creates local pseudo FireWire address spaces for the device to access.
- [getNodeFlags](./api-1810283-getnodeflags.md)
  Retrieves the node's characteristics.
- [getUnitCount](./api-1810297-getunitcount.md)
  Returns number of units attached to this device.
- [init](./api-1810312-init.md)
  Initializes the nub.
- [setNodeFlags](./api-1810338-setnodeflags.md)
  Sets the node's characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiredevice/1810324-setmaxspeed)*