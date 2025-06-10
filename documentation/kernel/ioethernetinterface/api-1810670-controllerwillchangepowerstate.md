# controllerWillChangePowerState

**Framework**: Kernel  
**Kind**: instm

Handles a notification that the network controller servicing this interface object is about to transition to a new power state.

## Declaration

```swift
virtual IOReturn controllerWillChangePowerState( 
 IONetworkController *controller, 
 IOPMPowerFlagsflags, 
 UInt32stateNumber, 
 IOService *policyMaker);
```

#### Return_value

Always returns kIOReturnSuccess.

#### Overview

If the controller is about to transition to an unusable state, and it is currently enabled, then the disable() method on the controller is called.

## Parameters

- `controller`: The network controller object.
- `flags`: Flags that describe the capability of the controller in the new power state.
- `stateNumber`: An index to a state in the network controller's power state array that the controller is switching to.
- `policyMaker`: A reference to the network controller's policy-maker, and is also the originator of this notification.

## See Also

- [controllerDidChangePowerState](ioethernetinterface/1810626-controllerdidchangepowerstate.md)
  Handles a notification that the network controller servicing this interface object has transitioned to a new power state.
- [controllerDidOpen](ioethernetinterface/1810636-controllerdidopen.md)
  A notification that the interface has opened the network controller.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioethernetinterface/1810670-controllerwillchangepowerstate)*