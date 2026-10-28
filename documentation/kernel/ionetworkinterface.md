# IONetworkInterface

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

Abstract class that manages the connection between an IONetworkController and the data link interface layer.

**Availability**:
- macOS 10.6+

## Declaration

```cpp
class IONetworkInterface : IOService
```

## Overview

An IONetworkInterface object manages the connection between an IONetworkController and the data link interface layer (DLIL). All interactions between the controller and DLIL must go through an interface object. Any data structures that are required by DLIL for a particular interface type shall be allocated and mantained by the interface object. IONetworkInterface is an abstract class that must be extended by a concrete subclass to specialize for a particular network type.

Although most drivers will allocate a single interface object, it is possible for multiple interfaces to be attached to a single controller. This controller driver will be responsible for arbitrating access among its multiple interface clients.

IONetworkInterface also maintains a dictionary of IONetworkData objects containing statistics structures. Controller drivers can ask for a particular data object by name and update the statistics counters within directly. This dictionary is added to the interface's property table and is visible outside of the kernel.

## Topics

### Miscellaneous
- [addNetworkData](./ionetworkinterface/api-1810235-addnetworkdata.md)
  Adds an `IONetworkData` object to the interface.
- [attachToDataLinkLayer](./ionetworkinterface/api-1810250-attachtodatalinklayer.md)
  Attach the network interface to the BSD data link layer.
- [clearInputQueue](./ionetworkinterface/api-1810266-clearinputqueue.md)
  Discards all packets in the input queue.
- [controllerDidChangePowerState](./ionetworkinterface/api-1810277-controllerdidchangepowerstate.md)
  Handles a notification that the network controller servicing this interface object has transitioned to a new power state.
- [controllerDidOpen](./ionetworkinterface/api-1810292-controllerdidopen.md)
  Sends a notification that the interface has opened the network controller.
- [controllerWillChangePowerState](./ionetworkinterface/api-1810306-controllerwillchangepowerstate.md)
  Handles a notification that the network controller servicing this interface object will transition to a new power state.
- [controllerWillClose](./ionetworkinterface/api-1810322-controllerwillclose.md)
  Sends a notification that the interface will close the network controller.
- [debuggerRegistered](./ionetworkinterface/api-1810336-debuggerregistered.md)
  Tells the `IONetworkData` that this interface will be used by the debugger.
- [detachFromDataLinkLayer](./ionetworkinterface/api-1810351-detachfromdatalinklayer.md)
  Detach the network interface from the BSD data link layer.
- [feedPacketInputTap](./ionetworkinterface/api-1810364-feedpacketinputtap.md)
  Feed received packets to the BPF
- [feedPacketOutputTap](./ionetworkinterface/api-1810380-feedpacketoutputtap.md)
  Feed output packets to the BPF
- [flushInputQueue](./ionetworkinterface/api-1810398-flushinputqueue.md)
  Submit all packets held in the input queue to the network stack.
- [free](./ionetworkinterface/api-1810410-free.md)
  Frees the `IONetworkInterface` object.
- [getController](./ionetworkinterface/api-1810426-getcontroller.md)
  Gets the `IONetworkController` object that created this interface.
- [getExtraFlags](./ionetworkinterface/api-1810443-getextraflags.md)
  Gets the current interface eflags.
- [getFlags](./ionetworkinterface/api-1810460-getflags.md)
  Gets the current interface flags.
- [getIfnet](./ionetworkinterface/api-1810471-getifnet.md)
  Returns the `ifnet_t` allocated by the interface object.
- [getInterfaceState](./ionetworkinterface/api-1810480-getinterfacestate.md)
  Reports the current state of the interface object.
- [getInterfaceType](./ionetworkinterface/api-1810498-getinterfacetype.md)
  Gets the interface type.
- [getMaxTransferUnit](./ionetworkinterface/api-1810513-getmaxtransferunit.md)
  Gets the maximum transfer unit for this interface.
- [getMediaAddressLength](./ionetworkinterface/api-1810531-getmediaaddresslength.md)
  Gets the size of the media (MAC-layer) address.
