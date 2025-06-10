# ioRead8

**Framework**: Kernel  
**Kind**: instm

Reads a 8-bit value from an I/O space aperture.

## Declaration

```swift
virtual UInt8 ioRead8(
 UInt16 offset,
 IOMemoryMap *map = 0 );
```

#### Return_value

The value read.

#### Overview

This method will read a 8-bit value from an offset in an I/O space aperture. If a map object is passed in, the value is read relative to it, otherwise to the value is read relative to the I/O space aperture for the bus. This function encapsulates the differences between architectures in generating I/O space operations. An eieio instruction is included on PPC.

## Parameters

- `offset`: An offset into a bus or device's I/O space aperture.
- `map`: If the offset is relative to the beginning of a device's aperture, an IOMemoryMap object for that object should be passed in. Otherwise, passing zero will write the value relative to the beginning of the bus' I/O space.

## See Also

- [configRead16](iopcidevice/1810221-configread16.md)
  Reads a 16-bit value from the PCI device's configuration space.
- [configRead32](iopcidevice/1810249-configread32.md)
  Reads a 32-bit value from the PCI device's configuration space.
- [configRead8](iopcidevice/1810282-configread8.md)
  Reads a 8-bit value from the PCI device's configuration space.
- [configWrite16](iopcidevice/1810325-configwrite16.md)
  Writes a 16-bit value to the PCI device's configuration space.
- [configWrite32](iopcidevice/1810356-configwrite32.md)
  Writes a 32-bit value to the PCI device's configuration space.
- [configWrite8](iopcidevice/1810381-configwrite8.md)
  Writes a 8-bit value to the PCI device's configuration space.
- [enablePCIPowerManagement](iopcidevice/1810420-enablepcipowermanagement.md)
  enable PCI power management for sleep state
- [extendedConfigRead16](iopcidevice/1810448-extendedconfigread16.md)
  Reads a 16-bit value from the PCI device's configuration space.
- [extendedConfigRead32](iopcidevice/1810495-extendedconfigread32.md)
  Reads a 32-bit value from the PCI device's configuration space.
- [extendedConfigRead8](iopcidevice/1810539-extendedconfigread8.md)
  Reads a 8-bit value from the PCI device's configuration space.
- [extendedConfigWrite16](iopcidevice/1810577-extendedconfigwrite16.md)
  Writes a 16-bit value to the PCI device's configuration space.
- [extendedConfigWrite32](iopcidevice/1810617-extendedconfigwrite32.md)
  Writes a 32-bit value to the PCI device's configuration space.
- [extendedConfigWrite8](iopcidevice/1810659-extendedconfigwrite8.md)
  Writes a 8-bit value to the PCI device's configuration space.
- [extendedFindPCICapability](iopcidevice/1810707-extendedfindpcicapability.md)
  Search configuration space for a PCI capability register.
- [findPCICapability](iopcidevice/1810749-findpcicapability.md)
  Search configuration space for a PCI capability register.
- [getBusNumber](iopcidevice/1810790-getbusnumber.md)
  Accessor to return the PCI device's assigned bus number.
- [getDeviceMemoryWithRegister](iopcidevice/1810831-getdevicememorywithregister.md)
  Returns an instance of IODeviceMemory representing one of the device's memory mapped ranges.
- [getDeviceNumber](iopcidevice/1810861-getdevicenumber.md)
  Accessor to return the PCI device's device number.
- [getFunctionNumber](iopcidevice/1810892-getfunctionnumber.md)
  Accessor to return the PCI device's function number.
- [hasPCIPowerManagement](iopcidevice/1810931-haspcipowermanagement.md)
  determine whether or not the device supports PCI Bus Power Management.
- [ioDeviceMemory](iopcidevice/1810959-iodevicememory.md)
  Accessor to the I/O space aperture for the bus.
- [ioRead16](iopcidevice/1810986-ioread16.md)
  Reads a 16-bit value from an I/O space aperture.
- [ioRead32](iopcidevice/1811005-ioread32.md)
  Reads a 32-bit value from an I/O space aperture.
- [ioWrite16](iopcidevice/1811083-iowrite16.md)
  Writes a 16-bit value to an I/O space aperture.
- [ioWrite32](iopcidevice/1811113-iowrite32.md)
  Writes a 32-bit value to an I/O space aperture.
- [ioWrite8](iopcidevice/1811151-iowrite8.md)
  Writes a 8-bit value to an I/O space aperture.
- [mapDeviceMemoryWithRegister](iopcidevice/1811470-mapdevicememorywithregister.md)
  Maps a physical range of the device.
- [setBusMasterEnable](iopcidevice/1811490-setbusmasterenable.md)
  Enables bus mastering on the device.
- [setConfigBits](iopcidevice/1811511-setconfigbits.md)
  Sets masked bits in a configuration space register.
- [setIOEnable](iopcidevice/1811528-setioenable.md)
  Sets the device's I/O space response.
- [setMemoryEnable](iopcidevice/1811543-setmemoryenable.md)
  Sets the device's memory space response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopcidevice/1811039-ioread8)*