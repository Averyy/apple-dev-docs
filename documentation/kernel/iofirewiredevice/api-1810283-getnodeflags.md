# getNodeFlags

**Framework**: Kernel  
**Kind**: instm

Retrieves the node's characteristics.

## Declaration

```swift
virtual UInt32 getNodeFlags(
 flags );
```

#### Return_value

UInt32 The flags set for a particular node.

## Parameters

- `flags`: Refer to "node flags" in IOFireWireFamilyCommon.h.

## See Also

- [clearNodeFlags](iofirewiredevice/1810239-clearnodeflags.md)
  Resets the node's characteristics.
- [createPhysicalAddressSpace](iofirewiredevice/1810254-createphysicaladdressspace.md)
  Creates local physical FireWire address spaces for the device to access.
- [createPseudoAddressSpace](iofirewiredevice/1810271-createpseudoaddressspace.md)
  Creates local pseudo FireWire address spaces for the device to access.
- [getUnitCount](iofirewiredevice/1810297-getunitcount.md)
  Returns number of units attached to this device.
- [init](iofirewiredevice/1810312-init.md)
  Initializes the nub.
- [setMaxSpeed](iofirewiredevice/1810324-setmaxspeed.md)
  Sets the maximum speed for this node.
- [setNodeFlags](iofirewiredevice/1810338-setnodeflags.md)
  Sets the node's characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiredevice/1810283-getnodeflags)*