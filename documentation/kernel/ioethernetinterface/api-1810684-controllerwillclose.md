# controllerWillClose

**Framework**: Kernel  
**Kind**: instm

A notification that the interface will close the network controller.

## Declaration

```swift
virtual void controllerWillClose(
 IONetworkController *controller);
```

#### Overview

This method will simply call super to propagate the method call. This method is called with the arbitration lock held.

## Parameters

- `controller`: The controller that is about to be closed.

## See Also

- [controllerDidChangePowerState](ioethernetinterface/1810626-controllerdidchangepowerstate.md)
  Handles a notification that the network controller servicing this interface object has transitioned to a new power state.
- [controllerDidOpen](ioethernetinterface/1810636-controllerdidopen.md)
  A notification that the interface has opened the network controller.
- [controllerWillChangePowerState](ioethernetinterface/1810670-controllerwillchangepowerstate.md)
  Handles a notification that the network controller servicing this interface object is about to transition to a new power state.
- [free](ioethernetinterface/1810696-free.md)
  Frees the IOEthernetInterface instance.
- [getNamePrefix](ioethernetinterface/1810711-getnameprefix.md)
  Returns a string containing the prefix to use when creating a BSD name for this interface.
- [init](ioethernetinterface/1810722-init.md)
  Initializes an IOEthernetInterface instance.
- [performCommand](ioethernetinterface/1810736-performcommand.md)
  Handles an ioctl command sent to the Ethernet interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioethernetinterface/1810684-controllerwillclose)*