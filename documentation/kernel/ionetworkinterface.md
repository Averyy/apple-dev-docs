# IONetworkInterface

**Framework**: Kernel  
**Kind**: cl

Abstract class that manages the connection between an IONetworkController and the data link interface layer.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class IONetworkInterface : IOService
```

#### Overview

An IONetworkInterface object manages the connection between an IONetworkController and the data link interface layer (DLIL). All interactions between the controller and DLIL must go through an interface object. Any data structures that are required by DLIL for a particular interface type shall be allocated and mantained by the interface object. IONetworkInterface is an abstract class that must be extended by a concrete subclass to specialize for a particular network type.

Although most drivers will allocate a single interface object, it is possible for multiple interfaces to be attached to a single controller. This controller driver will be responsible for arbitrating access among its multiple interface clients.

IONetworkInterface also maintains a dictionary of IONetworkData objects containing statistics structures. Controller drivers can ask for a particular data object by name and update the statistics counters within directly. This dictionary is added to the interface's property table and is visible outside of the kernel.

## Topics

### Miscellaneous
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
- [setFlags](ionetworkinterface/1810924-setflags.md)
  Performs a read-modify-write operation on the current interface flags value.
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
### Constants
- [InputOptionQueuePacket](ionetworkinterface/inputoptionqueuepacket.md)
### Instance Methods
- [- addNetworkData](ionetworkinterface/1502913-addnetworkdata.md)
- [- attachToDataLinkLayer](ionetworkinterface/1503071-attachtodatalinklayer.md)
- [- clearInputQueue](ionetworkinterface/1503069-clearinputqueue.md)
- [- configureOutputStartDelay](ionetworkinterface/1503080-configureoutputstartdelay.md)
- [- controllerDidChangePowerState](ionetworkinterface/1502947-controllerdidchangepowerstate.md)
- [- controllerDidOpen](ionetworkinterface/1503042-controllerdidopen.md)
- [- controllerWillChangePowerState](ionetworkinterface/1502968-controllerwillchangepowerstate.md)
- [- controllerWillClose](ionetworkinterface/1503013-controllerwillclose.md)
- [- debuggerRegistered](ionetworkinterface/1502975-debuggerregistered.md)
- [- detachFromDataLinkLayer](ionetworkinterface/1502919-detachfromdatalinklayer.md)
- [- drainOutputQueue](ionetworkinterface/1502933-drainoutputqueue.md)
- [- feedPacketInputTap](ionetworkinterface/1503085-feedpacketinputtap.md)
- [- feedPacketOutputTap](ionetworkinterface/1502992-feedpacketoutputtap.md)
- [- fetchDriverOutputStats](ionetworkinterface/4395251-fetchdriveroutputstats.md)
- [- flushInputQueue](ionetworkinterface/1503007-flushinputqueue.md)
- [- free](ionetworkinterface/1502935-free.md)
- [- getController](ionetworkinterface/1503075-getcontroller.md)
- [- getExtraFlags](ionetworkinterface/1503027-getextraflags.md)
- [- getFlags](ionetworkinterface/1503053-getflags.md)
- [- getIfnet](ionetworkinterface/1503049-getifnet.md)
- [- getInterfaceState](ionetworkinterface/1502914-getinterfacestate.md)
- [- getInterfaceType](ionetworkinterface/1503061-getinterfacetype.md)
- [- getMaxTransferUnit](ionetworkinterface/1502929-getmaxtransferunit.md)
- [- getMediaAddressLength](ionetworkinterface/1503064-getmediaaddresslength.md)
- [- getMediaHeaderLength](ionetworkinterface/1502921-getmediaheaderlength.md)
- [- getMetaClass](ionetworkinterface/1503043-getmetaclass.md)
- [- getNamePrefix](ionetworkinterface/1503001-getnameprefix.md)
- [- getNetworkData](ionetworkinterface/1503029-getnetworkdata.md)
- [- getNetworkData](ionetworkinterface/3516614-getnetworkdata.md)
- [- getParameter](ionetworkinterface/1502904-getparameter.md)
- [- getUnitNumber](ionetworkinterface/1503057-getunitnumber.md)
- [- haltOutputThread](ionetworkinterface/1503083-haltoutputthread.md)
- [- handleClientClose](ionetworkinterface/1502917-handleclientclose.md)
- [- handleClientOpen](ionetworkinterface/1503039-handleclientopen.md)
- [- handleClose](ionetworkinterface/1502979-handleclose.md)
- [- handleIsOpen](ionetworkinterface/1503051-handleisopen.md)
- [- handleOpen](ionetworkinterface/1503025-handleopen.md)
- [- if_start_precheck](ionetworkinterface/1502950-if_start_precheck.md)
- [- init](ionetworkinterface/1502990-init.md)
- [- initIfnet](ionetworkinterface/1502892-initifnet.md)
- [- initIfnetParams](ionetworkinterface/1502887-initifnetparams.md)
- [- inputEvent](ionetworkinterface/1502960-inputevent.md)
- [- inputPacket](ionetworkinterface/1502906-inputpacket.md)
- [- isPrimaryInterface](ionetworkinterface/1502942-isprimaryinterface.md)
- [- isRegistered](ionetworkinterface/1503017-isregistered.md)
- [- lock](ionetworkinterface/1502923-lock.md)
- [- message](ionetworkinterface/1503086-message.md)
- [- newUserClient](ionetworkinterface/1502927-newuserclient.md)
- [- notifyDriver](ionetworkinterface/1502932-notifydriver.md)
- [- performCommand](ionetworkinterface/1503045-performcommand.md)
- [- powerStateDidChangeTo](ionetworkinterface/1503034-powerstatedidchangeto.md)
- [- powerStateWillChangeTo](ionetworkinterface/1502940-powerstatewillchangeto.md)
- [- pushInputPacket](ionetworkinterface/1502999-pushinputpacket.md)
- [- pushInputQueue](ionetworkinterface/1502954-pushinputqueue.md)
- [- removeNetworkData](ionetworkinterface/1502900-removenetworkdata.md)
- [- removeNetworkData](ionetworkinterface/3516615-removenetworkdata.md)
- [- requestTerminate](ionetworkinterface/1503023-requestterminate.md)
- [- serializeProperties](ionetworkinterface/1502916-serializeproperties.md)
- [- setExtendedFlags](ionetworkinterface/1502889-setextendedflags.md)
- [- setExtraFlags](ionetworkinterface/1502902-setextraflags.md)
- [- setFlags](ionetworkinterface/1503084-setflags.md)
- [- setInterfaceState](ionetworkinterface/1502986-setinterfacestate.md)
- [- setInterfaceType](ionetworkinterface/1502966-setinterfacetype.md)
- [- setMaxTransferUnit](ionetworkinterface/1502952-setmaxtransferunit.md)
- [- setMediaAddressLength](ionetworkinterface/1502908-setmediaaddresslength.md)
- [- setMediaHeaderLength](ionetworkinterface/1503076-setmediaheaderlength.md)
- [- setUnitNumber](ionetworkinterface/1503035-setunitnumber.md)
- [- syncSIOCGIFMEDIA](ionetworkinterface/1502958-syncsiocgifmedia.md)
- [- syncSIOCSIFMEDIA](ionetworkinterface/1502898-syncsiocsifmedia.md)
- [- syncSIOCSIFMTU](ionetworkinterface/1502944-syncsiocsifmtu.md)
- [- unlock](ionetworkinterface/1502997-unlock.md)
- [- willTerminate](ionetworkinterface/1503066-willterminate.md)
### Type Methods
- [+ handleNetworkInputEvent](ionetworkinterface/2919941-handlenetworkinputevent.md)
- [+ if_detach](ionetworkinterface/1503073-if_detach.md)
- [+ if_input_poll](ionetworkinterface/1503003-if_input_poll.md)
- [+ if_input_poll_gated](ionetworkinterface/1503030-if_input_poll_gated.md)
- [+ if_ioctl](ionetworkinterface/1503015-if_ioctl.md)
- [+ if_output](ionetworkinterface/1502930-if_output.md)
- [+ if_set_bpf_tap](ionetworkinterface/1502995-if_set_bpf_tap.md)
- [+ if_start](ionetworkinterface/1503041-if_start.md)
- [+ if_start_gated](ionetworkinterface/1503059-if_start_gated.md)
- [+ performGatedCommand](ionetworkinterface/1502993-performgatedcommand.md)
- [+ powerChangeHandler](ionetworkinterface/1503032-powerchangehandler.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IONetworkController](ionetworkcontroller.md)
  Implements the framework for a generic network controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkinterface)*