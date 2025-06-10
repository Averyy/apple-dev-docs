# createPhysicalAddressSpace

**Framework**: Kernel  
**Kind**: instm

Creates local physical FireWire address spaces for the device to access.

## Declaration

```swift
virtual IOFWPhysicalAddressSpace *createPhysicalAddressSpace(
 IOMemoryDescriptor *mem);
```

#### Return_value

A valid `IOFWPhysicalAddressSpace` object on success; NULL on failure.

## Parameters

- `mem`: Memory area allocated to back the physical access by Link hardware.

## See Also

- [clearNodeFlags](iofirewiredevice/1810239-clearnodeflags.md)
  Resets the node's characteristics.
- [createPseudoAddressSpace](iofirewiredevice/1810271-createpseudoaddressspace.md)
  Creates local pseudo FireWire address spaces for the device to access.
- [getNodeFlags](iofirewiredevice/1810283-getnodeflags.md)
  Retrieves the node's characteristics.
- [getUnitCount](iofirewiredevice/1810297-getunitcount.md)
  Returns number of units attached to this device.
- [init](iofirewiredevice/1810312-init.md)
  Initializes the nub.
- [setMaxSpeed](iofirewiredevice/1810324-setmaxspeed.md)
  Sets the maximum speed for this node.
- [setNodeFlags](iofirewiredevice/1810338-setnodeflags.md)
  Sets the node's characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiredevice/1810254-createphysicaladdressspace)*