- [getMediaHeaderLength](./ionetworkinterface/api-1810551-getmediaheaderlength.md)
  Gets the size of the media header.
- [getNamePrefix](./ionetworkinterface/api-1810563-getnameprefix.md)
  Returns the BSD name prefix as a C-string.
- [getNetworkData(const char *)](./ionetworkinterface/api-1810574-getnetworkdata.md)
  Gets an `IONetworkData` object from the interface.
- [getNetworkData(const OSSymbol *)](./ionetworkinterface/api-1810596-getnetworkdata.md)
  Gets an `IONetworkData` object from the interface.
- [getUnitNumber](./ionetworkinterface/api-1810607-getunitnumber.md)
  Gets the unit number assigned to this interface object.
- [handleClientClose](./ionetworkinterface/api-1810628-handleclientclose.md)
  Handles a client close on the interface.
- [handleClientOpen](./ionetworkinterface/api-1810645-handleclientopen.md)
  Handles a client open on the interface.
- [init](./ionetworkinterface/api-1810663-init.md)
  Initializes the `IONetworkInterface` object.
- [initIfnetParams](./ionetworkinterface/api-1810678-initifnetparams.md)
  Allows a subclass to provide ifnet initialization parameters specific to an interface type.
- [inputEvent](./ionetworkinterface/api-1810692-inputevent.md)
  Sends an event to the network stack.
- [inputPacket](./ionetworkinterface/api-1810712-inputpacket.md)
  For drivers to submit a received packet to the network stack.
- [isPrimaryInterface](./ionetworkinterface/api-1810743-isprimaryinterface.md)
  Queries whether the interface is the primary network interface on the system.
- [isRegistered](./ionetworkinterface/api-1810763-isregistered.md)
  Queries if the interface has attached to the BSD network stack.
- [lock](./ionetworkinterface/api-1810783-lock.md)
  Acquires a recursive lock owned by the interface.
- [performCommand](./ionetworkinterface/api-1810800-performcommand.md)
  Handles an ioctl command sent to the network interface.
- [powerStateDidChangeTo](./ionetworkinterface/api-1810818-powerstatedidchangeto.md)
  Handles a post-change power interest notification from the network controller.
- [powerStateWillChangeTo](./ionetworkinterface/api-1810839-powerstatewillchangeto.md)
  Handles a pre-change power interest notification from the network controller.
- [registerOutputHandler](./ionetworkinterface/api-1810858-registeroutputhandler.md)
  Registers a target/action to handle outbound packets.
- [removeNetworkData(const char *)](./ionetworkinterface/api-1810886-removenetworkdata.md)
  Removes an `IONetworkData` object from the interface.
- [removeNetworkData(const OSSymbol *)](./ionetworkinterface/api-1810904-removenetworkdata.md)
  Removes an `IONetworkData` object from the interface.
- [setFlags](./ionetworkinterface/api-1810924-setflags.md)
  Performs a read-modify-write operation on the current interface flags value.
- [setInterfaceState](./ionetworkinterface/api-1810944-setinterfacestate.md)
  Updates the interface object state flags.
- [setInterfaceType](./ionetworkinterface/api-1810958-setinterfacetype.md)
  Sets the interface type.
- [setMaxTransferUnit](./ionetworkinterface/api-1810979-setmaxtransferunit.md)
  Sets the maximum transfer unit for this interface.
- [setMediaAddressLength](./ionetworkinterface/api-1810991-setmediaaddresslength.md)
  Sets the size of the media (MAC-layer) address.
- [setMediaHeaderLength](./ionetworkinterface/api-1811003-setmediaheaderlength.md)
  Sets the size of the media header.
- [setUnitNumber](./ionetworkinterface/api-1811014-setunitnumber.md)
  Assigns an unique unit number to this interface.
- [unlock](./ionetworkinterface/api-1811026-unlock.md)
  Releases the recursive lock owned by the interface.
