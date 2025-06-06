# IOPCIDevice

**Framework**: Kernel  
**Kind**: cl

An IOService class representing a PCI device.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```swift
class IOPCIDevice : IOService
```

#### Overview

The discovery of a PCI device by the PCI bus family results in an instance of the IOPCIDevice being created and published. It provides services for looking up and mapping memory mapped hardware, and access to the PCI configuration and I/O spaces.

Matching Supported by IOPCIDevice

Two types of matching are available, OpenFirmware name matching and PCI register matching. Currently, only one of these two matching schemes can be used in the same property table.

OpenFirmware Name Matching

IOService performs matching based on the IONameMatch property (see IOService). IOPCIDevices created with OpenFirmware device tree entries will name match based on the standard OpenFirmware name matching properties.

PCI Register Matching

A PCI device driver can also match on the values of certain config space registers.

In each case, several matching values can be specified, and an optional mask for the value of the config space register may follow the value, preceded by an '&' character.

kIOPCIMatchKey, "IOPCIMatch"

The kIOPCIMatchKey property matches the vendor and device ID (0x00) register, or the subsystem register (0x2c).

kIOPCIPrimaryMatchKey, "IOPCIPrimaryMatch"

The kIOPCIPrimaryMatchKey property matches the vendor and device ID (0x00) register.

kIOPCISecondaryMatchKey, "IOPCISecondaryMatch"

The kIOPCISecondaryMatchKey property matches the subsystem register (0x2c).

kIOPCIClassMatchKey, "IOPCIClassMatch"

The kIOPCIClassMatchKey property matches the class code register (0x08). The default mask for this register is 0xffffff00.

Examples:

&ltkey&gtIOPCIMatch&lt/key&gt

&ltstring&gt0x00261011&lt/string&gt

Matches a device whose vendor ID is 0x1011, and device ID is 0x0026, including subsystem IDs.

&ltkey&gtIOPCIMatch&lt/key&gt

&ltstring&gt0x00789004&0x00ffffff 0x78009004&0x0xff00ffff&lt/string&gt

Matches with any device with a vendor ID of 0x9004, and a device ID of 0xzz78 or 0x78zz, where 'z' is don't care.

&ltkey&gtIOPCIClassMatch&lt/key&gt

&ltstring&gt0x02000000&0xffff0000&lt/string&gt

Matches a device whose class code is 0x0200zz, an ethernet device.

## Topics

### Miscellaneous
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
- [ioRead8](iopcidevice/1811039-ioread8.md)
  Reads a 8-bit value from an I/O space aperture.
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
### Instance Variables
- [reserved](iopcidevice/reserved.md)
### Instance Methods
- [- ClientCrashed_Impl](iopcidevice/3736273-clientcrashed_impl.md)
- [- Close](../pcidriverkit/iopcidevice/close.md)
  Closes the session to the PCI device.
- [- ConfigurationRead16](../pcidriverkit/iopcidevice/configurationread16.md)
  Reads a 16-bit data value synchronously from the device’s configuration space.
- [- ConfigurationRead32](../pcidriverkit/iopcidevice/configurationread32.md)
  Reads a 32-bit data value synchronously from the device’s configuration space.
- [- ConfigurationRead8](../pcidriverkit/iopcidevice/configurationread8.md)
  Reads an 8-bit data value synchronously from the device’s configuration space.
- [- ConfigurationWrite16](../pcidriverkit/iopcidevice/configurationwrite16.md)
  Writes an 16-bit data value to the device’s configuration space.
- [- ConfigurationWrite32](../pcidriverkit/iopcidevice/configurationwrite32.md)
  Writes an 32-bit data value to the device’s configuration space.
- [- ConfigurationWrite8](../pcidriverkit/iopcidevice/configurationwrite8.md)
  Writes an 8-bit data value to the device’s configuration space.
