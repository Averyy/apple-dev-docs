# IOPMPowerSource

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOPMPowerSource : IOService
```

#### Overview

See IOKit/pwr_mgt/IOPM.h for power source keys relevant to this class. These report-type keys are required for calls to IOPMPowerSource::setReportables(), and they define the IORegistry interface through which data is passed back up to the rest of the system.

A subclassing driver that doesn't want to do anything fancy should:

1. Subclass IOPMPowerSource
2. Install its own battery change notifications or polling routine that can converse with actual battery hardware.
3. When battery state changes, change the relevant member variables through setCurrentCapacity() style accessors.
4. Call updateStatus() on itself when all such settings have been updated.

The subclass driver should also initially populate its settings and call updateStatus() on launch.

Settings:

```occ
 
 ExternalConnected
 Type: bool
 IORegistry Key: kIOPMPSExternalConnectedKey
 True if computer is drawing external power
 
 ExternalChargeCapable
 Type: bool
 IORegistry Key: kIOPMPSExternalChargeCapableKey
 True if external power is capable of charging internal battery
 
 BatteryInstalled
 Type: bool
 IORegistry Key: kIOPMPSBatteryInstalledKey
 True if a battery is present; false if removed
 
 IsCharging
 Type: bool
 IORegistry Key: kIOPMPSIsChargingKey
 True if battery is charging itself from external power
 
 AtWarnLevel
 Type: bool
 IORegistry Key: kIOPMPSAtWarnLevelKey
 True if draining battery capacity and past warn level
 
 AtCriticalLevel
 Type: bool
 IORegistry Key: kIOPMPSAtCriticalLevelKey
 True if draining battery capacity and past critical level
 
 CurrentCapacity
 MaxCapacity
 Type: unsigned int
 IORegistry Key: kIOPMPSCurrentCapacityKey, kIOPMPSMaxCapacityKey
 Capacity measured in mAh
 
 TimeRemaining
 Type: int
 IORegistry Key: kIOPMPSTimeRemainingKey
 Time remaining measured in minutes
 
 Amperage
 Type: int
 IORegistry Key: kIOPMPSAmperageKey
 Current is measured in mA
 
 Voltage
 Type: unsigned int
 IORegistry Key: kIOPMPSVoltageKey
 Voltage measured in mV
 
 CycleCount
 Type: unsigned int
 IORegistry Key: kIOPMPSCycleCountKey
 Number of charge/discharge cycles
 
 AdapterInfo
 Type: int
 IORegistry Key: kIOPMPSAdapterInfoKey
 Power adapter information
 
 Location
 Type: int
 IORegistry Key: kIOPMPSLocationKey
 Clue about battery's location in machine - Left vs. Right
 
 ErrorCondition
 Type: OSSymbol
 IORegistry Key: kIOPMPSErrorConditionKey
 String describing error state of battery
 
 Manufacturer
 Type: OSSymbol
 IORegistry Key: kIOPMPSManufacturerKey
 String describing battery manufacturer
 
 Manufactured Date
 Type: unsigned 16-bit bitfield
 IORegistry Key: kIOPMPSManufactureDateKey
 Date is published in a bitfield per the Smart Battery Data spec rev 1.1
 in section 5.1.26
   Bits 0...4 => day (value 1-31; 5 bits)
   Bits 5...8 => month (value 1-12; 4 bits)
   Bits 9...15 => years since 1980 (value 0-127; 7 bits)
 
 Model
 Type: OSSymbol
 IORegistry Key: kIOPMPSModelKey
 String describing model number
 
 Serial
 Type: OSSymbol
 IORegistry Key: kIOPMPSSerialKey
 String describing serial number or unique info
 The serial number published hear bears no correspondence to the Apple serial
 number printed on each battery. This is a manufacturer serial number with
 no correlation to the printed serial number.
 
 LegacyIOBatteryInfo
 Type: OSDictionary
 IORegistry Key: kIOPMPSLegacyBatteryInfoKey
 Dictionary conforming to the OS X 10.0-10.4
 
