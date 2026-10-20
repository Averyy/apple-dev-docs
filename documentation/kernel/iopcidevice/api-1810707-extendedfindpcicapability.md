# extendedFindPCICapability

**Framework**: Kernel  
**Kind**: instm

Search configuration space for a PCI capability register.

## Declaration

```cpp
virtual UInt32 extendedFindPCICapability(
 UInt32 capabilityID,
 IOByteCount *offset = 0 );
```

#### Return Value

The 32-bit value of the capability register if one was found, zero otherwise.

#### Overview

This method searches the device's config space for a PCI capability register matching the passed capability ID, if the device supports PCI capabilities.

## Parameters

- `capabilityID`: A PCI capability ID. PCI Express devices may support extended capabilities in config space starting at offset 0x100. To search this space, the ID passed should be the negated value of the PCI-SIG assigned ID for the extended capability.
- `offset`: An optional in/out parameter to return the offset into config space where the capability was found, and to set the start point of the next search. Initialize the offset to zero before the first call to extendedFindPCICapability() and subsequent calls will find all capabilty blocks that may exist on the device with the same ID.

## See Also

### Miscellaneous
- [configRead16](./api-1810221-configread16.md)
  Reads a 16-bit value from the PCI device's configuration space.
- [configRead32](./api-1810249-configread32.md)
  Reads a 32-bit value from the PCI device's configuration space.
- [configRead8](./api-1810282-configread8.md)
  Reads a 8-bit value from the PCI device's configuration space.
- [configWrite16](./api-1810325-configwrite16.md)
  Writes a 16-bit value to the PCI device's configuration space.
- [configWrite32](./api-1810356-configwrite32.md)
  Writes a 32-bit value to the PCI device's configuration space.
- [configWrite8](./api-1810381-configwrite8.md)
  Writes a 8-bit value to the PCI device's configuration space.
- [enablePCIPowerManagement](./api-1810420-enablepcipowermanagement.md)
  enable PCI power management for sleep state
- [extendedConfigRead16](./api-1810448-extendedconfigread16.md)
  Reads a 16-bit value from the PCI device's configuration space.
- [extendedConfigRead32](./api-1810495-extendedconfigread32.md)
  Reads a 32-bit value from the PCI device's configuration space.
- [extendedConfigRead8](./api-1810539-extendedconfigread8.md)
  Reads a 8-bit value from the PCI device's configuration space.
- [extendedConfigWrite16](./api-1810577-extendedconfigwrite16.md)
  Writes a 16-bit value to the PCI device's configuration space.
- [extendedConfigWrite32](./api-1810617-extendedconfigwrite32.md)
  Writes a 32-bit value to the PCI device's configuration space.
- [extendedConfigWrite8](./api-1810659-extendedconfigwrite8.md)
  Writes a 8-bit value to the PCI device's configuration space.
- [findPCICapability](./api-1810749-findpcicapability.md)
  Search configuration space for a PCI capability register.
- [getBusNumber](./api-1810790-getbusnumber.md)
  Accessor to return the PCI device's assigned bus number.
- [getDeviceMemoryWithRegister](./api-1810831-getdevicememorywithregister.md)
  Returns an instance of IODeviceMemory representing one of the device's memory mapped ranges.
- [getDeviceNumber](./api-1810861-getdevicenumber.md)
  Accessor to return the PCI device's device number.
- [getFunctionNumber](./api-1810892-getfunctionnumber.md)
  Accessor to return the PCI device's function number.
- [hasPCIPowerManagement](./api-1810931-haspcipowermanagement.md)
  determine whether or not the device supports PCI Bus Power Management.
- [ioDeviceMemory](./api-1810959-iodevicememory.md)
  Accessor to the I/O space aperture for the bus.
- [ioRead16](./api-1810986-ioread16.md)
  Reads a 16-bit value from an I/O space aperture.
- [ioRead32](./api-1811005-ioread32.md)
  Reads a 32-bit value from an I/O space aperture.
- [ioRead8](./api-1811039-ioread8.md)
  Reads a 8-bit value from an I/O space aperture.
- [ioWrite16](./api-1811083-iowrite16.md)
  Writes a 16-bit value to an I/O space aperture.
- [ioWrite32](./api-1811113-iowrite32.md)
  Writes a 32-bit value to an I/O space aperture.
- [ioWrite8](./api-1811151-iowrite8.md)
  Writes a 8-bit value to an I/O space aperture.
- [mapDeviceMemoryWithRegister](./api-1811470-mapdevicememorywithregister.md)
  Maps a physical range of the device.
- [setBusMasterEnable](./api-1811490-setbusmasterenable.md)
  Enables bus mastering on the device.
- [setConfigBits](./api-1811511-setconfigbits.md)
  Sets masked bits in a configuration space register.
- [setIOEnable](./api-1811528-setioenable.md)
  Sets the device's I/O space response.
- [setMemoryEnable](./api-1811543-setmemoryenable.md)
  Sets the device's memory space response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopcidevice/1810707-extendedfindpcicapability)*