### Constants
- [InputOptionQueuePacket](./ionetworkinterface/inputoptionqueuepacket.md)
### Instance Methods
- [- addNetworkData](./ionetworkinterface/api-1502913-addnetworkdata.md)
- [- attachToDataLinkLayer](./ionetworkinterface/api-1503071-attachtodatalinklayer.md)
- [- clearInputQueue](./ionetworkinterface/api-1503069-clearinputqueue.md)
- [- configureOutputStartDelay](./ionetworkinterface/api-1503080-configureoutputstartdelay.md)
- [- controllerDidChangePowerState](./ionetworkinterface/api-1502947-controllerdidchangepowerstate.md)
- [- controllerDidOpen](./ionetworkinterface/api-1503042-controllerdidopen.md)
- [- controllerWillChangePowerState](./ionetworkinterface/api-1502968-controllerwillchangepowerstate.md)
- [- controllerWillClose](./ionetworkinterface/api-1503013-controllerwillclose.md)
- [- debuggerRegistered](./ionetworkinterface/api-1502975-debuggerregistered.md)
- [- detachFromDataLinkLayer](./ionetworkinterface/api-1502919-detachfromdatalinklayer.md)
- [- drainOutputQueue](./ionetworkinterface/api-1502933-drainoutputqueue.md)
- [- feedPacketInputTap](./ionetworkinterface/api-1503085-feedpacketinputtap.md)
- [- feedPacketOutputTap](./ionetworkinterface/api-1502992-feedpacketoutputtap.md)
- [- fetchDriverOutputStats](./ionetworkinterface/api-4395251-fetchdriveroutputstats.md)
- [- flushInputQueue](./ionetworkinterface/api-1503007-flushinputqueue.md)
- [- free](./ionetworkinterface/api-1502935-free.md)
- [- getController](./ionetworkinterface/api-1503075-getcontroller.md)
- [- getExtraFlags](./ionetworkinterface/api-1503027-getextraflags.md)
- [- getFlags](./ionetworkinterface/api-1503053-getflags.md)
- [- getIfnet](./ionetworkinterface/api-1503049-getifnet.md)
- [- getInterfaceState](./ionetworkinterface/api-1502914-getinterfacestate.md)
- [- getInterfaceType](./ionetworkinterface/api-1503061-getinterfacetype.md)
- [- getMaxTransferUnit](./ionetworkinterface/api-1502929-getmaxtransferunit.md)
- [- getMediaAddressLength](./ionetworkinterface/api-1503064-getmediaaddresslength.md)
- [- getMediaHeaderLength](./ionetworkinterface/api-1502921-getmediaheaderlength.md)
- [- getMetaClass](./ionetworkinterface/api-1503043-getmetaclass.md)
- [- getNamePrefix](./ionetworkinterface/api-1503001-getnameprefix.md)
- [- getNetworkData](./ionetworkinterface/api-1503029-getnetworkdata.md)
- [- getNetworkData](./ionetworkinterface/api-3516614-getnetworkdata.md)
- [- getParameter](./ionetworkinterface/api-1502904-getparameter.md)
- [- getUnitNumber](./ionetworkinterface/api-1503057-getunitnumber.md)
- [- haltOutputThread](./ionetworkinterface/api-1503083-haltoutputthread.md)
- [- handleClientClose](./ionetworkinterface/api-1502917-handleclientclose.md)
- [- handleClientOpen](./ionetworkinterface/api-1503039-handleclientopen.md)
- [- handleClose](./ionetworkinterface/api-1502979-handleclose.md)
- [- handleIsOpen](./ionetworkinterface/api-1503051-handleisopen.md)
- [- handleOpen](./ionetworkinterface/api-1503025-handleopen.md)
- [- if_start_precheck](./ionetworkinterface/api-1502950-if_start_precheck.md)
- [- init](./ionetworkinterface/api-1502990-init.md)
- [- initIfnet](./ionetworkinterface/api-1502892-initifnet.md)
- [- initIfnetParams](./ionetworkinterface/api-1502887-initifnetparams.md)
- [- inputEvent](./ionetworkinterface/api-1502960-inputevent.md)
- [- inputPacket](./ionetworkinterface/api-1502906-inputpacket.md)
- [- isPrimaryInterface](./ionetworkinterface/api-1502942-isprimaryinterface.md)
- [- isRegistered](./ionetworkinterface/api-1503017-isregistered.md)
- [- lock](./ionetworkinterface/api-1502923-lock.md)
- [- message](./ionetworkinterface/api-1503086-message.md)
- [- newUserClient](./ionetworkinterface/api-1502927-newuserclient.md)
- [- notifyDriver](./ionetworkinterface/api-1502932-notifydriver.md)
- [- performCommand](./ionetworkinterface/api-1503045-performcommand.md)
- [- powerStateDidChangeTo](./ionetworkinterface/api-1503034-powerstatedidchangeto.md)
- [- powerStateWillChangeTo](./ionetworkinterface/api-1502940-powerstatewillchangeto.md)
- [- pushInputPacket](./ionetworkinterface/api-1502999-pushinputpacket.md)
- [- pushInputQueue](./ionetworkinterface/api-1502954-pushinputqueue.md)
- [- removeNetworkData](./ionetworkinterface/api-1502900-removenetworkdata.md)
- [- removeNetworkData](./ionetworkinterface/api-3516615-removenetworkdata.md)
- [- requestTerminate](./ionetworkinterface/api-1503023-requestterminate.md)
- [- serializeProperties](./ionetworkinterface/api-1502916-serializeproperties.md)
- [- setExtendedFlags](./ionetworkinterface/api-1502889-setextendedflags.md)
- [- setExtraFlags](./ionetworkinterface/api-1502902-setextraflags.md)
- [- setFlags](./ionetworkinterface/api-1503084-setflags.md)
- [- setInterfaceState](./ionetworkinterface/api-1502986-setinterfacestate.md)
- [- setInterfaceType](./ionetworkinterface/api-1502966-setinterfacetype.md)
- [- setMaxTransferUnit](./ionetworkinterface/api-1502952-setmaxtransferunit.md)
- [- setMediaAddressLength](./ionetworkinterface/api-1502908-setmediaaddresslength.md)
- [- setMediaHeaderLength](./ionetworkinterface/api-1503076-setmediaheaderlength.md)
- [- setUnitNumber](./ionetworkinterface/api-1503035-setunitnumber.md)
- [- syncSIOCGIFMEDIA](./ionetworkinterface/api-1502958-syncsiocgifmedia.md)
- [- syncSIOCSIFMEDIA](./ionetworkinterface/api-1502898-syncsiocsifmedia.md)
- [- syncSIOCSIFMTU](./ionetworkinterface/api-1502944-syncsiocsifmtu.md)
- [- unlock](./ionetworkinterface/api-1502997-unlock.md)
- [- willTerminate](./ionetworkinterface/api-1503066-willterminate.md)
### Type Methods
- [+ handleNetworkInputEvent](./ionetworkinterface/api-2919941-handlenetworkinputevent.md)
- [+ if_detach](./ionetworkinterface/api-1503073-if_detach.md)
- [+ if_input_poll](./ionetworkinterface/api-1503003-if_input_poll.md)
- [+ if_input_poll_gated](./ionetworkinterface/api-1503030-if_input_poll_gated.md)
- [+ if_ioctl](./ionetworkinterface/api-1503015-if_ioctl.md)
- [+ if_output](./ionetworkinterface/api-1502930-if_output.md)
- [+ if_set_bpf_tap](./ionetworkinterface/api-1502995-if_set_bpf_tap.md)
- [+ if_start](./ionetworkinterface/api-1503041-if_start.md)
- [+ if_start_gated](./ionetworkinterface/api-1503059-if_start_gated.md)
- [+ performGatedCommand](./ionetworkinterface/api-1502993-performgatedcommand.md)
- [+ powerChangeHandler](./ionetworkinterface/api-1503032-powerchangehandler.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

## See Also

### Interfaces
- [IONetworkController](./ionetworkcontroller.md)
  Implements the framework for a generic network controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkinterface)*