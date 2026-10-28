# initAll

**Framework**: Kernel  
**Kind**: instm

Initialize an address space object to handle r/w memory

## Declaration

```cpp
virtual bool initAll( 
 IOFireWireBus *bus, 
 FWAddress *addr, 
 UInt32len, 
 FWReadCallbackreader, 
 FWWriteCallbackwriter, 
 void *refcon);
```

## Return Value

returns true on success, false on failure

## Parameters

- `bus`: Points to IOFireWireBus object.
- `addr`: Points to starting address for the Pseudo Address Space.
- `len`: Length of the Pseudo Address Space.
- `reader`: Callback handler for incoming Read.
- `writer`: Callback handler for incoming Write.
- `refcon`: Client's callback object.

## See Also

### Miscellaneous
- [contains](./api-1813836-contains.md)
  returns number of bytes starting at addr in this space
- [doRead](./api-1813839-doread.md)
  A method for processing an address space read request
- [doWrite](./api-1813844-dowrite.md)
  A method for processing an address space write request
- [initFixed](./api-1813852-initfixed.md)
  Initialize a fixed address space at top of kCSRRegisterSpaceBaseAddressHi
- [setARxReqIntCompleteHandler](./api-1813855-setarxreqintcompletehandler.md)
  Installs a callback to receive notification, when FWIM has completed ARxReqInt processing and no incoming packets are left in the queue.
- [simpleRead](./api-1813859-simpleread.md)
  Create an address space object to handle read-only memory (eg. the local ROM) handles everything itself
- [simpleReader](./api-1813862-simplereader.md)
  A method for processing an address space read request
- [simpleReadFixed](./api-1813866-simplereadfixed.md)
  Create an address space object to handle fixed read-only memory (eg. the local ROM) handles everything itself
- [simpleRW(IOFireWireBus *, FWAddress *, IOMemoryDescriptor *)](./api-1813868-simplerw.md)
  Create an address space object to handle r/w memory handles everything itself
- [simpleRW(IOFireWireBus *, FWAddress *, UInt32, void *)](./api-1813871-simplerw.md)
  Create an address space object to handle r/w memory handles everything itself
- [simpleRWFixed](./api-1813874-simplerwfixed.md)
  Create a Read/Write fixed address space at top of kCSRRegisterSpaceBaseAddressHi.
- [simpleWriter](./api-1813878-simplewriter.md)
  A method for processing an address space write request


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwpseudoaddressspace/1813848-initall)*