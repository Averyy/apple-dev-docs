# IOEthernetController

**Framework**: Kernel  
**Kind**: cl

Abstract superclass for Ethernet controllers.

**Availability**:
- macOS 10.6+ - Deprecated in 10.15.4

## Declaration

```swift
class IOEthernetController : IONetworkController
```

#### Overview

Ethernet controller drivers should subclass IOEthernetController, and implement or override the hardware specific methods to create an Ethernet driver. An interface object (an IOEthernetInterface instance) must be instantiated by the driver, through attachInterface(), to connect the controller driver to the data link layer.

## Topics

### Miscellaneous
- [createInterface](ioethernetcontroller/1811019-createinterface.md)
  Creates an IOEthernetInterface object.
- [disablePacketFilter](ioethernetcontroller/1811029-disablepacketfilter.md)
  Disables a packet filter that is currently enabled from the given filter group.
- [enablePacketFilter](ioethernetcontroller/1811042-enablepacketfilter.md)
  Enables one of the supported packet filters from the given filter group.
- [free](ioethernetcontroller/1811058-free.md)
  Frees the IOEthernetController instance.
- [getHardwareAddress(IOEthernetAddress *)](ioethernetcontroller/1811070-gethardwareaddress.md)
  Gets the Ethernet controller's permanent station address.
- [getHardwareAddress(void *, UInt32 *)](ioethernetcontroller/1811082-gethardwareaddress.md)
  Gets the Ethernet controller's station address.
- [getMaxPacketSize](ioethernetcontroller/1811094-getmaxpacketsize.md)
  Gets the maximum packet size supported by the Ethernet controller, including the frame header and FCS.
- [getMinPacketSize](ioethernetcontroller/1811103-getminpacketsize.md)
  Gets the minimum packet size supported by the Ethernet controller, including the frame header and FCS.
- [getPacketFilters(const OSSymbol *, UInt32 *)](ioethernetcontroller/1811115-getpacketfilters.md)
  Gets the set of packet filters supported by the Ethernet controller in the given filter group.
- [getPacketFilters(UInt32 *)](ioethernetcontroller/1811127-getpacketfilters.md)
  Gets the set of packet filters supported by the Ethernet controller in the network filter group.
- [getVlanTagDemand](ioethernetcontroller/1811320-getvlantagdemand.md)
  Fetch the demand for hardware vlan tag stuffing for the given packet before it is transmitted on the network.
- [init](ioethernetcontroller/1811348-init.md)
  Initializes an IOEthernetController object.
- [initialize](ioethernetcontroller/1811361-initialize.md)
  IOEthernetController class initializer.
- [publishProperties](ioethernetcontroller/1811373-publishproperties.md)
  Publishes Ethernet controller properties and capabilities.
- [setHardwareAddress(const IOEthernetAddress *)](ioethernetcontroller/1811383-sethardwareaddress.md)
  Sets or changes the station address used by the Ethernet controller.
- [setHardwareAddress(const void *, UInt32)](ioethernetcontroller/1811391-sethardwareaddress.md)
  Sets or changes the station address used by the Ethernet controller.
- [setMulticastList](ioethernetcontroller/1811399-setmulticastlist.md)
  Sets the list of multicast addresses a multicast filter should use to match against the destination address of an incoming frame.
- [setMulticastMode](ioethernetcontroller/1811409-setmulticastmode.md)
  Enables or disables multicast mode.
- [setPromiscuousMode](ioethernetcontroller/1811419-setpromiscuousmode.md)
  Enables or disables promiscuous mode.
- [setVlanTag](ioethernetcontroller/1811426-setvlantag.md)
  Encode a received packet with the vlan tag result reported by the hardware.
- [setWakeOnMagicPacket](ioethernetcontroller/1811434-setwakeonmagicpacket.md)
  Enables or disables the wake on Magic Packet support.
