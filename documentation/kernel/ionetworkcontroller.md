# IONetworkController

**Framework**: Kernel  
**Kind**: cl

Implements the framework for a generic network controller.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class IONetworkController : IOService
```

#### Overview

A subclass of IONetworkController must provide additional functionality specific for a particular networking type. In addition, the driver must implement (override) a basic set of hardware dependent methods to create a working driver.

IONetworkController attaches itself to the data link layer (DLIL) via an IONetworkInterface object. A controller object without a companion interface is not accessible to the networking system. The controller interacts with DLIL by calling methods defined by the interface object. And conversely, DLIL will issue commands and packets to the controller through the interface object.

IONetworkController will create an IOCommandGate and attach this event source to an IOWorkLoop object. All commands sent from the interface object are handled through the IOCommandGate object, which will serialize access to the controller. Outbound packets sent from the interface to the controller have no implicit serialization. Drivers must implement an output function that is thread safe, or use an IOOutputQueue object which will provide a serialization model.

Note: IONetworkController internally uses some private messaging constants in the sys_iokit | sub_iokit_networking range defined in "IONetworkControllerPrivate.h". If you create a client for your controller (for example an IOUserClient), and it overrides the IOService::message method, your client may receive these messages. It should ignore these messages and pass them to super::message()

## Topics

### Miscellaneous
- [allocatePacket](ionetworkcontroller/1813917-allocatepacket.md)
  Allocates a packet with a data buffer that is larger than or equal to the size specified.
- [attachDebuggerClient](ionetworkcontroller/1813919-attachdebuggerclient.md)
  Attaches a new IOKernelDebugger client object.
- [attachInterface](ionetworkcontroller/1813921-attachinterface.md)
  Attaches a new network interface client object.
- [configureInterface](ionetworkcontroller/1813923-configureinterface.md)
  Configures a newly created network interface object.
- [copyMediumDictionary](ionetworkcontroller/1813924-copymediumdictionary.md)
  Returns a copy of the medium dictionary published by the driver.
- [copyPacket](ionetworkcontroller/1813925-copypacket.md)
  Allocates a new packet, containing data copied from an existing source packet.
- [createInterface](ionetworkcontroller/1813926-createinterface.md)
  Creates a new network interface object.
- [createOutputQueue](ionetworkcontroller/1813927-createoutputqueue.md)
  Creates an IOOutputQueue to handle output packet queueing, and also to resolve contention for the controller's transmitter from multiple client threads.
- [createWorkLoop](ionetworkcontroller/1813928-createworkloop.md)
  Method called by IONetworkController prior to the initial getWorkLoop() call.
- [detachDebuggerClient](ionetworkcontroller/1813929-detachdebuggerclient.md)
  Detaches an IOKernelDebugger client object.
- [detachInterface](ionetworkcontroller/1813930-detachinterface.md)
  Detaches an interface client object.
- [disable](ionetworkcontroller/1813931-disable.md)
  A disable request from an IOKernelDebugger client.
- [disable(IONetworkInterface *)](ionetworkcontroller/1813932-disable.md)
  A request from an interface client to disable the controller.
- [disable(IOService *)](ionetworkcontroller/1813933-disable.md)
  Handles a disable request from a client.
- [disablePacketFilter](ionetworkcontroller/1813934-disablepacketfilter.md)
  Disables a packet filter that is currently enabled from the given filter group.
- [doDisable](ionetworkcontroller/1813935-dodisable.md)
  Makes a synchronized call to disable() through executeCommand().
- [doEnable](ionetworkcontroller/1813936-doenable.md)
  Makes a synchronized call to enable() through executeCommand().
- [enable](ionetworkcontroller/1813937-enable.md)
  An enable request from an IOKernelDebugger client.
- [enable(IONetworkInterface *)](ionetworkcontroller/1813938-enable.md)
  A request from an interface client to enable the controller.
- [enable(IOService *)](ionetworkcontroller/1813939-enable.md)
  Handles an enable request from a client.
- [enablePacketFilter](ionetworkcontroller/1813940-enablepacketfilter.md)
  Enables one of the supported packet filters from the given filter group.
- [executeCommand](ionetworkcontroller/1813941-executecommand.md)
  Makes a C function call through the command gate.
- [free](ionetworkcontroller/1813942-free.md)
  Frees the IONetworkController object.
- [freePacket](ionetworkcontroller/1813943-freepacket.md)
  Releases the packet given back to the free pool.
- [getChecksumDemand](ionetworkcontroller/1813944-getchecksumdemand.md)
  Fetches the demand for hardware checksum computation and insertion for the given packet before it is transmitted on the network.
- [getChecksumSupport](ionetworkcontroller/1813945-getchecksumsupport.md)
  Gets checksums that are supported by the network controller for the given checksum family.
- [getCommandClient](ionetworkcontroller/1813946-getcommandclient.md)
  Gets the command client object.
- [getCommandGate](ionetworkcontroller/1813947-getcommandgate.md)
  Gets the IOCommandGate object created by IONetworkController.
- [getDebuggerLinkStatus](ionetworkcontroller/1813949-getdebuggerlinkstatus.md)
  Debugger polled-mode link status handler.
- [getFeatures](ionetworkcontroller/1813951-getfeatures.md)
  Reports generic features supported by the controller and/or the driver.
- [getHardwareAddress](ionetworkcontroller/1813953-gethardwareaddress.md)
  Gets the network controller's permanent hardware/station address.
- [getMaxPacketSize](ionetworkcontroller/1813954-getmaxpacketsize.md)
  Gets the maximum packet size supported by the controller.
- [getMediumDictionary](ionetworkcontroller/1813956-getmediumdictionary.md)
  Returns the medium dictionary published by the driver.
- [getMinPacketSize](ionetworkcontroller/1813957-getminpacketsize.md)
  Gets the minimum packet size supported by the controller.
- [getOutputHandler](ionetworkcontroller/1813959-getoutputhandler.md)
  Gets the address of the method designated to handle output packets for the network controller.
- [getOutputQueue](ionetworkcontroller/1813960-getoutputqueue.md)
  Gets the IOOutputQueue object created by createOutputQueue().
- [getPacketBufferConstraints](ionetworkcontroller/1813962-getpacketbufferconstraints.md)
  Gets the controller's packet buffer constraints.
- [getPacketFilters](ionetworkcontroller/1813964-getpacketfilters.md)
  Gets the set of packet filters supported by the network controller for the given filter group.
- [getSelectedMedium](ionetworkcontroller/1813966-getselectedmedium.md)
  Gets the current selected medium.
- [handleClose](ionetworkcontroller/1813967-handleclose.md)
  Handles a client close.
- [handleIsOpen](ionetworkcontroller/1813968-handleisopen.md)
  Queries whether a client has an open on the controller.
- [handleOpen](ionetworkcontroller/1813969-handleopen.md)
  Handles a client open.
- [init](ionetworkcontroller/1813970-init.md)
  Initializes the IONetworkController object.
- [message](ionetworkcontroller/1813971-message.md)
  Receives messages delivered from an attached provider.
- [newModelString](ionetworkcontroller/1813972-newmodelstring.md)
- [newRevisionString](ionetworkcontroller/1813973-newrevisionstring.md)
- [newVendorString](ionetworkcontroller/1813974-newvendorstring.md)
- [outputPacket](ionetworkcontroller/1813975-outputpacket.md)
  Transmits an output packet.
- [prepare](ionetworkcontroller/1813976-prepare.md)
  Prepares the controller before an IOService is created and attached as a client.
- [publishMediumDictionary](ionetworkcontroller/1813977-publishmediumdictionary.md)
  Publishes a dictionary of IONetworkMedium objects to advertise the media selection supported by the network controller.
- [publishProperties](ionetworkcontroller/1813978-publishproperties.md)
  Publishes controller properties and capabilities.
- [receivePacket](ionetworkcontroller/1813979-receivepacket.md)
  Debugger polled-mode receive handler.
- [registerWithPolicyMaker](ionetworkcontroller/1813980-registerwithpolicymaker.md)
  Implemented by controller drivers to register with the power management policy-maker.
- [releaseDebuggerLock](ionetworkcontroller/1813981-releasedebuggerlock.md)
  Releases the global debugger lock.
- [releaseFreePackets](ionetworkcontroller/1813982-releasefreepackets.md)
  Releases all packets held in the free packet queue.
- [replaceOrCopyPacket](ionetworkcontroller/1813983-replaceorcopypacket.md)
  A helper method that combines the functionality of copyPacket() and replacePacket() to process a packet containing a received frame.
- [replacePacket](ionetworkcontroller/1813984-replacepacket.md)
  Allocates a new packet to replace an existing packet, the existing packet is then returned.
- [reserveDebuggerLock](ionetworkcontroller/1813985-reservedebuggerlock.md)
  Takes the global debugger lock.
- [selectMedium](ionetworkcontroller/1813986-selectmedium.md)
  A client request to change the medium selection.
- [selectMediumWithName](ionetworkcontroller/1813987-selectmediumwithname.md)
  A client request to change the medium selection.
- [sendPacket](ionetworkcontroller/1813988-sendpacket.md)
  Debugger polled-mode transmit handler.
- [setChecksumResult](ionetworkcontroller/1813989-setchecksumresult.md)
  Encodes a received packet with the checksum result reported by the hardware.
- [setDebuggerMode](ionetworkcontroller/1813990-setdebuggermode.md)
  Set debugger mode for network drivers.
- [setHardwareAddress](ionetworkcontroller/1813991-sethardwareaddress.md)
  Sets or changes the station address used by the network controller.
- [setLinkStatus](ionetworkcontroller/1813992-setlinkstatus.md)
  Reports the link status and the active medium.
- [setMaxPacketSize](ionetworkcontroller/1813993-setmaxpacketsize.md)
  A client request to change the maximum packet size.
- [setSelectedMedium](ionetworkcontroller/1813994-setselectedmedium.md)
  Designates an entry in the published medium dictionary as the current selected medium.
- [start](ionetworkcontroller/1813995-start.md)
  Starts the network controller.
- [stop](ionetworkcontroller/1813996-stop.md)
  Stops the network controller.
- [systemWillShutdown](ionetworkcontroller/1813997-systemwillshutdown.md)
  Handles system shutdown and restart notifications.
### Callbacks
- [Action](ioworkloop/action.md)
- [IONetworkController::Action](ionetworkcontroller/ionetworkcontroller_action.md)
### Constants
- [TCP/IP](ionetworkcontroller/tcp_ip.md)
  TCP/IP checksums that may be supported by the hardware.
### Instance Variables
- [_reserved](ionetworkcontroller/reserved.md)
### Instance Methods
- [- allocatePacket](ionetworkcontroller/1393480-allocatepacket.md)
- [- allocatePacketNoWait](ionetworkcontroller/4077798-allocatepacketnowait.md)
- [- attachDebuggerClient](ionetworkcontroller/1393516-attachdebuggerclient.md)
- [- attachInterface](ionetworkcontroller/1393375-attachinterface.md)
- [- configureInterface](ionetworkcontroller/1393437-configureinterface.md)
- [- copyMediumDictionary](ionetworkcontroller/1393394-copymediumdictionary.md)
- [- copyPacket](ionetworkcontroller/1393532-copypacket.md)
- [- createInterface](ionetworkcontroller/1393472-createinterface.md)
- [- createOutputQueue](ionetworkcontroller/1393444-createoutputqueue.md)
- [- createWorkLoop](ionetworkcontroller/1393565-createworkloop.md)
- [- detachDebuggerClient](ionetworkcontroller/1393496-detachdebuggerclient.md)
- [- detachInterface](ionetworkcontroller/1393559-detachinterface.md)
- [- disable](ionetworkcontroller/1393413-disable.md)
- [- disable](ionetworkcontroller/3516610-disable.md)
- [- disable](ionetworkcontroller/3516611-disable.md)
- [- disablePacketFilter](ionetworkcontroller/1393357-disablepacketfilter.md)
- [- doDisable](ionetworkcontroller/1393400-dodisable.md)
- [- doEnable](ionetworkcontroller/1393406-doenable.md)
- [- enable](ionetworkcontroller/1393474-enable.md)
- [- enable](ionetworkcontroller/3516612-enable.md)
- [- enable](ionetworkcontroller/3516613-enable.md)
- [- enablePacketFilter](ionetworkcontroller/1393391-enablepacketfilter.md)
- [- executeCommand](ionetworkcontroller/1393419-executecommand.md)
- [- free](ionetworkcontroller/1393352-free.md)
- [- freePacket](ionetworkcontroller/1393500-freepacket.md)
- [- getChecksumDemand](ionetworkcontroller/1393433-getchecksumdemand.md)
- [- getChecksumSupport](ionetworkcontroller/1393514-getchecksumsupport.md)
- [- getCommandClient](ionetworkcontroller/1393429-getcommandclient.md)
- [- getCommandGate](ionetworkcontroller/1393539-getcommandgate.md)
- [- getCurrentMedium](ionetworkcontroller/1393383-getcurrentmedium.md)
- [- getDebuggerLinkStatus](ionetworkcontroller/1393365-getdebuggerlinkstatus.md)
- [- getFeatures](ionetworkcontroller/1393551-getfeatures.md)
- [- getHardwareAddress](ionetworkcontroller/1393512-gethardwareaddress.md)
- [- getMaxPacketSize](ionetworkcontroller/1393425-getmaxpacketsize.md)
- [- getMediumDictionary](ionetworkcontroller/1393561-getmediumdictionary.md)
- [- getMetaClass](ionetworkcontroller/1393510-getmetaclass.md)
- [- getMinPacketSize](ionetworkcontroller/1393543-getminpacketsize.md)
- [- getOutputHandler](ionetworkcontroller/1393525-getoutputhandler.md)
- [- getOutputQueue](ionetworkcontroller/1393421-getoutputqueue.md)
- [- getPacketBufferConstraints](ionetworkcontroller/1393381-getpacketbufferconstraints.md)
- [- getPacketFilters](ionetworkcontroller/1393465-getpacketfilters.md)
- [- getSelectedMedium](ionetworkcontroller/1393482-getselectedmedium.md)
- [- handleClose](ionetworkcontroller/1393458-handleclose.md)
- [- handleIsOpen](ionetworkcontroller/1393346-handleisopen.md)
- [- handleOpen](ionetworkcontroller/1393547-handleopen.md)
- [- init](ionetworkcontroller/1393333-init.md)
- [- message](ionetworkcontroller/1393387-message.md)
- [- newModelString](ionetworkcontroller/1393336-newmodelstring.md)
- [- newRevisionString](ionetworkcontroller/1393467-newrevisionstring.md)
- [- newVendorString](ionetworkcontroller/1393520-newvendorstring.md)
- [- outputPacket](ionetworkcontroller/1393415-outputpacket.md)
- [- prepare](ionetworkcontroller/1393567-prepare.md)
- [- publishMediumDictionary](ionetworkcontroller/1393569-publishmediumdictionary.md)
- [- publishProperties](ionetworkcontroller/1393369-publishproperties.md)
- [- receivePacket](ionetworkcontroller/1393363-receivepacket.md)
- [- registerWithPolicyMaker](ionetworkcontroller/1393530-registerwithpolicymaker.md)
- [- releaseDebuggerLock](ionetworkcontroller/1393545-releasedebuggerlock.md)
- [- releaseFreePackets](ionetworkcontroller/1393450-releasefreepackets.md)
- [- replaceOrCopyPacket](ionetworkcontroller/1393340-replaceorcopypacket.md)
- [- replacePacket](ionetworkcontroller/1393361-replacepacket.md)
- [- reserveDebuggerLock](ionetworkcontroller/1393529-reservedebuggerlock.md)
- [- selectMedium](ionetworkcontroller/1393563-selectmedium.md)
- [- selectMediumWithName](ionetworkcontroller/1393456-selectmediumwithname.md)
- [- sendPacket](ionetworkcontroller/1393476-sendpacket.md)
- [- setAggressiveness](ionetworkcontroller/1393549-setaggressiveness.md)
- [- setChecksumResult](ionetworkcontroller/1393460-setchecksumresult.md)
- [- setCurrentMedium](ionetworkcontroller/1393523-setcurrentmedium.md)
- [- setDebuggerMode](ionetworkcontroller/1393338-setdebuggermode.md)
- [- setHardwareAddress](ionetworkcontroller/1393463-sethardwareaddress.md)
- [- setHardwareAssists](ionetworkcontroller/4155390-sethardwareassists.md)
- [- setLinkStatus](ionetworkcontroller/1393431-setlinkstatus.md)
- [- setMaxPacketSize](ionetworkcontroller/1393398-setmaxpacketsize.md)
- [- setSelectedMedium](ionetworkcontroller/1393411-setselectedmedium.md)
- [- start](ionetworkcontroller/1393454-start.md)
- [- stop](ionetworkcontroller/1393537-stop.md)
- [- systemWillShutdown](ionetworkcontroller/1393502-systemwillshutdown.md)
### Type Methods
- [+ debugLinkStatusHandler](ionetworkcontroller/1393541-debuglinkstatushandler.md)
- [+ debugRxHandler](ionetworkcontroller/1393498-debugrxhandler.md)
- [+ debugSetModeHandler](ionetworkcontroller/1393441-debugsetmodehandler.md)
- [+ debugTxHandler](ionetworkcontroller/1393379-debugtxhandler.md)
- [+ executeCommandAction](ionetworkcontroller/1393373-executecommandaction.md)
- [+ handleCommand](ionetworkcontroller/1393423-handlecommand.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IONetworkInterface](ionetworkinterface.md)
  Abstract class that manages the connection between an IONetworkController and the data link interface layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkcontroller)*