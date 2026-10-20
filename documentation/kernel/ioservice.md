# IOService

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

The base class for most I/O Kit families, devices, and drivers.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOService : IORegistryEntry
```

#### Overview

[`IOService`](./ioservice.md) provides general utility functions that are useful across all families. It defines APIs used to publish services, instantiates other services based on the existence of a providing service such as driver stacking, destroys a service and its dependent stack, and notifies interested parties of service state changes.

This class uses a *matching dictionary* that contains service type properties to discover supported devices. For example, a matching dictionary may describe a [`IOUSBHostDevice`](../USBDriverKit/iousbhostdevice.md) (or subclass), an [`IOUSBHostDevice`](../USBDriverKit/iousbhostdevice.md) with a certain class code, or an [`IOPCIDevice`](./iopcidevice.md) with a set of matching names or device and vendor IDs. The list of properties considered for matching depends on the family that creates the dictionary.

Matching dictionaries are associated with [`IOService`](./ioservice.md) classes by the catalogue, as driver property tables, and also supplied by clients of the notification APIs.

[`IOService`](./ioservice.md) performs matching based on several criteria: the C++ class (using [`OSMetaClass`](./osmetaclass.md) dynamic casting), the registry entry name, a registry path to the service (which includes device tree paths), a name assigned by BSD, or  location (point of attachment).

##### Instantiate Drivers

Drivers are subclasses of [`IOService`](./ioservice.md), and the catalogue manages their availability. The system instantiates drivers based on the publication of an [`IOService`](./ioservice.md) they use (for example, an [`IOPCIDevice`](./iopcidevice.md) or [`IOUSBHostDevice`](../USBDriverKit/iousbhostdevice.md)), or when they are added to the catalogue and the I/O services they use are already available.

When [`registerService`](./ioservice/api-1532797-registerservice.md) publishes the IOService, the matching and probing process begins. This is always single threaded per provider. The system constructs a list of matching dictionaries from the catalogue and installed publish notification requests that successfully match the service, along with ordering supplied by `kIOProbeScoreKey` in the dictionary, or supplied with the notification. Each entry in the list is then processed in order. For notifications, the notification is delivered. For driver property tables, a lot more happens.

The system instantiates the driver class and calls `init()` with its property table, attaches the new driver instance to the provider, and calls [`probe`](./ioservice/api-1532835-probe.md) with the provider as an argument. The default `probe` method returns success — your driver should implement this method to interrogate the provider to make sure it can work with it. It may also modify its probe score at this time. After probing, the system detaches the driver and attaches the next one in the list for probing.

When the probing phase completes, the list consists of successfully probed drivers, in order of their probe score (after adjustments during the [`probe`](./ioservice/api-1532835-probe.md) call). The system divides the list into categories based on the `kIOMatchCategoryKey` property. Drivers without a match category are considered in one default category. Match categories allow multiple clients of a provider to attach and start, though the provider may also enforce open/close semantics to gain active access to it.

For each category, the system attaches the highest scoring driver in that category to the provider, then calls [start](./iohidinterface/api-1812781-start.md). If the method returns success, the system discards the rest of the drivers in the same match category; otherwise, it starts the next highest scoring driver.

The driver should only consider itself ready for work when the system calls its [start](./iohidinterface/api-1812781-start.md) method. This indicates that the driver is using the provider and consuming that match category. The driver should also be prepared for allocation, probing and freeing, even if the probe is successful.

After the drivers are synchronously started, the system delivers the installed “matched” notifications that match the registered service.

##### Match with Service Properties

Here are the service properties you can use when setting up the matching dictionary.

- **`kIOClassKey`**: The class of the driver to instantiate on matching providers.
- **`kIOProviderClassKey`**: The class of the provider(s) to be considered for matching, checked with [`OSDynamicCast`](../DriverKit/osdynamiccast.md) so subclasses will also match.
- **`kIOProbeScoreKey`**: The probe score initially used to order multiple matching drivers.
- **`kIOMatchCategoryKey`**: A string defining the driver category for matching purposes. All drivers without the [`kIOMatchCategoryKey`](../iokit/kiomatchcategorykey.md) property are considered to be in the same default category. Only one driver in a category can be started on each provider.
- **`kIONameMatchKey`**: A string or collection of strings that match the provider’s name. The comparison is implemented with the [`compareNames`](./ioregistryentry/api-1437634-comparenames.md) method, which supports a single string, or any collection such as `OSArray`, [`OSSet`](./osset.md), or [`OSDictionary`](./osdictionary.md). of strings. [`IOService`](../DriverKit/ioservice.md) objects with device tree properties such as  [`IOPCIDevice`](./iopcidevice.md) are matched based on that standard’s “compatible”, “name”, “device_type” properties. The matching name is left in the driver’s property table in the [`kIONameMatchedKey`](../iokit/kionamematchedkey.md) property.
- **`kIONameMatchedKey`**: The successfully matched name from the [`kIONameMatchKey`](../iokit/kionamematchkey.md) property is left in the driver’s property table as the [`kIONameMatchedKey`](../iokit/kionamematchedkey.md) property.
- **`kIOPropertyMatchKey`**: A dictionary of properties that must exist in the matching [`IOService`](./ioservice.md), and compare successfully with [isEqualTo](./osmetaclassbase/api-1808069-isequalto.md).
- **`kIOUserClientClassKey`**: The class name that the service will attempt to allocate when a user client connection is requested. The system queries the device nub first, then the nub’s provider.
- **`kIOKitDebugKey`**: Debug flags for logging the driver loading process. Flags are defined in `IOKit/IOKitDebug.h`.

## Topics

### Miscellaneous
- [acknowledgePowerChange](./ioservice/api-1809710-acknowledgepowerchange.md)
  Acknowledges an in-progress power state change.
- [- acknowledgeSetPowerState](./ioservice/api-1532596-acknowledgesetpowerstate.md)
  Acknowledges the belated completion of a driver’s setPowerState power state change.
- [activityTickle](./ioservice/api-1809731-activitytickle.md)
  Informs power management when a power-managed device is in use, so that power management can track when it is idle and adjust its power state accordingly.
- [addLocation](./ioservice/api-1809740-addlocation.md)
  Adds a location matching property to an existing dictionary.
- [addMatchingNotification](./ioservice/api-1809749-addmatchingnotification.md)
  Adds a persistant notification handler to be notified of IOService events.
- [addNotification](./ioservice/api-1809760-addnotification.md)
  Deprecated use addMatchingNotification(). Adds a persistant notification handler to be notified of IOService events.
- [addPowerChild](./ioservice/api-1809766-addpowerchild.md)
  Informs a driver that it has a new child.
- [adjustBusy](./ioservice/api-1809776-adjustbusy.md)
  Adjusts the `busyState` of an IOService object.
- [attach](./ioservice/api-1809786-attach.md)
  Attaches an IOService client to a provider in the I/O Registry.
- [callPlatformFunction](./ioservice/api-1809795-callplatformfunction.md)
  Calls the platform function with the given name.
- [causeInterrupt](./ioservice/api-1809803-causeinterrupt.md)
  Causes a device interrupt to occur.
- [changePowerStateTo](./ioservice/api-1809809-changepowerstateto.md)
  Sets a driver's power state.
- [changePowerStateToPriv](./ioservice/api-1809819-changepowerstatetopriv.md)
  Tells a driver's superclass to change the power state of its device.
- [clampPowerOn](./ioservice/api-1809824-clamppoweron.md)
  Deprecated. Do not use.
- [close](./ioservice/api-1809831-close.md)
  Releases active access to a provider.
- [command_received](./ioservice/api-1809840-command_received.md)
- [compareProperties](./ioservice/api-1809848-compareproperties.md)
  Compares a set of properties in a matching dictionary with an IOService object's property table.
- [compareProperty(OSDictionary *, const char *)](./ioservice/api-1809855-compareproperty.md)
  Compares a property in a matching dictionary with an IOService object's property table.
- [compareProperty(OSDictionary *, const OSString *)](./ioservice/api-1809861-compareproperty.md)
  Compares a property in a matching dictionary with an IOService object's property table.
- [configureReport](./ioservice/api-1809870-configurereport.md)
  configure IOReporting channels
- [copyClientWithCategory](./ioservice/api-1809878-copyclientwithcategory.md)
- [copyMatchingService](./ioservice/api-1809887-copymatchingservice.md)
  Finds one of the current published IOService objects matching a matching dictionary.
- [currentCapability](./ioservice/api-1809891-currentcapability.md)
  Finds out the capability of a device's current power state.
- [currentPowerConsumption](./ioservice/api-1809899-currentpowerconsumption.md)
  Finds out the current power consumption of a device.
- [deRegisterInterestedDriver](./ioservice/api-1809905-deregisterinteresteddriver.md)
  De-registers power state interest from a previous call to `registerInterestedDriver`.
- [detach](./ioservice/api-1809913-detach.md)
  Detaches an IOService client from a provider in the I/O Registry.
- [didTerminate](./ioservice/api-1809918-didterminate.md)
  Passes a termination up the stack.
- [didYouWakeSystem](./ioservice/api-1809924-didyouwakesystem.md)
  Asks a driver if its device is the one that just woke the system from sleep.
- [disableInterrupt](./ioservice/api-1809929-disableinterrupt.md)
  Synchronously disables a device interrupt.
- [enableInterrupt](./ioservice/api-1809937-enableinterrupt.md)
  Enables a device interrupt.
- [errnoFromReturn](./ioservice/api-1809942-errnofromreturn.md)
  Translates an IOReturn code to a BSD `errno`.
- [finalize](./ioservice/api-1809948-finalize.md)
  Finalizes the destruction of an IOService object.
- [free](./ioservice/api-1809960-free.md)
  Frees data structures that were allocated when power management was initialized on this service.
- [getAggressiveness](./ioservice/api-1809962-getaggressiveness.md)
  Returns the current aggressiveness value for the given type.
- [getBusyState](./ioservice/api-1809968-getbusystate.md)
  Returns the `busyState` of an IOService object.
- [getClient](./ioservice/api-1809973-getclient.md)
  Returns an IOService object's primary client.
- [getClientIterator](./ioservice/api-1809979-getclientiterator.md)
  Returns an iterator over an IOService object's clients.
- [getDeviceMemory](./ioservice/api-1809984-getdevicememory.md)
  Returns the array of IODeviceMemory objects representing a device's memory mapped ranges.
- [getDeviceMemoryCount](./ioservice/api-1809990-getdevicememorycount.md)
  Returns a count of the physical memory ranges available for a device.
- [getDeviceMemoryWithIndex](./ioservice/api-1809999-getdevicememorywithindex.md)
  Returns an instance of IODeviceMemory representing one of a device's memory mapped ranges.
- [getInterruptType](./ioservice/api-1810004-getinterrupttype.md)
  Returns the type of interrupt used for a device supplying hardware interrupts.
- [getMatchingServices](./ioservice/api-1810011-getmatchingservices.md)
  Finds the set of current published IOService objects matching a matching dictionary.
- [getOpenClientIterator](./ioservice/api-1810018-getopenclientiterator.md)
  Returns an iterator over a provider's clients that currently have opened the provider.
- [getOpenProviderIterator](./ioservice/api-1810027-getopenprovideriterator.md)
  Returns an iterator over an client's providers that are currently opened by the client.
- [getPlatform](./ioservice/api-1810033-getplatform.md)
  Returns a pointer to the platform expert instance for the computer.
- [getPMRootDomain](./ioservice/api-1810046-getpmrootdomain.md)
  Returns a pointer to the power management root domain instance for the computer.
- [getPMworkloop](./ioservice/api-1810059-getpmworkloop.md)
  Returns a pointer to the system-wide power management work loop.
- [getPowerState](./ioservice/api-1810074-getpowerstate.md)
  Determines a device's power state.
- [getProvider](./ioservice/api-1810088-getprovider.md)
  Returns an IOService object's primary provider.
- [getProviderIterator](./ioservice/api-1810097-getprovideriterator.md)
  Returns an iterator over an IOService object's providers.
- [getResources](./ioservice/api-1810107-getresources.md)
  Allocates any needed resources for a published IOService object before clients attach.
- [getResourceService](./ioservice/api-1810116-getresourceservice.md)
  Returns a pointer to the IOResources service.
- [getServiceRoot](./ioservice/api-1810122-getserviceroot.md)
  Returns a pointer to the root of the service plane.
- [getState](./ioservice/api-1810137-getstate.md)
  Accessor for IOService state bits, not normally needed or used outside IOService.
- [getWorkLoop](./ioservice/api-1810145-getworkloop.md)
  Returns the current work loop or `provider->getWorkLoop`.
- [handleClose](./ioservice/api-1810153-handleclose.md)
  Controls the open / close behavior of an IOService object (overrideable by subclasses).
- [handleIsOpen](./ioservice/api-1810164-handleisopen.md)
  Controls the open / close behavior of an IOService object (overrideable by subclasses).
- [handleOpen](./ioservice/api-1810174-handleopen.md)
  Controls the open / close behavior of an IOService object (overrideable by subclasses).
- [initialPowerStateForDomainState](./ioservice/api-1810182-initialpowerstatefordomainstate.md)
  Determines which power state a device is in, given the current power domain state.
- [isInactive](./ioservice/api-1810198-isinactive.md)
  Checks if the IOService object has been terminated, and is in the process of being destroyed.
- [isOpen](./ioservice/api-1810209-isopen.md)
  Determines whether a specific, or any, client has an IOService object open.
- [joinPMtree](./ioservice/api-1810216-joinpmtree.md)
  Joins the driver into the power plane of the I/O Registry.
- [lockForArbitration](./ioservice/api-1810228-lockforarbitration.md)
  Locks an IOService object against changes in state or ownership.
- [makeUsable](./ioservice/api-1810246-makeusable.md)
  Requests that a device become usable.
- [mapDeviceMemoryWithIndex](./ioservice/api-1810261-mapdevicememorywithindex.md)
  Maps a physical range of a device.
- [matchLocation](./ioservice/api-1810275-matchlocation.md)
  Allows a registered IOService object to direct location matching.
- [matchPropertyTable](./ioservice/api-1810286-matchpropertytable.md)
  Allows a registered IOService object to implement family specific matching.
- [maxCapabilityForDomainState](./ioservice/api-1810302-maxcapabilityfordomainstate.md)
  Determines a driver's highest power state possible for a given power domain state.
- [message](./ioservice/api-1810323-message.md)
  Receives a generic message delivered from an attached provider.
- [messageClient](./ioservice/api-1810334-messageclient.md)
  Sends a generic message to an attached client.
- [messageClients](./ioservice/api-1810353-messageclients.md)
  Sends a generic message to all attached clients.
- [nameMatching(const char *, OSDictionary *)](./ioservice/api-1810365-namematching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify an IOService name match.
- [nameMatching(const OSString *, OSDictionary *)](./ioservice/api-1810383-namematching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify an IOService name match.
- [newTemperature](./ioservice/api-1810402-newtemperature.md)
  Tells a power managed driver that the temperature in the thermal zone has changed.
- [newUserClient](./ioservice/api-1810417-newuserclient.md)
  Creates a connection for a non kernel client.
- [nextIdleTimeout](./ioservice/api-1810435-nextidletimeout.md)
  Allows subclasses to customize idle power management behavior.
- [open](./ioservice/api-1810450-open.md)
  Requests active access to a provider.
- [PM_Clamp_Timer_Expired](./ioservice/api-1810463-pm_clamp_timer_expired.md)
- [PM_idle_timer_expiration](./ioservice/api-1810474-pm_idle_timer_expiration.md)
- [PMinit](./ioservice/api-1810486-pminit.md)
  Initializes power management for a driver.
- [PMstop](./ioservice/api-1810502-pmstop.md)
  Stop power managing the driver.
- [powerChangeDone](./ioservice/api-1810518-powerchangedone.md)
  Tells a driver when a power state change is complete.
- [powerOverrideOffPriv](./ioservice/api-1810533-poweroverrideoffpriv.md)
  Allows a driver to disable a power override.
- [powerOverrideOnPriv](./ioservice/api-1810549-poweroverrideonpriv.md)
  Allows a driver to ignore its children's power management requests and only use changePowerStateToPriv to define its own power state.
- [powerStateDidChangeTo](./ioservice/api-1810564-powerstatedidchangeto.md)
  Informs interested parties that a device has changed to a different power state.
- [powerStateForDomainState](./ioservice/api-1810576-powerstatefordomainstate.md)
  Determines what power state the device would be in for a given power domain state.
- [powerStateWillChangeTo](./ioservice/api-1810597-powerstatewillchangeto.md)
  Informs interested parties that a device is about to change its power state.
- [probe](./ioservice/api-1810605-probe.md)
  During an IOService object's instantiation, probes a matched service to see if it can be used.
- [propertyMatching](./ioservice/api-1810622-propertymatching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify an IOService phandle match.
- [publishResource(const char *, OSObject *)](./ioservice/api-1810642-publishresource.md)
  Uses the resource service to publish a property.
- [publishResource(const OSSymbol *, OSObject *)](./ioservice/api-1810661-publishresource.md)
  Uses the resource service to publish a property.
- [registerInterestedDriver](./ioservice/api-1810675-registerinteresteddriver.md)
  Allows an IOService object to register interest in the changing power state of a power-managed IOService object.
- [registerInterrupt](./ioservice/api-1810691-registerinterrupt.md)
  Registers a C function interrupt handler for a device supplying interrupts.
- [registerPowerDriver](./ioservice/api-1810706-registerpowerdriver.md)
  Registers a set of power states that the driver supports.
- [registerService](./ioservice/api-1810726-registerservice.md)
  Starts the registration process for a newly discovered IOService object.
- [registryEntryIDMatching](./ioservice/api-1810750-registryentryidmatching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify a IORegistryEntryID match.
- [removePowerChild](./ioservice/api-1810770-removepowerchild.md)
  Informs a power managed driver that one of its power plane childen is disappearing.
- [requestPowerDomainState](./ioservice/api-1810786-requestpowerdomainstate.md)
  Tells a driver to adjust its power state.
- [requestProbe](./ioservice/api-1810804-requestprobe.md)
  Requests that hardware be re-scanned for devices.
- [requestTerminate](./ioservice/api-1810819-requestterminate.md)
  Passes a termination up the stack.
- [resourceMatching(const char *, OSDictionary *)](./ioservice/api-1810840-resourcematching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify a resource service match.
- [resourceMatching(const OSString *, OSDictionary *)](./ioservice/api-1810857-resourcematching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify a resource service match.
- [serviceMatching(const char *, OSDictionary *)](./ioservice/api-1810880-servicematching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify an IOService class match.
- [serviceMatching(const OSString *, OSDictionary *)](./ioservice/api-1810901-servicematching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify an IOService class match.
- [setAggressiveness](./ioservice/api-1810925-setaggressiveness.md)
  Broadcasts an aggressiveness factor from the parent of a driver to the driver.
- [setDeviceMemory](./ioservice/api-1810946-setdevicememory.md)
  Sets the array of IODeviceMemory objects representing a device's memory mapped ranges.
- [setIdleTimerPeriod](./ioservice/api-1810962-setidletimerperiod.md)
  Sets or changes the idle timer period.
- [setPowerParent](./ioservice/api-1810987-setpowerparent.md)
  This call is handled internally by power management. It is not intended to be overridden or called by drivers.
- [- setPowerState](./ioservice/api-1532866-setpowerstate.md)
  Requests a power managed driver to change the power state of its device.
- [start](./ioservice/api-1811009-start.md)
  During an IOService object's instantiation, starts the IOService object that has been selected to run on the provider.
- [start_PM_idle_timer](./ioservice/api-1811024-start_pm_idle_timer.md)
- [stop](./ioservice/api-1811034-stop.md)
  During an IOService termination, the stop method is called in its clients before they are detached & it is destroyed.
- [stringFromReturn](./ioservice/api-1811046-stringfromreturn.md)
  Supplies a programmer-friendly string from an IOReturn code.
- [systemWake](./ioservice/api-1811056-systemwake.md)
  Tells every driver in the power plane that the system is waking up.
- [systemWillShutdown](./ioservice/api-1811071-systemwillshutdown.md)
  Notifies members of the power plane of system shutdown and restart.
- [temperatureCriticalForZone](./ioservice/api-1811087-temperaturecriticalforzone.md)
  Alerts a driver to a critical temperature in some thermal zone.
- [temporaryPowerClampOn](./ioservice/api-1811099-temporarypowerclampon.md)
  A driver calls this method to hold itself in the highest power state until it has children.
- [terminate](./ioservice/api-1811110-terminate.md)
  Makes an IOService object inactive and begins its destruction.
- [terminateClient](./ioservice/api-1811121-terminateclient.md)
  Passes a termination up the stack.
- [unlockForArbitration](./ioservice/api-1811130-unlockforarbitration.md)
  Unlocks an IOService obkect after a successful lockForArbitration.
- [unregisterInterrupt](./ioservice/api-1811142-unregisterinterrupt.md)
  Removes a C function interrupt handler for a device supplying hardware interrupts.
- [updateReport](./ioservice/api-1811152-updatereport.md)
  request current data for the specified channels
- [waitForMatchingService](./ioservice/api-1811164-waitformatchingservice.md)
  Waits for a matching to service to be published.
- [waitForService](./ioservice/api-1811172-waitforservice.md)
  Deprecated use waitForMatchingService(). Waits for a matching to service to be published.
- [waitQuiet](./ioservice/api-1811184-waitquiet.md)
  Waits for an IOService object's `busyState` to be zero.
- [willTerminate](./ioservice/api-1811202-willterminate.md)
  Passes a termination up the stack.
- [youAreRoot](./ioservice/api-1811214-youareroot.md)
  Informs power management which IOService object is the power plane root.
### DataTypes
- [ExpansionData](./ioservice/expansiondata.md)
### Instance Variables
- [reserved](./ioservice/reserved.md)
### Instance Methods
- [- AdjustBusy](./ioservice/api-3753458-adjustbusy.md)
- [- AdjustBusy_Impl](./ioservice/api-3753459-adjustbusy_impl.md)
- [- ChangePowerState](./ioservice/api-3180692-changepowerstate.md)
  Changes the device's power state to the specified level.
- [- ChangePowerState_Impl](./ioservice/api-3152487-changepowerstate_impl.md)
- [- ClientCrashed](./ioservice/api-3727923-clientcrashed.md)
- [- ClientCrashed_Impl](./ioservice/api-3727924-clientcrashed_impl.md)
- [- ConfigureReport](./ioservice/api-3753461-configurereport.md)
- [- ConfigureReport_Impl](./ioservice/api-3753462-configurereport_impl.md)
- [- CopyDispatchQueue_Impl](./ioservice/api-3075032-copydispatchqueue_impl.md)
- [- CopyName](./ioservice/api-3753464-copyname.md)
- [- CopyName_Impl](./ioservice/api-3753465-copyname_impl.md)
- [- CopyProperties](./ioservice/api-3180694-copyproperties.md)
  Returns the registry properties associated with the current service. 
- [- CopyProperties_Impl](./ioservice/api-3180695-copyproperties_impl.md)
- [- CopyProviderProperties](./ioservice/api-3538559-copyproviderproperties.md)
- [- CopyProviderProperties_Impl](./ioservice/api-3538560-copyproviderproperties_impl.md)
- [- CopySystemStateNotificationService](./ioservice/api-3753467-copysystemstatenotificationservi.md)
- [- CopySystemStateNotificationService_Impl](./ioservice/api-3753468-copysystemstatenotificationservi.md)
- [- CoreAnalyticsSendEvent](./ioservice/api-3753470-coreanalyticssendevent.md)
- [- CoreAnalyticsSendEvent_Impl](./ioservice/api-3753471-coreanalyticssendevent_impl.md)
- [- Create](./ioservice/api-3325788-create.md)
- [- CreateDefaultDispatchQueue](./ioservice/api-3753473-createdefaultdispatchqueue.md)
- [- CreateDefaultDispatchQueue_Impl](./ioservice/api-3753474-createdefaultdispatchqueue_impl.md)
- [- Create_Impl](./ioservice/api-3325789-create_impl.md)
- [- Dispatch](./ioservice/api-3180697-dispatch.md)
- [- GetBusyState](./ioservice/api-3753476-getbusystate.md)
- [- GetBusyState_Impl](./ioservice/api-3753477-getbusystate_impl.md)
- [- GetProvider](./ioservice/api-3753479-getprovider.md)
- [- GetRegistryEntryID](./ioservice/api-3180698-getregistryentryid.md)
  Returns the registry ID for the current service. 
- [- GetRegistryEntryID_Impl](./ioservice/api-3180699-getregistryentryid_impl.md)
- [- JoinPMTree](./ioservice/api-4061663-joinpmtree.md)
- [- JoinPMTree_Impl](./ioservice/api-4061664-joinpmtree_impl.md)
- [- NewUserClient](./ioservice/api-3325791-newuserclient.md)
- [- NewUserClient_Impl](./ioservice/api-3325792-newuserclient_impl.md)
- [- PMinit](./ioservice/api-1532776-pminit.md)
- [- PMstop](./ioservice/api-1532667-pmstop.md)
- [- RegisterService](./ioservice/api-3180701-registerservice.md)
  Starts the registration process for the service and performs any additional matching.
- [- RegisterService_Impl](./ioservice/api-3075044-registerservice_impl.md)
- [- RemoveProperty](./ioservice/api-3753480-removeproperty.md)
- [- RemoveProperty_Impl](./ioservice/api-3753481-removeproperty_impl.md)
- [- RequireMaxBusStall](./ioservice/api-3689549-requiremaxbusstall.md)
- [- RequireMaxBusStall_Impl](./ioservice/api-3689550-requiremaxbusstall_impl.md)
- [- SearchProperty](./ioservice/api-3325794-searchproperty.md)
- [- SearchProperty_Impl](./ioservice/api-3325795-searchproperty_impl.md)
- [- SendIOMessageServicePropertyChange](./ioservice/api-3943382-sendiomessageservicepropertychan.md)
- [- SendIOMessageServicePropertyChange_Impl](./ioservice/api-3943383-sendiomessageservicepropertychan.md)
- [- SetDispatchQueue_Impl](./ioservice/api-3180703-setdispatchqueue_impl.md)
- [- SetLegend](./ioservice/api-3753483-setlegend.md)
- [- SetLegend_Impl](./ioservice/api-3753484-setlegend_impl.md)
- [- SetName](./ioservice/api-3325797-setname.md)
- [- SetName_Impl](./ioservice/api-3325798-setname_impl.md)
- [- SetPowerOverride](./ioservice/api-4485635-setpoweroverride.md)
- [- SetPowerOverride_Impl](./ioservice/api-4485636-setpoweroverride_impl.md)
- [- SetPowerState](./ioservice/api-3180704-setpowerstate.md)
  Updates the service in response to power-related changes for a provider.
- [- SetPowerState_Impl](./ioservice/api-3180705-setpowerstate_impl.md)
- [- SetProperties](./ioservice/api-3075047-setproperties.md)
- [- SetProperties_Impl](./ioservice/api-3075048-setproperties_impl.md)
- [- Start](./ioservice/api-3180710-start.md)
  Starts the current service and associates it with the specified provider.  
- [- Start_Impl](./ioservice/api-3180711-start_impl.md)
- [- StateNotificationItemCopy](./ioservice/api-3753486-statenotificationitemcopy.md)
- [- StateNotificationItemCopy_Impl](./ioservice/api-3753487-statenotificationitemcopy_impl.md)
- [- StateNotificationItemCreate](./ioservice/api-3753489-statenotificationitemcreate.md)
- [- StateNotificationItemCreate_Impl](./ioservice/api-3753490-statenotificationitemcreate_impl.md)
- [- StateNotificationItemSet](./ioservice/api-3753492-statenotificationitemset.md)
- [- StateNotificationItemSet_Impl](./ioservice/api-3753493-statenotificationitemset_impl.md)
- [- Stop](./ioservice/api-3180713-stop.md)
  Stops the service associated with the specified provider. 
- [- Stop_Impl](./ioservice/api-3180714-stop_impl.md)
- [- Stop_async](./ioservice/api-3684894-stop_async.md)
- [- Stop_async_Impl](./ioservice/api-3684895-stop_async_impl.md)
- [- StringFromReturn](./ioservice/api-3753495-stringfromreturn.md)
- [- StringFromReturn](./ioservice/api-3943385-stringfromreturn.md)
- [- StringFromReturn_Impl](./ioservice/api-3753496-stringfromreturn_impl.md)
- [- Terminate](./ioservice/api-3538570-terminate.md)
- [- Terminate_Impl](./ioservice/api-3538571-terminate_impl.md)
- [- UpdateReport](./ioservice/api-3753498-updatereport.md)
- [- UpdateReport_Impl](./ioservice/api-3753499-updatereport_impl.md)
- [- UserSetProperties](./ioservice/api-3753501-usersetproperties.md)
- [- UserSetProperties_Impl](./ioservice/api-3753502-usersetproperties_impl.md)
- [- acknowledgeNotification](./ioservice/api-1532615-acknowledgenotification.md)
- [- acknowledgePowerChange](./ioservice/api-1532614-acknowledgepowerchange.md)
- [- activityTickle](./ioservice/api-1532877-activitytickle.md)
- [- addInterruptStatistics](./ioservice/api-1532794-addinterruptstatistics.md)
- [- addNeededResource](./ioservice/api-1532799-addneededresource.md)
- [- addPowerChild](./ioservice/api-1532771-addpowerchild.md)
- [- adjustBusy](./ioservice/api-1532718-adjustbusy.md)
- [- allowPowerChange](./ioservice/api-1532563-allowpowerchange.md)
- [- applyToClients](./ioservice/api-1532705-applytoclients.md)
- [- applyToClients](./ioservice/api-3567140-applytoclients.md)
- [- applyToInterested](./ioservice/api-1532867-applytointerested.md)
- [- applyToProviders](./ioservice/api-1532775-applytoproviders.md)
- [- applyToProviders](./ioservice/api-3567141-applytoproviders.md)
- [- askChangeDown](./ioservice/api-1532647-askchangedown.md)
- [- attach](./ioservice/api-1532842-attach.md)
- [- callPlatformFunction](./ioservice/api-1532716-callplatformfunction.md)
- [- callPlatformFunction](./ioservice/api-3516483-callplatformfunction.md)
- [- canTerminateForReplacement](./ioservice/api-3857674-canterminateforreplacement.md)
- [- cancelPowerChange](./ioservice/api-1532580-cancelpowerchange.md)
- [- causeInterrupt](./ioservice/api-1532818-causeinterrupt.md)
- [- changePowerStateTo](./ioservice/api-1532683-changepowerstateto.md)
- [- changePowerStateToPriv](./ioservice/api-1532812-changepowerstatetopriv.md)
- [- checkResource](./ioservice/api-1532783-checkresource.md)
- [- checkResources](./ioservice/api-1532599-checkresources.md)
- [- close](./ioservice/api-1532865-close.md)
- [- compareProperties](./ioservice/api-1532808-compareproperties.md)
- [- compareProperty](./ioservice/api-1532873-compareproperty.md)
- [- compareProperty](./ioservice/api-3516484-compareproperty.md)
- [- configureReport](./ioservice/api-1532713-configurereport.md)
- [- copyClientWithCategory](./ioservice/api-1532583-copyclientwithcategory.md)
- [- copyNotifiers](./ioservice/api-2870324-copynotifiers.md)
- [- currentCapability](./ioservice/api-1532694-currentcapability.md)
- [- currentPowerConsumption](./ioservice/api-1532862-currentpowerconsumption.md)
- [- deRegisterInterestedDriver](./ioservice/api-1532853-deregisterinteresteddriver.md)
- [- deliverNotification](./ioservice/api-1532765-delivernotification.md)
- [- detach](./ioservice/api-1532594-detach.md)
- [- didTerminate](./ioservice/api-1532715-didterminate.md)
- [- disableInterrupt](./ioservice/api-1532634-disableinterrupt.md)
- [- doServiceMatch](./ioservice/api-1532795-doservicematch.md)
- [- doServiceTerminate](./ioservice/api-1532573-doserviceterminate.md)
- [- enableInterrupt](./ioservice/api-1532864-enableinterrupt.md)
- [- errnoFromReturn](./ioservice/api-1532706-errnofromreturn.md)
- [- finalize](./ioservice/api-1532659-finalize.md)
- [- free](./ioservice/api-3180716-free.md)
  Performs any final cleanup for the service.
- [- getAggressiveness](./ioservice/api-1532725-getaggressiveness.md)
- [- getBusyState](./ioservice/api-1532698-getbusystate.md)
- [- getClient](./ioservice/api-1532758-getclient.md)
- [- getClientIterator](./ioservice/api-1532748-getclientiterator.md)
- [- getClientWithCategory](./ioservice/api-1532672-getclientwithcategory.md)
- [- getDeviceMemory](./ioservice/api-1532588-getdevicememory.md)
- [- getDeviceMemoryCount](./ioservice/api-1532745-getdevicememorycount.md)
- [- getDeviceMemoryWithIndex](./ioservice/api-1532861-getdevicememorywithindex.md)
- [- getInterruptType](./ioservice/api-1532557-getinterrupttype.md)
- [- getMetaClass](./ioservice/api-1532719-getmetaclass.md)
- [- getOpenClientIterator](./ioservice/api-1532757-getopenclientiterator.md)
- [- getOpenProviderIterator](./ioservice/api-1532590-getopenprovideriterator.md)
- [- getPowerState](./ioservice/api-1532710-getpowerstate.md)
- [- getProvider](./ioservice/api-1532585-getprovider.md)
- [- getProviderIterator](./ioservice/api-1532627-getprovideriterator.md)
- [- getResources](./ioservice/api-1532807-getresources.md)
- [- getState](./ioservice/api-1532791-getstate.md)
- [- getWorkLoop](./ioservice/api-1532780-getworkloop.md)
- [- handleClose](./ioservice/api-1532838-handleclose.md)
- [- handleIsOpen](./ioservice/api-1532682-handleisopen.md)
- [- handleOpen](./ioservice/api-1532701-handleopen.md)
- [- hasParent](./ioservice/api-3857675-hasparent.md)
- [- init](./ioservice/api-1532700-init.md)
- [- init](./ioservice/api-3180717-init.md)
  Handles the basic initialization of the service.
- [- initialPowerStateForDomainState](./ioservice/api-1532851-initialpowerstatefordomainstate.md)
- [- invokeNotifier](./ioservice/api-2870327-invokenotifier.md)
- [- invokeNotifiers](./ioservice/api-2870325-invokenotifiers.md)
- [- isInactive](./ioservice/api-1532870-isinactive.md)
- [- isOpen](./ioservice/api-1532598-isopen.md)
- [- joinPMtree](./ioservice/api-1532587-joinpmtree.md)
- [- lockForArbitration](./ioservice/api-1532692-lockforarbitration.md)
- [- lookupInterrupt](./ioservice/api-1532726-lookupinterrupt.md)
- [- makeUsable](./ioservice/api-1532872-makeusable.md)
- [- mapDeviceMemoryWithIndex](./ioservice/api-1532762-mapdevicememorywithindex.md)
- [- matchInternal](./ioservice/api-1532714-matchinternal.md)
- [- matchLocation](./ioservice/api-1532803-matchlocation.md)
- [- matchPassive](./ioservice/api-1532642-matchpassive.md)
- [- matchPropertyTable](./ioservice/api-1532892-matchpropertytable.md)
- [- matchPropertyTable](./ioservice/api-3516485-matchpropertytable.md)
- [- maxCapabilityForDomainState](./ioservice/api-1532813-maxcapabilityfordomainstate.md)
- [- message](./ioservice/api-1532558-message.md)
- [- messageClient](./ioservice/api-1532884-messageclient.md)
- [- messageClients](./ioservice/api-1532646-messageclients.md)
- [- newUserClient](./ioservice/api-1532702-newuserclient.md)
- [- newUserClient](./ioservice/api-3516487-newuserclient.md)
- [- newUserClient](./ioservice/api-3553375-newuserclient.md)
- [- newUserClient](./ioservice/api-3553376-newuserclient.md)
- [- nextIdleTimeout](./ioservice/api-1532675-nextidletimeout.md)
- [- open](./ioservice/api-1532575-open.md)
- [- passiveMatch](./ioservice/api-1532787-passivematch.md)
- [- powerChangeDone](./ioservice/api-1532685-powerchangedone.md)
- [- powerOverrideOffPriv](./ioservice/api-1532855-poweroverrideoffpriv.md)
- [- powerOverrideOnPriv](./ioservice/api-1532639-poweroverrideonpriv.md)
- [- powerStateDidChangeTo](./ioservice/api-1532891-powerstatedidchangeto.md)
- [- powerStateForDomainState](./ioservice/api-1532649-powerstatefordomainstate.md)
- [- powerStateWillChangeTo](./ioservice/api-1532889-powerstatewillchangeto.md)
- [- probe](./ioservice/api-1532835-probe.md)
- [- probeCandidates](./ioservice/api-1532781-probecandidates.md)
- [- registerInterest](./ioservice/api-1532612-registerinterest.md)
- [- registerInterest](./ioservice/api-3516489-registerinterest.md)
- [- registerInterestedDriver](./ioservice/api-1532847-registerinteresteddriver.md)
- [- registerInterrupt](./ioservice/api-1532830-registerinterrupt.md)
- [- registerInterruptBlock](./ioservice/api-2967276-registerinterruptblock.md)
- [- registerPowerDriver](./ioservice/api-1532665-registerpowerdriver.md)
- [- registerService](./ioservice/api-1532797-registerservice.md)
- [- removeInterruptStatistics](./ioservice/api-1532663-removeinterruptstatistics.md)
- [- removePowerChild](./ioservice/api-1532779-removepowerchild.md)
- [- requestPowerDomainState](./ioservice/api-1532751-requestpowerdomainstate.md)
- [- requestProbe](./ioservice/api-1532789-requestprobe.md)
- [- requestTerminate](./ioservice/api-1532728-requestterminate.md)
- [- requireMaxBusStall](./ioservice/api-1532887-requiremaxbusstall.md)
- [- requireMaxInterruptDelay](./ioservice/api-1532798-requiremaxinterruptdelay.md)
- [- resolveInterrupt](./ioservice/api-1532677-resolveinterrupt.md)
- [- scheduleStop](./ioservice/api-1532571-schedulestop.md)
- [- scheduleTerminatePhase2](./ioservice/api-1532641-scheduleterminatephase2.md)
- [- serializeProperties](./ioservice/api-1532823-serializeproperties.md)
- [- setAggressiveness](./ioservice/api-1532679-setaggressiveness.md)
- [- setDeviceMemory](./ioservice/api-1532699-setdevicememory.md)
- [- setIdleTimerPeriod](./ioservice/api-1532753-setidletimerperiod.md)
- [- start](./ioservice/api-1532606-start.md)
- [- startCandidate](./ioservice/api-1532735-startcandidate.md)
- [- startMatching](./ioservice/api-1532845-startmatching.md)
- [- start_PM_idle_timer](./ioservice/api-1532669-start_pm_idle_timer.md)
- [- stop](./ioservice/api-1532568-stop.md)
- [- stringFromReturn](./ioservice/api-1532752-stringfromreturn.md)
- [- systemWillShutdown](./ioservice/api-1532569-systemwillshutdown.md)
- [- tellChangeDown](./ioservice/api-1532643-tellchangedown.md)
- [- tellChangeUp](./ioservice/api-1532625-tellchangeup.md)
- [- tellNoChangeDown](./ioservice/api-1532656-tellnochangedown.md)
- [- temporaryPowerClampOn](./ioservice/api-1532592-temporarypowerclampon.md)
- [- terminate](./ioservice/api-1532674-terminate.md)
- [- terminateClient](./ioservice/api-1532730-terminateclient.md)
- [- terminatePhase1](./ioservice/api-1532849-terminatephase1.md)
- [- unlockForArbitration](./ioservice/api-1532561-unlockforarbitration.md)
- [- unregisterAllInterest](./ioservice/api-1532882-unregisterallinterest.md)
- [- unregisterAllInterrupts](./ioservice/api-4445089-unregisterallinterrupts.md)
- [- unregisterInterrupt](./ioservice/api-1532856-unregisterinterrupt.md)
- [- updateReport](./ioservice/api-1532767-updatereport.md)
- [- waitForState](./ioservice/api-1532770-waitforstate.md)
- [- waitForState](./ioservice/api-3516492-waitforstate.md)
- [- waitQuiet](./ioservice/api-1532773-waitquiet.md)
- [- waitQuiet](./ioservice/api-3516493-waitquiet.md)
- [- willTerminate](./ioservice/api-1532846-willterminate.md)
### Type Methods
- [+ AdjustBusy_Invoke](./ioservice/api-3753460-adjustbusy_invoke.md)
- [+ ChangePowerState_Invoke](./ioservice/api-3152488-changepowerstate_invoke.md)
- [+ ClientCrashed_Invoke](./ioservice/api-3727925-clientcrashed_invoke.md)
- [+ ConfigureReport_Invoke](./ioservice/api-3753463-configurereport_invoke.md)
- [+ CopyName_Invoke](./ioservice/api-3753466-copyname_invoke.md)
- [+ CopyProperties_Invoke](./ioservice/api-3075035-copyproperties_invoke.md)
- [+ CopyProviderProperties_Invoke](./ioservice/api-3538561-copyproviderproperties_invoke.md)
- [+ CopySystemStateNotificationService_Invoke](./ioservice/api-3753469-copysystemstatenotificationservi.md)
- [+ CoreAnalyticsSendEvent_Invoke](./ioservice/api-3753472-coreanalyticssendevent_invoke.md)
- [+ CreateDefaultDispatchQueue_Invoke](./ioservice/api-3753475-createdefaultdispatchqueue_invok.md)
- [+ CreateKernelClassMatchingDictionary](./ioservice/api-3538562-createkernelclassmatchingdiction.md)
- [+ CreateKernelClassMatchingDictionary](./ioservice/api-3538563-createkernelclassmatchingdiction.md)
- [+ CreateNameMatchingDictionary](./ioservice/api-3538564-createnamematchingdictionary.md)
- [+ CreateNameMatchingDictionary](./ioservice/api-3538565-createnamematchingdictionary.md)
- [+ CreatePropertyMatchingDictionary](./ioservice/api-3538566-createpropertymatchingdictionary.md)
- [+ CreatePropertyMatchingDictionary](./ioservice/api-3538567-createpropertymatchingdictionary.md)
- [+ CreateUserClassMatchingDictionary](./ioservice/api-3538568-createuserclassmatchingdictionar.md)
- [+ CreateUserClassMatchingDictionary](./ioservice/api-3538569-createuserclassmatchingdictionar.md)
- [+ Create_Invoke](./ioservice/api-3325790-create_invoke.md)
- [+ GetBusyState_Invoke](./ioservice/api-3753478-getbusystate_invoke.md)
- [+ GetRegistryEntryID_Invoke](./ioservice/api-3075041-getregistryentryid_invoke.md)
- [+ JoinPMTree_Invoke](./ioservice/api-4061665-joinpmtree_invoke.md)
- [+ NewUserClient_Invoke](./ioservice/api-3325793-newuserclient_invoke.md)
- [+ RegisterService_Invoke](./ioservice/api-3075045-registerservice_invoke.md)
- [+ RemoveProperty_Invoke](./ioservice/api-3753482-removeproperty_invoke.md)
- [+ RequireMaxBusStall_Invoke](./ioservice/api-3689551-requiremaxbusstall_invoke.md)
- [+ SearchProperty_Invoke](./ioservice/api-3325796-searchproperty_invoke.md)
- [+ SendIOMessageServicePropertyChange_Invoke](./ioservice/api-3943384-sendiomessageservicepropertychan.md)
- [+ SetLegend_Invoke](./ioservice/api-3753485-setlegend_invoke.md)
- [+ SetName_Invoke](./ioservice/api-3325799-setname_invoke.md)
- [+ SetPowerOverride_Invoke](./ioservice/api-4485637-setpoweroverride_invoke.md)
- [+ SetPowerState_Invoke](./ioservice/api-3152491-setpowerstate_invoke.md)
- [+ SetProperties_Invoke](./ioservice/api-3075049-setproperties_invoke.md)
- [+ Start_Invoke](./ioservice/api-3075052-start_invoke.md)
- [+ StateNotificationItemCopy_Invoke](./ioservice/api-3753488-statenotificationitemcopy_invoke.md)
- [+ StateNotificationItemCreate_Invoke](./ioservice/api-3753491-statenotificationitemcreate_invo.md)
- [+ StateNotificationItemSet_Invoke](./ioservice/api-3753494-statenotificationitemset_invoke.md)
- [+ Stop_Invoke](./ioservice/api-3075055-stop_invoke.md)
- [+ Stop_async_Invoke](./ioservice/api-3684896-stop_async_invoke.md)
- [+ StringFromReturn_Invoke](./ioservice/api-3753497-stringfromreturn_invoke.md)
- [+ Terminate_Invoke](./ioservice/api-3538572-terminate_invoke.md)
- [+ UpdateReport_Invoke](./ioservice/api-3753500-updatereport_invoke.md)
- [+ UserSetProperties_Invoke](./ioservice/api-3753503-usersetproperties_invoke.md)
- [+ actionDidStop](./ioservice/api-1532805-actiondidstop.md)
- [+ actionDidTerminate](./ioservice/api-1532611-actiondidterminate.md)
- [+ actionFinalize](./ioservice/api-1532875-actionfinalize.md)
- [+ actionStop](./ioservice/api-1532839-actionstop.md)
- [+ actionWillStop](./ioservice/api-1532676-actionwillstop.md)
- [+ actionWillTerminate](./ioservice/api-1532651-actionwillterminate.md)
- [+ addLocation](./ioservice/api-1532786-addlocation.md)
- [+ addMatchingNotification](./ioservice/api-1532878-addmatchingnotification.md)
- [+ addMatchingNotification](./ioservice/api-3516482-addmatchingnotification.md)
- [+ addNotification](./ioservice/api-1532881-addnotification.md)
- [+ copyExistingServices](./ioservice/api-1532695-copyexistingservices.md)
- [+ copyMatchingService](./ioservice/api-1532874-copymatchingservice.md)
- [+ doInstallNotification](./ioservice/api-1532603-doinstallnotification.md)
- [+ getMatchingServices](./ioservice/api-1532708-getmatchingservices.md)
- [+ getPMRootDomain](./ioservice/api-1532815-getpmrootdomain.md)
- [+ getPlatform](./ioservice/api-1532696-getplatform.md)
- [+ getResourceService](./ioservice/api-1532617-getresourceservice.md)
- [+ getServiceRoot](./ioservice/api-1532741-getserviceroot.md)
- [+ getSystemStateNotificationService](./ioservice/api-3753504-getsystemstatenotificationservic.md)
- [+ instanceMatch](./ioservice/api-1532586-instancematch.md)
- [+ nameMatching](./ioservice/api-1532678-namematching.md)
- [+ nameMatching](./ioservice/api-3516486-namematching.md)
- [+ propertyMatching](./ioservice/api-1532859-propertymatching.md)
- [+ publishHiddenMedia](./ioservice/api-3857676-publishhiddenmedia.md)
- [+ publishHiddenMediaApplier](./ioservice/api-3857677-publishhiddenmediaapplier.md)
- [+ publishResource](./ioservice/api-1532848-publishresource.md)
- [+ publishResource](./ioservice/api-3516488-publishresource.md)
- [+ publishUserResource](./ioservice/api-3192003-publishuserresource.md)
- [+ registryEntryIDMatching](./ioservice/api-1532608-registryentryidmatching.md)
- [+ resourceMatching](./ioservice/api-1532747-resourcematching.md)
- [+ resourceMatching](./ioservice/api-3516490-resourcematching.md)
- [+ serviceMatching](./ioservice/api-1532788-servicematching.md)
- [+ serviceMatching](./ioservice/api-3516491-servicematching.md)
- [+ setNotification](./ioservice/api-1532577-setnotification.md)
- [+ setRootMedia](./ioservice/api-3857678-setrootmedia.md)
- [+ syncNotificationHandler](./ioservice/api-1532755-syncnotificationhandler.md)
- [+ terminateThread](./ioservice/api-1532810-terminatethread.md)
- [+ terminateWorker](./ioservice/api-1532833-terminateworker.md)
- [+ userServerCheckInTokenCancellationHandler](./ioservice/api-3786074-userservercheckintokencancellati.md)
- [+ waitForMatchingService](./ioservice/api-1532633-waitformatchingservice.md)
- [+ waitForService](./ioservice/api-1532827-waitforservice.md)
- [+ waitToBecomeTerminateThread](./ioservice/api-2935674-waittobecometerminatethread.md)

## Relationships

### Inherits From
- [IORegistryEntry](./ioregistryentry.md)

## See Also

### Driver Services
- [IOPlatformIO](./ioplatformio.md)
  The base class for platform I/O drivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservice)*