- [- ConfigureInterrupts](iopcidevice/3919729-configureinterrupts.md)
- [- ConfigureInterrupts_Impl](iopcidevice/3919730-configureinterrupts_impl.md)
- [- Dispatch](iopcidevice/3180683-dispatch.md)
- [- EnablePCIPowerManagement](iopcidevice/3516629-enablepcipowermanagement.md)
- [- EnablePCIPowerManagement_Impl](iopcidevice/3516630-enablepcipowermanagement_impl.md)
- [- FindPCICapability](iopcidevice/3516632-findpcicapability.md)
- [- FindPCICapability_Impl](iopcidevice/3516633-findpcicapability_impl.md)
- [- GetBARInfo](iopcidevice/3861819-getbarinfo.md)
- [- GetBARInfo_Impl](iopcidevice/3861820-getbarinfo_impl.md)
- [- GetBusDeviceFunction](iopcidevice/3516635-getbusdevicefunction.md)
- [- GetBusDeviceFunction_Impl](iopcidevice/3516636-getbusdevicefunction_impl.md)
- [- GetLinkSpeed](iopcidevice/3943407-getlinkspeed.md)
- [- GetLinkSpeed_Impl](iopcidevice/3943408-getlinkspeed_impl.md)
- [- HasPCIPowerManagement](iopcidevice/3516638-haspcipowermanagement.md)
- [- HasPCIPowerManagement_Impl](iopcidevice/3516639-haspcipowermanagement_impl.md)
- [- MemoryRead16](../pcidriverkit/iopcidevice/memoryread16-9qkdh.md)
  Reads a 16-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [- MemoryRead16](../pcidriverkit/iopcidevice/memoryread16-50bq8.md)
  Reads a 16-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [- MemoryRead32](../pcidriverkit/iopcidevice/memoryread32-60hg9.md)
  Reads a 32-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [- MemoryRead32](../pcidriverkit/iopcidevice/memoryread32-84jap.md)
  Reads a 32-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [- MemoryRead64](../pcidriverkit/iopcidevice/memoryread64-9ntrf.md)
  Reads a 64-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [- MemoryRead64](../pcidriverkit/iopcidevice/memoryread64-37uob.md)
  Reads a 64-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [- MemoryRead8](../pcidriverkit/iopcidevice/memoryread8-1edw0.md)
  Reads a 8-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [- MemoryRead8](../pcidriverkit/iopcidevice/memoryread8-7b2zp.md)
  Reads a 8-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [- MemoryWrite16](../pcidriverkit/iopcidevice/memorywrite16-8k6ch.md)
  Writes an 16-bit value to the PCI device’s aperture at the specified memory index.
- [- MemoryWrite16](../pcidriverkit/iopcidevice/memorywrite16-534yk.md)
  Writes an 16-bit value to the PCI device’s aperture at the specified memory index.
- [- MemoryWrite32](../pcidriverkit/iopcidevice/memorywrite32-ow7r.md)
  Writes an 32-bit value to the PCI device’s aperture at the specified memory index.
- [- MemoryWrite32](../pcidriverkit/iopcidevice/memorywrite32-4pmh.md)
  Writes an 32-bit value to the PCI device’s aperture at the specified memory index.
- [- MemoryWrite64](../pcidriverkit/iopcidevice/memorywrite64-8qyob.md)
  Writes an 64-bit value to the PCI device’s aperture at the specified memory index.
- [- MemoryWrite64](../pcidriverkit/iopcidevice/memorywrite64-nvpu.md)
  Writes an 64-bit value to the PCI device’s aperture at the specified memory index.
- [- MemoryWrite8](../pcidriverkit/iopcidevice/memorywrite8-fzh6.md)
  Writes an 8-bit value to the PCI device’s aperture at the specified memory index.
- [- MemoryWrite8](../pcidriverkit/iopcidevice/memorywrite8-1uey6.md)
  Writes an 8-bit value to the PCI device’s aperture at the specified memory index.
- [- Open](../pcidriverkit/iopcidevice/open.md)
  Opens a session to the PCI device.
