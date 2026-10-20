# controllerWillClose

**Framework**: Kernel  
**Kind**: instm

A notification that the interface will close the network controller.

## Declaration

```cpp
virtual void controllerWillClose(
 IONetworkController *controller);
```

#### Overview

This method will simply call super to propagate the method call. This method is called with the arbitration lock held.

## Parameters

- `controller`: The controller that is about to be closed.

## See Also

### Miscellaneous
- [controllerDidChangePowerState](./api-1810626-controllerdidchangepowerstate.md)
  Handles a notification that the network controller servicing this interface object has transitioned to a new power state.
- [controllerDidOpen](./api-1810636-controllerdidopen.md)
  A notification that the interface has opened the network controller.
- [controllerWillChangePowerState](./api-1810670-controllerwillchangepowerstate.md)
  Handles a notification that the network controller servicing this interface object is about to transition to a new power state.
- [free](./api-1810696-free.md)
  Frees the IOEthernetInterface instance.
- [getNamePrefix](./api-1810711-getnameprefix.md)
  Returns a string containing the prefix to use when creating a BSD name for this interface.
- [init](./api-1810722-init.md)
  Initializes an IOEthernetInterface instance.
- [performCommand](./api-1810736-performcommand.md)
  Handles an ioctl command sent to the Ethernet interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioethernetinterface/1810684-controllerwillclose)*