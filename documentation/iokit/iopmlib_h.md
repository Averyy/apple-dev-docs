# IOPMLib.h

**Framework**: IOKit  
**Role**: API Collection

IOPMLib provides access to common power management facilities, like initiating system sleep, getting current idle timer values, registering for sleep/wake notifications, and preventing system sleep.

## Overview

### Included Headers

- <CoreFoundation/CFArray.h>
- <IOKit/IOKitLib.h>
- <IOKit/pwr_mgt/IOPMLibDefs.h>
- <IOKit/pwr_mgt/IOPMKeys.h>
- <Availability.h>

## Topics

### ScheduledEvents
- [IOPMCancelScheduledPowerEvent](./api-1557116-iopmcancelscheduledpowerevent.md)
  Cancel a previously scheduled power event.
- [IOPMCopyScheduledPowerEvents](./api-1557109-iopmcopyscheduledpowerevents.md)
  List all scheduled system power events
- [IOPMSchedulePowerEvent](./api-1557076-iopmschedulepowerevent.md)
  Schedule the machine to wake from sleep, power on, go to sleep, or shutdown.
### Notifications
- [IOAllowPowerChange](./api-1557064-ioallowpowerchange.md)
  The caller acknowledges notification of a power state change on a device it has registered for notifications for via IORegisterForSystemPower or IORegisterApp.
- [IOCancelPowerChange](./api-1557115-iocancelpowerchange.md)
  The caller denies an idle system sleep power state change.
- [IODeregisterApp](./api-1557129-ioderegisterapp.md)
  Disconnects the caller from an IOService after receiving power state change notifications from the IOService. (Caller must also release IORegisterApp's return io_connect_t and returned IONotificationPortRef for complete clean-up).
- [IODeregisterForSystemPower](./api-1557132-ioderegisterforsystempower.md)
  Disconnects the caller from the Root Power Domain IOService after receiving system power state change notifications. (Caller must also destroy the IONotificationPortRef returned from IORegisterForSystemPower.)
- [IORegisterApp](./api-1557102-ioregisterapp.md)
  Connects the caller to an IOService for the purpose of receiving power state change notifications for the device controlled by the IOService.
- [IORegisterForSystemPower](./api-1557114-ioregisterforsystempower.md)
  Connects the caller to the Root Power Domain IOService for the purpose of receiving sleep & wake notifications for the system. Does not provide system shutdown and restart notifications.
### IOSystemLoadAdvisory
- [IOCopySystemLoadAdvisoryDetailed](./api-1557099-iocopysystemloadadvisorydetailed.md)
  Indicates how user activity, battery level, and thermal level each contribute to the overall "SystemLoadAdvisory" level. In the future, this combined level may represent new levels as well.
- [IOGetSystemLoadAdvisory](./api-1557110-iogetsystemloadadvisory.md)
  Returns a hint about whether now would be a good time to perform time-insensitive work.
### CPU Power & Thermal
- [IOPMCopyCPUPowerStatus](./api-1557079-iopmcopycpupowerstatus.md)
  Copy status of all current CPU power levels.
- [IOPMGetThermalWarningLevel](./api-1557103-iopmgetthermalwarninglevel.md)
  Get thermal warning level of the system.
### Assertions
- [IOPMAssertionCopyProperties](./api-1557066-iopmassertioncopyproperties.md)
  Copies details about an `IOPMAssertion`
- [IOPMAssertionCreate](./api-1557118-iopmassertioncreate.md)
  Dynamically requests a system behavior from the power management system.
- [IOPMAssertionCreateWithDescription](./api-1557078-iopmassertioncreatewithdescripti.md)
- [IOPMAssertionCreateWithName](./api-1557134-iopmassertioncreatewithname.md)
  Dynamically requests a system behavior from the power management system.
- [IOPMAssertionCreateWithProperties](./api-1557082-iopmassertioncreatewithpropertie.md)
  Creates an IOPMAssertion with more flexibility than [`IOPMAssertionCreateWithDescription`](./api-1557078-iopmassertioncreatewithdescripti.md).
- [IOPMAssertionDeclareUserActivity](./api-1557127-iopmassertiondeclareuseractivity.md)
  Declares that the user is active on the system. This causes the display to power on and postpone display sleep up to the user's display sleep Energy Saver settings. If you prefer to hold the display awake for a longer period and you know how long you'd like to hold it, consider taking assertion [`kIOPMAssertionTypePreventUserIdleDisplaySleep`](./kiopmassertiontypepreventuseridledisplaysleep.md) using [`IOPMAssertionCreateWithDescription`](./api-1557078-iopmassertioncreatewithdescripti.md) API instead.
- [IOPMAssertionRelease](./api-1557090-iopmassertionrelease.md)
  Decrements the assertion's retain count.
- [IOPMAssertionRetain](./api-1557071-iopmassertionretain.md)
  Increments the assertion's retain count.
- [IOPMAssertionSetProperty](./api-1557107-iopmassertionsetproperty.md)
  Sets a property in the assertion.
- [IOPMCopyAssertionsByProcess](./api-1557130-iopmcopyassertionsbyprocess.md)
  Returns a dictionary listing all assertions, grouped by their owning process.
- [IOPMCopyAssertionsStatus](./api-1557072-iopmcopyassertionsstatus.md)
  Returns a list of available assertions and their system-wide levels.
### Miscellaneous
- [IOPMAssertionDictionaryKeys](./iopmlib_h/iopmassertiondictionarykeys.md)
- [IOPMAssertionTypes](./iopmlib_h/iopmassertiontypes.md)
  Use as AssertionType argument to [`IOPMAssertionCreate`](./api-1557118-iopmassertioncreate.md). The idle display will not sleep when enabled, and consequently the system will not idle sleep.
- [IOPMCopyBatteryInfo](./api-1557138-iopmcopybatteryinfo.md)
  Request raw battery data from the system.
- [IOPMFindPowerManagement](./api-1557133-iopmfindpowermanagement.md)
  Finds the Root Power Domain IOService.
- [IOPMGetAggressiveness](./api-1557117-iopmgetaggressiveness.md)
  Retrieves the current value of one of the aggressiveness factors in IOKit Power Management.
- [IOPMSetAggressiveness](./api-1557098-iopmsetaggressiveness.md)
  Sets one of the aggressiveness factors in IOKit Power Management.
- [IOPMSleepEnabled](./api-1557074-iopmsleepenabled.md)
  Tells whether the system supports full sleep, or just doze
- [IOPMSleepSystem](./api-1557121-iopmsleepsystem.md)
  Request that the system initiate sleep.
### Data Types
- [IOPMAssertionID](./iopmassertionid.md)
  Type for AssertionID arguments to [`IOPMAssertionCreateWithProperties`](./api-1557082-iopmassertioncreatewithpropertie.md) and [`IOPMAssertionRelease`](./api-1557090-iopmassertionrelease.md)
- [IOPMAssertionLevel](./iopmassertionlevel.md)
  Type for AssertionLevel argument to IOPMAssertionCreate
- [IOSystemLoadAdvisoryLevel](./iosystemloadadvisorylevel.md)
  Return type for IOGetSystemLoadAdvisory
### Constants
- [Defines](./iopmlib_h/defines.md)
- [Assertion](./api-1557096-assertion.md)
  Level for an enabled assertion, passed as an argument to IOPMAssertionCreate.
- [kIOPMNullAssertionID](./api-1557135-kiopmnullassertionid.md)
  This value represents a non-initialized assertion ID


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iopmlib_h)*