- [- Reset](iopcidevice/3943410-reset.md)
- [- Reset_Impl](iopcidevice/3943411-reset_impl.md)
- [- RestoreDeviceState](iopcidevice/3857680-restoredevicestate.md)
- [- RestoreDeviceState_Impl](iopcidevice/3857681-restoredevicestate_impl.md)
- [- SaveDeviceState](iopcidevice/3857683-savedevicestate.md)
- [- SaveDeviceState_Impl](iopcidevice/3857684-savedevicestate_impl.md)
- [- SetASPMState](iopcidevice/3986557-setaspmstate.md)
- [- SetASPMState_Impl](iopcidevice/3986558-setaspmstate_impl.md)
- [- SetLinkSpeed](iopcidevice/3943413-setlinkspeed.md)
- [- SetLinkSpeed_Impl](iopcidevice/3943414-setlinkspeed_impl.md)
- [- SetProperties_Impl](iopcidevice/3738458-setproperties_impl.md)
- [- addPowerChild](iopcidevice/3928138-addpowerchild.md)
- [- attach](iopcidevice/1398479-attach.md)
- [- callPlatformFunction](iopcidevice/1398982-callplatformfunction.md)
- [- callPlatformFunction](iopcidevice/3516649-callplatformfunction.md)
- [- checkLink](iopcidevice/1398893-checklink.md)
- [- compareName](iopcidevice/1398837-comparename.md)
- [- completeFLR](iopcidevice/4359881-completeflr.md)
- [- configAccess](iopcidevice/1398500-configaccess.md)
- [- configRead16](iopcidevice/1398671-configread16.md)
- [- configRead16](iopcidevice/3516650-configread16.md)
- [- configRead32](iopcidevice/1398925-configread32.md)
- [- configRead32](iopcidevice/3516651-configread32.md)
- [- configRead8](iopcidevice/1398814-configread8.md)
- [- configRead8](iopcidevice/3516652-configread8.md)
- [- configWrite16](iopcidevice/1398984-configwrite16.md)
- [- configWrite16](iopcidevice/3516653-configwrite16.md)
- [- configWrite16Filter](iopcidevice/4116459-configwrite16filter.md)
- [- configWrite32](iopcidevice/1398497-configwrite32.md)
- [- configWrite32](iopcidevice/3516654-configwrite32.md)
- [- configWrite32Filter](iopcidevice/4116460-configwrite32filter.md)
- [- configWrite8](iopcidevice/1398899-configwrite8.md)
- [- configWrite8](iopcidevice/3516655-configwrite8.md)
- [- configWrite8Filter](iopcidevice/4116461-configwrite8filter.md)
- [- configureInterrupts](iopcidevice/3919732-configureinterrupts.md)
- [- copyAERErrorDescriptionForBit](iopcidevice/1398866-copyaererrordescriptionforbit.md)
- [- createEventSource](iopcidevice/1398504-createeventsource.md)
- [- detach](iopcidevice/1398677-detach.md)
- [- detachAbove](iopcidevice/1398929-detachabove.md)
- [- detachFromChild](iopcidevice/4359882-detachfromchild.md)
- [- deviceMemoryRead](iopcidevice/4359883-devicememoryread.md)
- [- deviceMemoryRead16](iopcidevice/3684899-devicememoryread16.md)
- [- deviceMemoryRead16](iopcidevice/4446109-devicememoryread16.md)
- [- deviceMemoryRead32](iopcidevice/3684900-devicememoryread32.md)
- [- deviceMemoryRead32](iopcidevice/4446110-devicememoryread32.md)
- [- deviceMemoryRead64](iopcidevice/3684901-devicememoryread64.md)
- [- deviceMemoryRead64](iopcidevice/4446111-devicememoryread64.md)
- [- deviceMemoryRead8](iopcidevice/3684902-devicememoryread8.md)
- [- deviceMemoryRead8](iopcidevice/4446112-devicememoryread8.md)
- [- deviceMemoryWrite](iopcidevice/4359884-devicememorywrite.md)
- [- deviceMemoryWrite16](iopcidevice/3684903-devicememorywrite16.md)
- [- deviceMemoryWrite16](iopcidevice/4446113-devicememorywrite16.md)
- [- deviceMemoryWrite32](iopcidevice/3684904-devicememorywrite32.md)
- [- deviceMemoryWrite32](iopcidevice/4446114-devicememorywrite32.md)
- [- deviceMemoryWrite64](iopcidevice/3684905-devicememorywrite64.md)
- [- deviceMemoryWrite64](iopcidevice/4446115-devicememorywrite64.md)
- [- deviceMemoryWrite8](iopcidevice/3684906-devicememorywrite8.md)
- [- deviceMemoryWrite8](iopcidevice/4446116-devicememorywrite8.md)
- [- enableACS](iopcidevice/3172732-enableacs.md)
- [- enableLTR](iopcidevice/1398617-enableltr.md)
- [- enablePCIPowerManagement](iopcidevice/1398619-enablepcipowermanagement.md)
- [- extendedConfigRead16](iopcidevice/1398591-extendedconfigread16.md)
- [- extendedConfigRead32](iopcidevice/1398613-extendedconfigread32.md)
- [- extendedConfigRead8](iopcidevice/1398935-extendedconfigread8.md)
- [- extendedConfigWrite16](iopcidevice/1398741-extendedconfigwrite16.md)
- [- extendedConfigWrite32](iopcidevice/1398816-extendedconfigwrite32.md)
- [- extendedConfigWrite8](iopcidevice/1398879-extendedconfigwrite8.md)
- [- extendedFindPCICapability](iopcidevice/1398481-extendedfindpcicapability.md)
- [- findPCICapability](iopcidevice/1398485-findpcicapability.md)
- [- flr](iopcidevice/4359885-flr.md)
- [- free](iopcidevice/1398909-free.md)
  Performs any final cleanup for the object.
