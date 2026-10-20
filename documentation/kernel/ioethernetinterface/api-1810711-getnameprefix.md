# getNamePrefix

**Framework**: Kernel  
**Kind**: instm

Returns a string containing the prefix to use when creating a BSD name for this interface.

## Declaration

```cpp
virtual const char * getNamePrefix() const;
```

#### Return Value

Returns a pointer to a constant C string "en". Therefore, Ethernet interfaces will be registered with BSD as en0, en1, etc.

#### Overview

The BSD name for each interface object is created by concatenating a string returned by this method, with an unique unit number assigned by IONetworkStack.

## See Also

### Miscellaneous
- [controllerDidChangePowerState](./api-1810626-controllerdidchangepowerstate.md)
  Handles a notification that the network controller servicing this interface object has transitioned to a new power state.
- [controllerDidOpen](./api-1810636-controllerdidopen.md)
  A notification that the interface has opened the network controller.
- [controllerWillChangePowerState](./api-1810670-controllerwillchangepowerstate.md)
  Handles a notification that the network controller servicing this interface object is about to transition to a new power state.
- [controllerWillClose](./api-1810684-controllerwillclose.md)
  A notification that the interface will close the network controller.
- [free](./api-1810696-free.md)
  Frees the IOEthernetInterface instance.
- [init](./api-1810722-init.md)
  Initializes an IOEthernetInterface instance.
- [performCommand](./api-1810736-performcommand.md)
  Handles an ioctl command sent to the Ethernet interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioethernetinterface/1810711-getnameprefix)*