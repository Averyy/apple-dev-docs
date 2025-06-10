# controllerDidOpen

**Framework**: Kernel  
**Kind**: instm

A notification that the interface has opened the network controller.

## Declaration

```swift
virtual bool controllerDidOpen(
 IONetworkController *controller);
```

#### Return_value

Returns true on success, false otherwise. Returning false will cause the controller to be closed, and any pending client opens to be rejected.

#### Overview

This method will be called by IONetworkInterface after a network controller has accepted an open from this interface object. IOEthernetInterface will first call the implementation in its superclass, then inspect the controller through properties published in the registry. This method is called with the arbitration lock held.

## Parameters

- `controller`: The controller object that was opened.

## See Also

- [controllerDidChangePowerState](ioethernetinterface/1810626-controllerdidchangepowerstate.md)
  Handles a notification that the network controller servicing this interface object has transitioned to a new power state.
- [controllerWillChangePowerState](ioethernetinterface/1810670-controllerwillchangepowerstate.md)
  Handles a notification that the network controller servicing this interface object is about to transition to a new power state.
- [controllerWillClose](ioethernetinterface/1810684-controllerwillclose.md)
  A notification that the interface will close the network controller.
- [free](ioethernetinterface/1810696-free.md)
  Frees the IOEthernetInterface instance.
- [getNamePrefix](ioethernetinterface/1810711-getnameprefix.md)
  Returns a string containing the prefix to use when creating a BSD name for this interface.
- [init](ioethernetinterface/1810722-init.md)
  Initializes an IOEthernetInterface instance.
- [performCommand](ioethernetinterface/1810736-performcommand.md)
  Handles an ioctl command sent to the Ethernet interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioethernetinterface/1810636-controllerdidopen)*