```

## Topics

### Miscellaneous
- [powerSource](iopmpowersource/1809904-powersource.md)
  Creates a new IOPMPowerSource nub. Must be attached to IORegistry, and registered by provider.
- [setPSProperty](iopmpowersource/1809917-setpsproperty.md)
- [updateStatus](iopmpowersource/1809926-updatestatus.md)
  Must be called by physical battery controller when battery state has changed significantly.
### Instance Variables
- [settingsChangedSinceUpdate](iopmpowersource/settingschangedsinceupdate.md)
- [properties](iopmpowersource/properties.md)
### Instance Methods
- [- adapterInfo](iopmpowersource/1543712-adapterinfo.md)
- [- amperage](iopmpowersource/1543726-amperage.md)
- [- atCriticalLevel](iopmpowersource/1543768-atcriticallevel.md)
- [- atWarnLevel](iopmpowersource/1543776-atwarnlevel.md)
- [- batteryInstalled](iopmpowersource/1543775-batteryinstalled.md)
- [- capacityPercentRemaining](iopmpowersource/1543736-capacitypercentremaining.md)
- [- currentCapacity](iopmpowersource/1543777-currentcapacity.md)
- [- cycleCount](iopmpowersource/1543711-cyclecount.md)
- [- errorCondition](iopmpowersource/1543760-errorcondition.md)
- [- externalChargeCapable](iopmpowersource/1543708-externalchargecapable.md)
- [- externalConnected](iopmpowersource/1543749-externalconnected.md)
- [- free](iopmpowersource/1543728-free.md)
- [- getMetaClass](iopmpowersource/1543720-getmetaclass.md)
- [- getPSProperty](iopmpowersource/1543772-getpsproperty.md)
- [- init](iopmpowersource/1543771-init.md)
- [- isCharging](iopmpowersource/1543769-ischarging.md)
- [- legacyIOBatteryInfo](iopmpowersource/1543735-legacyiobatteryinfo.md)
- [- location](iopmpowersource/1543759-location.md)
- [- manufacturer](iopmpowersource/1543716-manufacturer.md)
- [- maxCapacity](iopmpowersource/1543724-maxcapacity.md)
- [- model](iopmpowersource/1543766-model.md)
- [- serial](iopmpowersource/1543709-serial.md)
- [- setAdapterInfo](iopmpowersource/1543733-setadapterinfo.md)
- [- setAmperage](iopmpowersource/1543739-setamperage.md)
- [- setAtCriticalLevel](iopmpowersource/1543731-setatcriticallevel.md)
- [- setAtWarnLevel](iopmpowersource/1543755-setatwarnlevel.md)
- [- setBatteryInstalled](iopmpowersource/1543762-setbatteryinstalled.md)
- [- setCurrentCapacity](iopmpowersource/1543706-setcurrentcapacity.md)
- [- setCycleCount](iopmpowersource/1543758-setcyclecount.md)
- [- setErrorCondition](iopmpowersource/1543748-seterrorcondition.md)
- [- setExternalChargeCapable](iopmpowersource/1543743-setexternalchargecapable.md)
- [- setExternalConnected](iopmpowersource/1543764-setexternalconnected.md)
- [- setIsCharging](iopmpowersource/1543734-setischarging.md)
- [- setLegacyIOBatteryInfo](iopmpowersource/1543714-setlegacyiobatteryinfo.md)
- [- setLocation](iopmpowersource/1543722-setlocation.md)
- [- setManufacturer](iopmpowersource/1543729-setmanufacturer.md)
- [- setMaxCapacity](iopmpowersource/1543719-setmaxcapacity.md)
- [- setModel](iopmpowersource/1543773-setmodel.md)
- [- setPSProperty](iopmpowersource/1543767-setpsproperty.md)
- [- setSerial](iopmpowersource/1543747-setserial.md)
- [- setTimeRemaining](iopmpowersource/1543753-settimeremaining.md)
- [- setVoltage](iopmpowersource/1543751-setvoltage.md)
- [- timeRemaining](iopmpowersource/1543738-timeremaining.md)
- [- updateStatus](iopmpowersource/1543745-updatestatus.md)
- [- voltage](iopmpowersource/1543763-voltage.md)
### Type Methods
- [+ powerSource](iopmpowersource/1543765-powersource.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IOACPIPlatformDevice](ioacpiplatformdevice.md)
- [IOACPIPlatformExpert](ioacpiplatformexpert.md)
- [IOPMPowerSourceList](iopmpowersourcelist.md)
- [IOPMrootDomain](iopmrootdomain.md)
- [IOPowerConnection](iopowerconnection.md)
- [IOPwrController](iopwrcontroller.md)
- [IOACPIAddress](ioacpiaddress.md)
- [IOACPIAddressSpaceDescriptor](ioacpiaddressspacedescriptor.md)
- [IOACPIAddressSpaceHandler](ioacpiaddressspacehandler.md)
- [IOACPIAddressSpaceID](ioacpiaddressspaceid.md)
- [IOPMPowerState](iopmpowerstate.md)
- [acknowledgeSleepWakeNotification](1579170-acknowledgesleepwakenotification.md)
- [gIOACPIAddressKey](gioacpiaddresskey.md)
- [gIOACPIDeviceStatusKey](gioacpidevicestatuskey.md)
- [gIOACPIHardwareIDKey](gioacpihardwareidkey.md)
- [gIOACPIPlane](gioacpiplane.md)
- [gIOACPIUniqueIDKey](gioacpiuniqueidkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopmpowersource)*