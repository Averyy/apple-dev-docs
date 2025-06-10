# createPseudoAddressSpace

**Framework**: Kernel  
**Kind**: instm

Creates local pseudo FireWire address spaces for the device to access.

## Declaration

```swift
virtual IOFWPseudoAddressSpace *createPseudoAddressSpace(
 FWAddress *addr,
 UInt32len, 
 FWReadCallbackreader,
 FWWriteCallbackwriter,
 void *refcon);
```

#### Return_value

A valid `IOFWPseudoAddressSpace` object on success; NULL on failure.

## Parameters

- `addr`: The FireWire address that is mapped to the pseudo address access.
- `len`: Size of the address space to allocate.
- `reader`: Read callback, when the device reads from this address space.
- `writer`: Write callback, when the device writes to this address space.
- `refcon`: Client's callback object returned during reader/writer callbacks.

## See Also

- [clearNodeFlags](iofirewiredevice/1810239-clearnodeflags.md)
  Resets the node's characteristics.
- [createPhysicalAddressSpace](iofirewiredevice/1810254-createphysicaladdressspace.md)
  Creates local physical FireWire address spaces for the device to access.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiredevice/1810271-createpseudoaddressspace)*