- [- getBusNumber](iopcidevice/1398476-getbusnumber.md)
- [- getDeviceMemoryWithIndex](iopcidevice/1398913-getdevicememorywithindex.md)
- [- getDeviceMemoryWithRegister](iopcidevice/1398763-getdevicememorywithregister.md)
- [- getDeviceNumber](iopcidevice/1398803-getdevicenumber.md)
- [- getFunctionNumber](iopcidevice/1398549-getfunctionnumber.md)
- [- getLinkSpeed](iopcidevice/3943417-getlinkspeed.md)
- [- getMetaClass](iopcidevice/1398771-getmetaclass.md)
- [- getProperty](iopcidevice/3753534-getproperty.md)
- [- getResources](iopcidevice/1398852-getresources.md)
- [- handleClose](iopcidevice/3543394-handleclose.md)
- [- handleOpen](iopcidevice/3543395-handleopen.md)
- [- hasPCIPowerManagement](iopcidevice/1398543-haspcipowermanagement.md)
- [- init](iopcidevice/1398907-init.md)
- [- init](iopcidevice/3516656-init.md)
- [- initReserved](iopcidevice/1398669-initreserved.md)
- [- initialPowerStateForDomainState](iopcidevice/1398555-initialpowerstatefordomainstate.md)
- [- ioDeviceMemory](iopcidevice/1398727-iodevicememory.md)
- [- ioRead16](iopcidevice/1398512-ioread16.md)
- [- ioRead32](iopcidevice/1398717-ioread32.md)
- [- ioRead8](iopcidevice/1398588-ioread8.md)
- [- ioWrite16](iopcidevice/1398705-iowrite16.md)
- [- ioWrite32](iopcidevice/1398775-iowrite32.md)
- [- ioWrite8](iopcidevice/1398855-iowrite8.md)
- [- isDownstreamFacing](iopcidevice/4359886-isdownstreamfacing.md)
- [- kernelRequestProbe](iopcidevice/1398761-kernelrequestprobe.md)
- [- launchReprobeThread](iopcidevice/4359887-launchreprobethread.md)
- [- mapDeviceMemoryWithRegister](iopcidevice/1398789-mapdevicememorywithregister.md)
- [- matchLocation](iopcidevice/1398961-matchlocation.md)
- [- matchPropertyTable](iopcidevice/1398666-matchpropertytable.md)
- [- matchPropertyTable](iopcidevice/3538575-matchpropertytable.md)
- [- maxCapabilityForDomainState](iopcidevice/1399002-maxcapabilityfordomainstate.md)
- [- newUserClient](iopcidevice/1398840-newuserclient.md)
- [- powerStateForDomainState](iopcidevice/1398921-powerstatefordomainstate.md)
- [- powerStateWillChangeTo](iopcidevice/1398799-powerstatewillchangeto.md)
- [- powerStateWillChangeToGated](iopcidevice/4359888-powerstatewillchangetogated.md)
- [- prepareFLR](iopcidevice/4359889-prepareflr.md)
- [- protectDevice](iopcidevice/1398709-protectdevice.md)
- [- registerCrashNotification](iopcidevice/3943418-registercrashnotification.md)
- [- relocate](iopcidevice/1398535-relocate.md)
- [- removePowerChild](iopcidevice/3928139-removepowerchild.md)
- [- reprobeThreadCall](iopcidevice/4359890-reprobethreadcall.md)
- [- requestProbe](iopcidevice/1398685-requestprobe.md)
- [- reset](iopcidevice/3943419-reset.md)
- [- resetFunction](iopcidevice/4359891-resetfunction.md)
- [- resetNubState](iopcidevice/4359892-resetnubstate.md)
- [- restoreDeviceState](iopcidevice/1398874-restoredevicestate.md)
- [- saveDeviceState](iopcidevice/1398493-savedevicestate.md)
- [- setASPMState](iopcidevice/1398736-setaspmstate.md)
- [- setBusLeadEnable](iopcidevice/3917649-setbusleadenable.md)
- [- setBusMasterEnable](iopcidevice/1398970-setbusmasterenable.md)
- [- setConfigBits](iopcidevice/1398640-setconfigbits.md)
- [- setConfigHandler](iopcidevice/1398553-setconfighandler.md)
- [- setIOEnable](iopcidevice/1398888-setioenable.md)
- [- setLatencyTolerance](iopcidevice/1398903-setlatencytolerance.md)
- [- setLinkSpeed](iopcidevice/3943420-setlinkspeed.md)
- [- setMemoryEnable](iopcidevice/1398630-setmemoryenable.md)
- [- setPCIPowerState](iopcidevice/1398828-setpcipowerstate.md)
- [- setPowerState](iopcidevice/1398729-setpowerstate.md)
- [- setPowerStateGated](iopcidevice/4359893-setpowerstategated.md)
- [- setProperties](iopcidevice/1398957-setproperties.md)
- [- setProperty](iopcidevice/4097725-setproperty.md)
- [- setProperty](iopcidevice/4097726-setproperty.md)
- [- setProperty](iopcidevice/4097727-setproperty.md)
- [- setProperty](iopcidevice/4097728-setproperty.md)
- [- setProperty](iopcidevice/4097729-setproperty.md)
- [- setProperty](iopcidevice/4097730-setproperty.md)
- [- setProperty](iopcidevice/4097731-setproperty.md)
- [- setTunnelL1Enable](iopcidevice/1398498-settunnell1enable.md)
- [- shouldSkipReset](iopcidevice/4395252-shouldskipreset.md)
- [- supportsFLR](iopcidevice/4359894-supportsflr.md)
- [- unregisterCrashNotification](iopcidevice/3943421-unregistercrashnotification.md)
- [- updateWakeReason](iopcidevice/1398863-updatewakereason.md)
### Type Methods
- [+ ConfigureInterrupts_Invoke](iopcidevice/3919731-configureinterrupts_invoke.md)
- [+ EnablePCIPowerManagement_Invoke](iopcidevice/3516631-enablepcipowermanagement_invoke.md)
- [+ FindPCICapability_Invoke](iopcidevice/3516634-findpcicapability_invoke.md)
- [+ GetBARInfo_Invoke](iopcidevice/3861821-getbarinfo_invoke.md)
- [+ GetBusDeviceFunction_Invoke](iopcidevice/3516637-getbusdevicefunction_invoke.md)
- [+ GetLinkSpeed_Invoke](iopcidevice/3943409-getlinkspeed_invoke.md)
- [+ HasPCIPowerManagement_Invoke](iopcidevice/3516640-haspcipowermanagement_invoke.md)
- [+ Reset_Invoke](iopcidevice/3943412-reset_invoke.md)
- [+ RestoreDeviceState_Invoke](iopcidevice/3857682-restoredevicestate_invoke.md)
- [+ SaveDeviceState_Invoke](iopcidevice/3857685-savedevicestate_invoke.md)
- [+ SetASPMState_Invoke](iopcidevice/3986559-setaspmstate_invoke.md)
- [+ SetLinkSpeed_Invoke](iopcidevice/3943415-setlinkspeed_invoke.md)
- [+ getCloseCommandMask](iopcidevice/3943416-getclosecommandmask.md)
- [+ hasL1Errata](iopcidevice/4480432-hasl1errata.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [Implementing a PCIe Kext for a Thunderbolt Device](hardware_families/pci/implementing_a_pcie_kext_for_a_thunderbolt_device.md)
  Create an IOKit driver to support Thunderbolt devices that implement features not supported in PCIDriverKit, such as wireless networking or audio. 
- [IOAGPDevice](ioagpdevice.md)
  An IOService class representing an AGP primary device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopcidevice)*