# inputPacket

**Framework**: Kernel  
**Kind**: instm

For drivers to submit a received packet to the network stack.

## Declaration

```cpp
virtual UInt32 inputPacket( 
 mbuf_t packet, 
 UInt32 length = 0, 
 IOOptionBits options = 0, 
 void *param = 0 );
```

## Return Value

Returns the number of packets that were submitted to the network stack, or zero if the packet was enqueued.

## Overview

The packet provided to this method may be added to an input queue managed by the interface object, which the driver can use to postpone the packet handoff to the network stack, until all received packets have been added to the input queue. A subsequent call to `flushInputQueue()`, will transfer the entire contents of the input queue to the network stack. This input queue is not protected by a lock. Drivers that leverage this input queue must either access the queue from a single thread, or enforce serialized access.

## Parameters

- `mbuf_t`: The mbuf containing the received packet.
- `length`: Specify the size of the received packet in the mbuf. The mbuf length fields are updated with this value. If zero, then the mbuf length fields are not updated.
- `options`: Pass `kInputOptionQueuePacket` to enqueue the input packet. Pass zero to bypass the input queue, and immediately submit the packet to the network stack.
- `param`: A parameter provided by the driver. Not used.

## See Also

### Miscellaneous
- [addNetworkData](./api-1810235-addnetworkdata.md)
  Adds an `IONetworkData` object to the interface.
- [attachToDataLinkLayer](./api-1810250-attachtodatalinklayer.md)
  Attach the network interface to the BSD data link layer.
- [clearInputQueue](./api-1810266-clearinputqueue.md)
  Discards all packets in the input queue.
- [controllerDidChangePowerState](./api-1810277-controllerdidchangepowerstate.md)
  Handles a notification that the network controller servicing this interface object has transitioned to a new power state.
- [controllerDidOpen](./api-1810292-controllerdidopen.md)
  Sends a notification that the interface has opened the network controller.
- [controllerWillChangePowerState](./api-1810306-controllerwillchangepowerstate.md)
  Handles a notification that the network controller servicing this interface object will transition to a new power state.
- [controllerWillClose](./api-1810322-controllerwillclose.md)
  Sends a notification that the interface will close the network controller.
- [debuggerRegistered](./api-1810336-debuggerregistered.md)
  Tells the `IONetworkData` that this interface will be used by the debugger.
- [detachFromDataLinkLayer](./api-1810351-detachfromdatalinklayer.md)
  Detach the network interface from the BSD data link layer.
- [feedPacketInputTap](./api-1810364-feedpacketinputtap.md)
  Feed received packets to the BPF
- [feedPacketOutputTap](./api-1810380-feedpacketoutputtap.md)
  Feed output packets to the BPF
- [flushInputQueue](./api-1810398-flushinputqueue.md)
  Submit all packets held in the input queue to the network stack.
- [free](./api-1810410-free.md)
  Frees the `IONetworkInterface` object.
- [getController](./api-1810426-getcontroller.md)
  Gets the `IONetworkController` object that created this interface.
- [getExtraFlags](./api-1810443-getextraflags.md)
  Gets the current interface eflags.
- [getFlags](./api-1810460-getflags.md)
  Gets the current interface flags.
- [getIfnet](./api-1810471-getifnet.md)
  Returns the `ifnet_t` allocated by the interface object.
- [getInterfaceState](./api-1810480-getinterfacestate.md)
  Reports the current state of the interface object.
- [getInterfaceType](./api-1810498-getinterfacetype.md)
  Gets the interface type.
- [getMaxTransferUnit](./api-1810513-getmaxtransferunit.md)
  Gets the maximum transfer unit for this interface.
- [getMediaAddressLength](./api-1810531-getmediaaddresslength.md)
  Gets the size of the media (MAC-layer) address.
- [getMediaHeaderLength](./api-1810551-getmediaheaderlength.md)
  Gets the size of the media header.
- [getNamePrefix](./api-1810563-getnameprefix.md)
  Returns the BSD name prefix as a C-string.
- [getNetworkData(const char *)](./api-1810574-getnetworkdata.md)
  Gets an `IONetworkData` object from the interface.
- [getNetworkData(const OSSymbol *)](./api-1810596-getnetworkdata.md)
  Gets an `IONetworkData` object from the interface.
- [getUnitNumber](./api-1810607-getunitnumber.md)
  Gets the unit number assigned to this interface object.
- [handleClientClose](./api-1810628-handleclientclose.md)
  Handles a client close on the interface.
- [handleClientOpen](./api-1810645-handleclientopen.md)
  Handles a client open on the interface.
- [init](./api-1810663-init.md)
  Initializes the `IONetworkInterface` object.
- [initIfnetParams](./api-1810678-initifnetparams.md)
  Allows a subclass to provide ifnet initialization parameters specific to an interface type.
- [inputEvent](./api-1810692-inputevent.md)
  Sends an event to the network stack.
- [isPrimaryInterface](./api-1810743-isprimaryinterface.md)
  Queries whether the interface is the primary network interface on the system.
- [isRegistered](./api-1810763-isregistered.md)
  Queries if the interface has attached to the BSD network stack.
- [lock](./api-1810783-lock.md)
  Acquires a recursive lock owned by the interface.
- [performCommand](./api-1810800-performcommand.md)
  Handles an ioctl command sent to the network interface.
- [powerStateDidChangeTo](./api-1810818-powerstatedidchangeto.md)
  Handles a post-change power interest notification from the network controller.
- [powerStateWillChangeTo](./api-1810839-powerstatewillchangeto.md)
  Handles a pre-change power interest notification from the network controller.
- [registerOutputHandler](./api-1810858-registeroutputhandler.md)
  Registers a target/action to handle outbound packets.
- [removeNetworkData(const char *)](./api-1810886-removenetworkdata.md)
  Removes an `IONetworkData` object from the interface.
- [removeNetworkData(const OSSymbol *)](./api-1810904-removenetworkdata.md)
  Removes an `IONetworkData` object from the interface.
- [setFlags](./api-1810924-setflags.md)
  Performs a read-modify-write operation on the current interface flags value.
- [setInterfaceState](./api-1810944-setinterfacestate.md)
  Updates the interface object state flags.
- [setInterfaceType](./api-1810958-setinterfacetype.md)
  Sets the interface type.
- [setMaxTransferUnit](./api-1810979-setmaxtransferunit.md)
  Sets the maximum transfer unit for this interface.
- [setMediaAddressLength](./api-1810991-setmediaaddresslength.md)
  Sets the size of the media (MAC-layer) address.
- [setMediaHeaderLength](./api-1811003-setmediaheaderlength.md)
  Sets the size of the media header.
- [setUnitNumber](./api-1811014-setunitnumber.md)
  Assigns an unique unit number to this interface.
- [unlock](./api-1811026-unlock.md)
  Releases the recursive lock owned by the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkinterface/1810712-inputpacket)*