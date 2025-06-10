# enablePacketFilter

**Framework**: Kernel  
**Kind**: instm

Enables one of the supported packet filters from the given filter group.

## Declaration

```swift
virtual IOReturn enablePacketFilter(
 const OSSymbol *group, 
 UInt32 aFilter, 
 UInt32 enabledFilters, 
 IOOptionBits options = 0) = 0;
```

#### Return_value

Returns kIOReturnSuccess on success, or an error otherwise.

#### Overview

A client will call this method to enable a supported filter from the filter group specified. If the client wishes to enable more than one filter, it must call this method multiple times to enable the desired set of filters. This method call is synchronized by the workloop's gate.

## Parameters

- `group`: The name of the filter group containing the filter to be enabled.
- `aFilter`: The filter to enable.
- `enabledFilters`: All filters currently enabled by the client.
- `options`: Optional flags for the enable request.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionetworkcontroller/1813940-enablepacketfilter)*