# setFlags

**Framework**: Kernel  
**Kind**: instm

Performs a read-modify-write operation on the current interface flags value.

## Declaration

```swift
virtual bool setFlags(
 UInt16 flags,
 UInt16 clear = 0 );
```

#### Return_value

Always returns true.

#### Overview

Calls `ifnet_set_flags` if the interface is attached to the network stack, and updates the `kIOInterfaceFlags` property using the provided value. See `bsd/net/if.h` header file for the flag constants.

## Parameters

- `flags`: The bits that should be set.
- `clear`: The bits that should be cleared. If zero, then non of the flags are cleared and the result is formed by OR'ing the original flags value with the new flags.

## See Also

- [addNetworkData](ionetworkinterface/1810235-addnetworkdata.md)
  Adds an `IONetworkData` object to the interface.
- [attachToDataLinkLayer](ionetworkinterface/1810250-attachtodatalinklayer.md)
  Attach the network interface to the BSD data link layer.
- [clearInputQueue](ionetworkinterface/1810266-clearinputqueue.md)
  Discards all packets in the input queue.
- [controllerDidChangePowerState](ionetworkinterface/1810277-controllerdidchangepowerstate.md)
  Handles a notification that the network controller servicing this interface object has transitioned to a new power state.
- [controllerDidOpen](ionetworkinterface/1810292-controllerdidopen.md)
  Sends a notification that the interface has opened the network controller.
- [controllerWillChangePowerState](ionetworkinterface/1810306-controllerwillchangepowerstate.md)
  Handles a notification that the network controller servicing this interface object will transition to a new power state.
- [controllerWillClose](ionetworkinterface/1810322-controllerwillclose.md)
  Sends a notification that the interface will close the network controller.
- [debuggerRegistered](ionetworkinterface/1810336-debuggerregistered.md)
  Tells the `IONetworkData` that this interface will be used by the debugger.
- [detachFromDataLinkLayer](ionetworkinterface/1810351-detachfromdatalinklayer.md)
  Detach the network interface from the BSD data link layer.
- [feedPacketInputTap](ionetworkinterface/1810364-feedpacketinputtap.md)
  Feed received packets to the BPF
- [feedPacketOutputTap](ionetworkinterface/1810380-feedpacketoutputtap.md)
  Feed output packets to the BPF
- [flushInputQueue](ionetworkinterface/1810398-flushinputqueue.md)
  Submit all packets held in the input queue to the network stack.
- [free](ionetworkinterface/1810410-free.md)
  Frees the `IONetworkInterface` object.
- [getController](ionetworkinterface/1810426-getcontroller.md)
  Gets the `IONetworkController` object that created this interface.
- [getExtraFlags](ionetworkinterface/1810443-getextraflags.md)
  Gets the current interface eflags.
- [getFlags](ionetworkinterface/1810460-getflags.md)
  Gets the current interface flags.
- [getIfnet](ionetworkinterface/1810471-getifnet.md)
  Returns the `ifnet_t` allocated by the interface object.
- [getInterfaceState](ionetworkinterface/1810480-getinterfacestate.md)
  Reports the current state of the interface object.
- [getInterfaceType](ionetworkinterface/1810498-getinterfacetype.md)
  Gets the interface type.
- [getMaxTransferUnit](ionetworkinterface/1810513-getmaxtransferunit.md)
  Gets the maximum transfer unit for this interface.
- [getMediaAddressLength](ionetworkinterface/1810531-getmediaaddresslength.md)
  Gets the size of the media (MAC-layer) address.
- [getMediaHeaderLength](ionetworkinterface/1810551-getmediaheaderlength.md)
  Gets the size of the media header.
- [getNamePrefix](ionetworkinterface/1810563-getnameprefix.md)
  Returns the BSD name prefix as a C-string.
- [getNetworkData(const char *)](ionetworkinterface/1810574-getnetworkdata.md)
  Gets an `IONetworkData` object from the interface.
- [getNetworkData(const OSSymbol *)](ionetworkinterface/1810596-getnetworkdata.md)
  Gets an `IONetworkData` object from the interface.
- [getUnitNumber](ionetworkinterface/1810607-getunitnumber.md)
  Gets the unit number assigned to this interface object.
- [handleClientClose](ionetworkinterface/1810628-handleclientclose.md)
  Handles a client close on the interface.
- [handleClientOpen](ionetworkinterface/1810645-handleclientopen.md)
  Handles a client open on the interface.
- [init](ionetworkinterface/1810663-init.md)
  Initializes the `IONetworkInterface` object.
- [initIfnetParams](ionetworkinterface/1810678-initifnetparams.md)
  Allows a subclass to provide ifnet initialization parameters specific to an interface type.
- [inputEvent](ionetworkinterface/1810692-inputevent.md)
  Sends an event to the network stack.
- [inputPacket](ionetworkinterface/1810712-inputpacket.md)
  For drivers to submit a received packet to the network stack.
- [isPrimaryInterface](ionetworkinterface/1810743-isprimaryinterface.md)
  Queries whether the interface is the primary network interface on the system.
- [isRegistered](ionetworkinterface/1810763-isregistered.md)
  Queries if the interface has attached to the BSD network stack.
- [lock](ionetworkinterface/1810783-lock.md)
  Acquires a recursive lock owned by the interface.
- [performCommand](ionetworkinterface/1810800-performcommand.md)
  Handles an ioctl command sent to the network interface.
- [powerStateDidChangeTo](ionetworkinterface/1810818-powerstatedidchangeto.md)
  Handles a post-change power interest notification from the network controller.
- [powerStateWillChangeTo](ionetworkinterface/1810839-powerstatewillchangeto.md)
  Handles a pre-change power interest notification from the network controller.
- [registerOutputHandler](ionetworkinterface/1810858-registeroutputhandler.md)
  Registers a target/action to handle outbound packets.
- [removeNetworkData(const char *)](ionetworkinterface/1810886-removenetworkdata.md)
  Removes an `IONetworkData` object from the interface.
- [removeNetworkData(const OSSymbol *)](ionetworkinterface/1810904-removenetworkdata.md)
  Removes an `IONetworkData` object from the interface.
- [setInterfaceState](ionetworkinterface/1810944-setinterfacestate.md)
  Updates the interface object state flags.
- [setInterfaceType](ionetworkinterface/1810958-setinterfacetype.md)
  Sets the interface type.
- [setMaxTransferUnit](ionetworkinterface/1810979-setmaxtransferunit.md)
  Sets the maximum transfer unit for this interface.
- [setMediaAddressLength](ionetworkinterface/1810991-setmediaaddresslength.md)
  Sets the size of the media (MAC-layer) address.
- [setMediaHeaderLength](ionetworkinterface/1811003-setmediaheaderlength.md)
  Sets the size of the media header.
- [setUnitNumber](ionetworkinterface/1811014-setunitnumber.md)
  Assigns an unique unit number to this interface.
- [unlock](ionetworkinterface/1811026-unlock.md)
  Releases the recursive lock owned by the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkinterface/1810924-setflags)*