# initFixed

**Framework**: Kernel  
**Kind**: instm

Initialize a fixed address space at top of kCSRRegisterSpaceBaseAddressHi

## Declaration

```swift
virtual bool initFixed( 
 IOFireWireBus *bus, 
 FWAddress addr, 
 UInt32 len, 
 FWReadCallback reader, 
 FWWriteCallback writer, 
 void *refcon);
```

#### Return_value

returns true on success, false on failure

## Parameters

- `bus`: Points to IOFireWireBus object.
- `addr`: Points to starting address for the Pseudo Address Space.
- `reader`: Callback handler for incoming Read.
- `writer`: Callback handler for incoming Write.
- `refcon`: Client's callback object.

## See Also

- [contains](iofwpseudoaddressspace/1813836-contains.md)
  returns number of bytes starting at addr in this space
- [doRead](iofwpseudoaddressspace/1813839-doread.md)
  A method for processing an address space read request
- [doWrite](iofwpseudoaddressspace/1813844-dowrite.md)
  A method for processing an address space write request
- [initAll](iofwpseudoaddressspace/1813848-initall.md)
  Initialize an address space object to handle r/w memory
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwpseudoaddressspace/1813852-initfixed)*