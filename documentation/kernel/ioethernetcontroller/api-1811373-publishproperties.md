# publishProperties

**Framework**: Kernel  
**Kind**: instm

Publishes Ethernet controller properties and capabilities.

## Declaration

```swift
virtual bool publishProperties();
```

#### Return_value

Returns true if all properties and capabilities were discovered, and published successfully, false otherwise. Returning false will prevent client objects from attaching to the Ethernet controller since a property that a client relies upon may be missing.

#### Overview

This method publishes Ethernet controller properties to the property table. For instance, getHardwareAddress() is called to fetch the hardware address, and the address is then published to the property table. This method call is synchronized by the workloop's gate, and must never be called directly by subclasses.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioethernetcontroller/1811373-publishproperties)*