### Instance Variables
- [_reserved](ioethernetcontroller/reserved.md)
### Instance Methods
- [- addTimeSyncReceivePacketHandler](ioethernetcontroller/2934806-addtimesyncreceivepackethandler.md)
- [- addTimeSyncTransmitPacketHandler](ioethernetcontroller/2934783-addtimesynctransmitpackethandler.md)
- [- allocateAVBPacket](ioethernetcontroller/2934778-allocateavbpacket.md)
- [- changeAVBControllerState](ioethernetcontroller/2934802-changeavbcontrollerstate.md)
- [- cleanupTransmitQueue](ioethernetcontroller/2934797-cleanuptransmitqueue.md)
- [- completeAVBPacket](ioethernetcontroller/2934805-completeavbpacket.md)
- [- createInterface](ioethernetcontroller/1506635-createinterface.md)
- [- createRealtimeAVBPacketPool](ioethernetcontroller/4284033-createrealtimeavbpacketpool.md)
- [- deregisterForAVBStateChangeNotifications](ioethernetcontroller/2934809-deregisterforavbstatechangenotif.md)
- [- disablePacketFilter](ioethernetcontroller/1506610-disablepacketfilter.md)
- [- enablePacketFilter](ioethernetcontroller/1506623-enablepacketfilter.md)
- [- free](ioethernetcontroller/1506601-free.md)
- [- getAVBSupport](ioethernetcontroller/2934775-getavbsupport.md)
- [- getControllerAVBState](ioethernetcontroller/2934818-getcontrolleravbstate.md)
- [- getHardwareAddress](ioethernetcontroller/1506619-gethardwareaddress.md)
- [- getHardwareAddress](ioethernetcontroller/3516606-gethardwareaddress.md)
- [- getMaxPacketSize](ioethernetcontroller/1506630-getmaxpacketsize.md)
- [- getMetaClass](ioethernetcontroller/1506595-getmetaclass.md)
- [- getMinPacketSize](ioethernetcontroller/1506647-getminpacketsize.md)
- [- getPacketFilters](ioethernetcontroller/1506617-getpacketfilters.md)
- [- getPacketFilters](ioethernetcontroller/3516607-getpacketfilters.md)
- [- getRealtimeReceiveQueueFilter](ioethernetcontroller/2934811-getrealtimereceivequeuefilter.md)
- [- getTransmitQueuePacketLatency](ioethernetcontroller/2934793-gettransmitqueuepacketlatency.md)
- [- getTransmitQueuePrefetchDelay](ioethernetcontroller/2934816-gettransmitqueueprefetchdelay.md)
- [- getVlanTagDemand](ioethernetcontroller/1506624-getvlantagdemand.md)
- [- init](ioethernetcontroller/1506598-init.md)
- [- publishProperties](ioethernetcontroller/1506650-publishproperties.md)
- [- receivedTimeSyncPacket](ioethernetcontroller/2934785-receivedtimesyncpacket.md)
- [- registerForAVBStateChangeNotifications](ioethernetcontroller/2934801-registerforavbstatechangenotific.md)
- [- removeTimeSyncReceivePacketHandler](ioethernetcontroller/2934796-removetimesyncreceivepackethandl.md)
- [- removeTimeSyncTransmitPacketHandler](ioethernetcontroller/2934781-removetimesynctransmitpackethand.md)
- [- setAVBControllerState](ioethernetcontroller/2934825-setavbcontrollerstate.md)
- [- setAVBPacketMapper](ioethernetcontroller/2934807-setavbpacketmapper.md)
- [- setGPTPPresent](ioethernetcontroller/2934787-setgptppresent.md)
- [- setHardwareAddress](ioethernetcontroller/1506608-sethardwareaddress.md)
- [- setHardwareAddress](ioethernetcontroller/3516608-sethardwareaddress.md)
- [- setMulticastList](ioethernetcontroller/1506649-setmulticastlist.md)
- [- setMulticastMode](ioethernetcontroller/1506646-setmulticastmode.md)
- [- setNumberOfRealtimeReceiveQueues](ioethernetcontroller/2934779-setnumberofrealtimereceivequeues.md)
- [- setNumberOfRealtimeTransmitQueues](ioethernetcontroller/2934803-setnumberofrealtimetransmitqueue.md)
- [- setPromiscuousMode](ioethernetcontroller/1506593-setpromiscuousmode.md)
- [- setRealtimeMulticastIsAllowed](ioethernetcontroller/2934788-setrealtimemulticastisallowed.md)
- [- setRealtimeReceiveDestinationMACList](ioethernetcontroller/2934790-setrealtimereceivedestinationmac.md)
- [- setRealtimeReceiveQueueFilter](ioethernetcontroller/2934817-setrealtimereceivequeuefilter.md)
- [- setRealtimeReceiveQueuePacketHandler](ioethernetcontroller/2934786-setrealtimereceivequeuepackethan.md)
- [- setTimeSyncPacketSupport](ioethernetcontroller/2934776-settimesyncpacketsupport.md)
- [- setTransmitQueuePacketLatency](ioethernetcontroller/2934814-settransmitqueuepacketlatency.md)
- [- setTransmitQueuePrefetchDelay](ioethernetcontroller/2934774-settransmitqueueprefetchdelay.md)
- [- setVlanTag](ioethernetcontroller/1506645-setvlantag.md)
- [- setWakeOnMagicPacket](ioethernetcontroller/1506633-setwakeonmagicpacket.md)
- [- timeSyncCallbackThread](ioethernetcontroller/2934821-timesynccallbackthread.md)
- [- transmitRealtimePackets](ioethernetcontroller/2934777-transmitrealtimepackets.md)
- [- transmitTimeSyncPacket](ioethernetcontroller/2934820-transmittimesyncpacket.md)
- [- transmittedTimeSyncPacket](ioethernetcontroller/2934799-transmittedtimesyncpacket.md)
### Type Methods
- [+ allocatedAVBPacketCompletion](ioethernetcontroller/2934795-allocatedavbpacketcompletion.md)
- [+ initialize](ioethernetcontroller/1506611-initialize.md)
- [+ realtimePoolAVBPacketCompletion](ioethernetcontroller/2934804-realtimepoolavbpacketcompletion.md)
- [+ timeSyncCallbackThreadEntry](ioethernetcontroller/2934789-timesynccallbackthreadentry.md)

