# setARxReqIntCompleteHandler

**Framework**: Kernel  
**Kind**: instm

Installs a callback to receive notification, when FWIM has completed ARxReqInt processing and no incoming packets are left in the queue.

## Declaration

```c
inline void setARxReqIntCompleteHandler(
 void *refcon,
 IOFWARxReqIntCompleteHandlerhandler )
```

#### Return Value

none.

## Parameters

- `refcon`: Client's callback object.
- `handler`: Client callback to be invoked, at the end of interrupt processing.

## See Also

### Miscellaneous
- [contains](./api-1813836-contains.md)
  returns number of bytes starting at addr in this space
- [doRead](./api-1813839-doread.md)
  A method for processing an address space read request
- [doWrite](./api-1813844-dowrite.md)
  A method for processing an address space write request
- [initAll](./api-1813848-initall.md)
  Initialize an address space object to handle r/w memory
- [initFixed](./api-1813852-initfixed.md)
  Initialize a fixed address space at top of kCSRRegisterSpaceBaseAddressHi
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwpseudoaddressspace/1813855-setarxreqintcompletehandler)*