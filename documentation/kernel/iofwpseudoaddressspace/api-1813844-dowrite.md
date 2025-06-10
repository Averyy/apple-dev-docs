# doWrite

**Framework**: Kernel  
**Kind**: instm

A method for processing an address space write request

## Declaration

```swift
virtual UInt32 doWrite( 
 UInt16nodeID, 
 IOFWSpeed& speed, 
 FWAddressaddr, 
 UInt32len, 
 const void *buf, 
 IOFWRequestRefConreqrefcon);
```

#### Return_value

UIn32 returns kFWResponseComplete on success

## Parameters

- `nodeID`: FireWire Write to nodeID.
- `speed`: at this 'speed'.
- `addr`: with FireWire address 'addr'.
- `len`: write 'len' bytes to nodeID.
- `buf`: obtain bytes from location given by 'buf'.
- `reqrefcon`: Can be queried for extra info about the request.

## See Also

- [contains](iofwpseudoaddressspace/1813836-contains.md)
  returns number of bytes starting at addr in this space
- [doRead](iofwpseudoaddressspace/1813839-doread.md)
  A method for processing an address space read request
- [initAll](iofwpseudoaddressspace/1813848-initall.md)
  Initialize an address space object to handle r/w memory
- [initFixed](iofwpseudoaddressspace/1813852-initfixed.md)
  Initialize a fixed address space at top of kCSRRegisterSpaceBaseAddressHi
- [setARxReqIntCompleteHandler](iofwpseudoaddressspace/1813855-setarxreqintcompletehandler.md)
  Installs a callback to receive notification, when FWIM has completed ARxReqInt processing and no incoming packets are left in the queue.
- [simpleRead](iofwpseudoaddressspace/1813859-simpleread.md)
  Create an address space object to handle read-only memory (eg. the local ROM) handles everything itself
- [simpleReader](iofwpseudoaddressspace/1813862-simplereader.md)
  A method for processing an address space read request
- [simpleReadFixed](iofwpseudoaddressspace/1813866-simplereadfixed.md)
  Create an address space object to handle fixed read-only memory (eg. the local ROM) handles everything itself
- [simpleRW(IOFireWireBus *, FWAddress *, IOMemoryDescriptor *)](iofwpseudoaddressspace/1813868-simplerw.md)
  Create an address space object to handle r/w memory handles everything itself
- [simpleRW(IOFireWireBus *, FWAddress *, UInt32, void *)](iofwpseudoaddressspace/1813871-simplerw.md)
  Create an address space object to handle r/w memory handles everything itself
- [simpleRWFixed](iofwpseudoaddressspace/1813874-simplerwfixed.md)
  Create a Read/Write fixed address space at top of kCSRRegisterSpaceBaseAddressHi.
- [simpleWriter](iofwpseudoaddressspace/1813878-simplewriter.md)
  A method for processing an address space write request


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwpseudoaddressspace/1813844-dowrite)*