## Relationships

### Inherits From
- [IONetworkController](ionetworkcontroller.md)

## See Also

- [IOUSBDevice](iousbdevice.md)
  An input/output service object that represents a device on the USB bus.
- [IOUSBInterface](iousbinterface.md)
  An object that represents an interface of a device on the USB bus.
- [IOOFPathMatching](1575304-ioofpathmatching.md)
- [IOUSBHostInterface](iousbhostinterface.md)
- [IOUSBHostDevice](iousbhostdevice.md)
- [IOUSBHostPipe](iousbhostpipe.md)
- [IOUSBHostIOSource](iousbhostiosource.md)
- [IOUSBHostStream](iousbhoststream.md)
- [IOHIDEventDriver](iohideventdriver.md)
- [IOHIDEventService](iohideventservice.md)
  IOService represents an device or OS service in IOKit and DriverKit.
- [IOHIDInterface](iohidinterface.md)
  IOService represents an device or OS service in IOKit and DriverKit.
- [IOHIDSystem](iohidsystem.md)
- [IOHIKeyboardMapper](iohikeyboardmapper.md)
- [IOHIKeyboard](iohikeyboard.md)
- [IOHIPointing](iohipointing.md)
- [IOHIDevice](iohidevice.md)
- [IOHIDElement](iohidelement.md)
- [IOHIDWorkLoop](iohidworkloop.md)
- [IOEthernetInterface](ioethernetinterface.md)
  The Ethernet interface object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioethernetcontroller)*