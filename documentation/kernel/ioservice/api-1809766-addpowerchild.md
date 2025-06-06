# addPowerChild

**Framework**: Kernel  
**Kind**: instm

Informs a driver that it has a new child.

## Declaration

```swift
virtual IOReturn addPowerChild(
 IOService *theChild );
```

#### Overview

The Platform Expert uses this method to call a driver and introduce it to a new child. This call is handled internally by power management. It is not intended to be overridden or called by drivers.

## Parameters

- `theChild`: A pointer to the child IOService object.

## See Also

- [acknowledgePowerChange](ioservice/1809710-acknowledgepowerchange.md)
  Acknowledges an in-progress power state change.
- [- acknowledgeSetPowerState](ioservice/1532596-acknowledgesetpowerstate.md)
  Acknowledges the belated completion of a driver’s setPowerState power state change.
- [activityTickle](ioservice/1809731-activitytickle.md)
  Informs power management when a power-managed device is in use, so that power management can track when it is idle and adjust its power state accordingly.
- [addLocation](ioservice/1809740-addlocation.md)
  Adds a location matching property to an existing dictionary.
- [addMatchingNotification](ioservice/1809749-addmatchingnotification.md)
  Adds a persistant notification handler to be notified of IOService events.
- [addNotification](ioservice/1809760-addnotification.md)
  Deprecated use addMatchingNotification(). Adds a persistant notification handler to be notified of IOService events.
- [adjustBusy](ioservice/1809776-adjustbusy.md)
  Adjusts the `busyState` of an IOService object.
- [attach](ioservice/1809786-attach.md)
  Attaches an IOService client to a provider in the I/O Registry.
- [callPlatformFunction](ioservice/1809795-callplatformfunction.md)
  Calls the platform function with the given name.
- [causeInterrupt](ioservice/1809803-causeinterrupt.md)
  Causes a device interrupt to occur.
- [changePowerStateTo](ioservice/1809809-changepowerstateto.md)
  Sets a driver's power state.
- [changePowerStateToPriv](ioservice/1809819-changepowerstatetopriv.md)
  Tells a driver's superclass to change the power state of its device.
- [clampPowerOn](ioservice/1809824-clamppoweron.md)
  Deprecated. Do not use.
- [close](ioservice/1809831-close.md)
  Releases active access to a provider.
- [command_received](ioservice/1809840-command_received.md)
- [compareProperties](ioservice/1809848-compareproperties.md)
  Compares a set of properties in a matching dictionary with an IOService object's property table.
- [compareProperty(OSDictionary *, const char *)](ioservice/1809855-compareproperty.md)
  Compares a property in a matching dictionary with an IOService object's property table.
- [compareProperty(OSDictionary *, const OSString *)](ioservice/1809861-compareproperty.md)
  Compares a property in a matching dictionary with an IOService object's property table.
- [configureReport](ioservice/1809870-configurereport.md)
  configure IOReporting channels
- [copyClientWithCategory](ioservice/1809878-copyclientwithcategory.md)
- [copyMatchingService](ioservice/1809887-copymatchingservice.md)
  Finds one of the current published IOService objects matching a matching dictionary.
- [currentCapability](ioservice/1809891-currentcapability.md)
  Finds out the capability of a device's current power state.
- [currentPowerConsumption](ioservice/1809899-currentpowerconsumption.md)
  Finds out the current power consumption of a device.
- [deRegisterInterestedDriver](ioservice/1809905-deregisterinteresteddriver.md)
  De-registers power state interest from a previous call to `registerInterestedDriver`.
- [detach](ioservice/1809913-detach.md)
  Detaches an IOService client from a provider in the I/O Registry.
- [didTerminate](ioservice/1809918-didterminate.md)
  Passes a termination up the stack.
- [didYouWakeSystem](ioservice/1809924-didyouwakesystem.md)
  Asks a driver if its device is the one that just woke the system from sleep.
- [disableInterrupt](ioservice/1809929-disableinterrupt.md)
  Synchronously disables a device interrupt.
- [enableInterrupt](ioservice/1809937-enableinterrupt.md)
  Enables a device interrupt.
- [errnoFromReturn](ioservice/1809942-errnofromreturn.md)
  Translates an IOReturn code to a BSD `errno`.
- [finalize](ioservice/1809948-finalize.md)
  Finalizes the destruction of an IOService object.
- [free](ioservice/1809960-free.md)
  Frees data structures that were allocated when power management was initialized on this service.
- [getAggressiveness](ioservice/1809962-getaggressiveness.md)
  Returns the current aggressiveness value for the given type.
- [getBusyState](ioservice/1809968-getbusystate.md)
  Returns the `busyState` of an IOService object.
- [getClient](ioservice/1809973-getclient.md)
  Returns an IOService object's primary client.
- [getClientIterator](ioservice/1809979-getclientiterator.md)
  Returns an iterator over an IOService object's clients.
- [getDeviceMemory](ioservice/1809984-getdevicememory.md)
  Returns the array of IODeviceMemory objects representing a device's memory mapped ranges.
- [getDeviceMemoryCount](ioservice/1809990-getdevicememorycount.md)
  Returns a count of the physical memory ranges available for a device.
- [getDeviceMemoryWithIndex](ioservice/1809999-getdevicememorywithindex.md)
  Returns an instance of IODeviceMemory representing one of a device's memory mapped ranges.
- [getInterruptType](ioservice/1810004-getinterrupttype.md)
  Returns the type of interrupt used for a device supplying hardware interrupts.
- [getMatchingServices](ioservice/1810011-getmatchingservices.md)
  Finds the set of current published IOService objects matching a matching dictionary.
- [getOpenClientIterator](ioservice/1810018-getopenclientiterator.md)
  Returns an iterator over a provider's clients that currently have opened the provider.
- [getOpenProviderIterator](ioservice/1810027-getopenprovideriterator.md)
  Returns an iterator over an client's providers that are currently opened by the client.
- [getPlatform](ioservice/1810033-getplatform.md)
  Returns a pointer to the platform expert instance for the computer.
- [getPMRootDomain](ioservice/1810046-getpmrootdomain.md)
  Returns a pointer to the power management root domain instance for the computer.
- [getPMworkloop](ioservice/1810059-getpmworkloop.md)
  Returns a pointer to the system-wide power management work loop.
- [getPowerState](ioservice/1810074-getpowerstate.md)
  Determines a device's power state.
- [getProvider](ioservice/1810088-getprovider.md)
  Returns an IOService object's primary provider.
- [getProviderIterator](ioservice/1810097-getprovideriterator.md)
  Returns an iterator over an IOService object's providers.
- [getResources](ioservice/1810107-getresources.md)
  Allocates any needed resources for a published IOService object before clients attach.
- [getResourceService](ioservice/1810116-getresourceservice.md)
  Returns a pointer to the IOResources service.
- [getServiceRoot](ioservice/1810122-getserviceroot.md)
  Returns a pointer to the root of the service plane.
- [getState](ioservice/1810137-getstate.md)
  Accessor for IOService state bits, not normally needed or used outside IOService.
- [getWorkLoop](ioservice/1810145-getworkloop.md)
  Returns the current work loop or `provider->getWorkLoop`.
- [handleClose](ioservice/1810153-handleclose.md)
  Controls the open / close behavior of an IOService object (overrideable by subclasses).
- [handleIsOpen](ioservice/1810164-handleisopen.md)
  Controls the open / close behavior of an IOService object (overrideable by subclasses).
- [handleOpen](ioservice/1810174-handleopen.md)
  Controls the open / close behavior of an IOService object (overrideable by subclasses).
- [initialPowerStateForDomainState](ioservice/1810182-initialpowerstatefordomainstate.md)
  Determines which power state a device is in, given the current power domain state.
- [isInactive](ioservice/1810198-isinactive.md)
  Checks if the IOService object has been terminated, and is in the process of being destroyed.
- [isOpen](ioservice/1810209-isopen.md)
  Determines whether a specific, or any, client has an IOService object open.
- [joinPMtree](ioservice/1810216-joinpmtree.md)
  Joins the driver into the power plane of the I/O Registry.
- [lockForArbitration](ioservice/1810228-lockforarbitration.md)
  Locks an IOService object against changes in state or ownership.
- [makeUsable](ioservice/1810246-makeusable.md)
  Requests that a device become usable.
- [mapDeviceMemoryWithIndex](ioservice/1810261-mapdevicememorywithindex.md)
  Maps a physical range of a device.
- [matchLocation](ioservice/1810275-matchlocation.md)
  Allows a registered IOService object to direct location matching.
- [matchPropertyTable](ioservice/1810286-matchpropertytable.md)
  Allows a registered IOService object to implement family specific matching.
- [maxCapabilityForDomainState](ioservice/1810302-maxcapabilityfordomainstate.md)
  Determines a driver's highest power state possible for a given power domain state.
- [message](ioservice/1810323-message.md)
  Receives a generic message delivered from an attached provider.
- [messageClient](ioservice/1810334-messageclient.md)
  Sends a generic message to an attached client.
- [messageClients](ioservice/1810353-messageclients.md)
  Sends a generic message to all attached clients.
- [nameMatching(const char *, OSDictionary *)](ioservice/1810365-namematching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify an IOService name match.
- [nameMatching(const OSString *, OSDictionary *)](ioservice/1810383-namematching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify an IOService name match.
- [newTemperature](ioservice/1810402-newtemperature.md)
  Tells a power managed driver that the temperature in the thermal zone has changed.
- [newUserClient](ioservice/1810417-newuserclient.md)
  Creates a connection for a non kernel client.
- [nextIdleTimeout](ioservice/1810435-nextidletimeout.md)
  Allows subclasses to customize idle power management behavior.
- [open](ioservice/1810450-open.md)
  Requests active access to a provider.
- [PM_Clamp_Timer_Expired](ioservice/1810463-pm_clamp_timer_expired.md)
- [PM_idle_timer_expiration](ioservice/1810474-pm_idle_timer_expiration.md)
- [PMinit](ioservice/1810486-pminit.md)
  Initializes power management for a driver.
- [PMstop](ioservice/1810502-pmstop.md)
  Stop power managing the driver.
- [powerChangeDone](ioservice/1810518-powerchangedone.md)
  Tells a driver when a power state change is complete.
- [powerOverrideOffPriv](ioservice/1810533-poweroverrideoffpriv.md)
  Allows a driver to disable a power override.
- [powerOverrideOnPriv](ioservice/1810549-poweroverrideonpriv.md)
  Allows a driver to ignore its children's power management requests and only use changePowerStateToPriv to define its own power state.
- [powerStateDidChangeTo](ioservice/1810564-powerstatedidchangeto.md)
  Informs interested parties that a device has changed to a different power state.
- [powerStateForDomainState](ioservice/1810576-powerstatefordomainstate.md)
  Determines what power state the device would be in for a given power domain state.
- [powerStateWillChangeTo](ioservice/1810597-powerstatewillchangeto.md)
  Informs interested parties that a device is about to change its power state.
- [probe](ioservice/1810605-probe.md)
  During an IOService object's instantiation, probes a matched service to see if it can be used.
- [propertyMatching](ioservice/1810622-propertymatching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify an IOService phandle match.
- [publishResource(const char *, OSObject *)](ioservice/1810642-publishresource.md)
  Uses the resource service to publish a property.
- [publishResource(const OSSymbol *, OSObject *)](ioservice/1810661-publishresource.md)
  Uses the resource service to publish a property.
- [registerInterestedDriver](ioservice/1810675-registerinteresteddriver.md)
  Allows an IOService object to register interest in the changing power state of a power-managed IOService object.
- [registerInterrupt](ioservice/1810691-registerinterrupt.md)
  Registers a C function interrupt handler for a device supplying interrupts.
- [registerPowerDriver](ioservice/1810706-registerpowerdriver.md)
  Registers a set of power states that the driver supports.
- [registerService](ioservice/1810726-registerservice.md)
  Starts the registration process for a newly discovered IOService object.
- [registryEntryIDMatching](ioservice/1810750-registryentryidmatching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify a IORegistryEntryID match.
- [removePowerChild](ioservice/1810770-removepowerchild.md)
  Informs a power managed driver that one of its power plane childen is disappearing.
- [requestPowerDomainState](ioservice/1810786-requestpowerdomainstate.md)
  Tells a driver to adjust its power state.
- [requestProbe](ioservice/1810804-requestprobe.md)
  Requests that hardware be re-scanned for devices.
- [requestTerminate](ioservice/1810819-requestterminate.md)
  Passes a termination up the stack.
- [resourceMatching(const char *, OSDictionary *)](ioservice/1810840-resourcematching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify a resource service match.
- [resourceMatching(const OSString *, OSDictionary *)](ioservice/1810857-resourcematching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify a resource service match.
- [serviceMatching(const char *, OSDictionary *)](ioservice/1810880-servicematching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify an IOService class match.
- [serviceMatching(const OSString *, OSDictionary *)](ioservice/1810901-servicematching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify an IOService class match.
- [setAggressiveness](ioservice/1810925-setaggressiveness.md)
  Broadcasts an aggressiveness factor from the parent of a driver to the driver.
- [setDeviceMemory](ioservice/1810946-setdevicememory.md)
  Sets the array of IODeviceMemory objects representing a device's memory mapped ranges.
- [setIdleTimerPeriod](ioservice/1810962-setidletimerperiod.md)
  Sets or changes the idle timer period.
- [setPowerParent](ioservice/1810987-setpowerparent.md)
  This call is handled internally by power management. It is not intended to be overridden or called by drivers.
- [- setPowerState](ioservice/1532866-setpowerstate.md)
  Requests a power managed driver to change the power state of its device.
- [start](ioservice/1811009-start.md)
  During an IOService object's instantiation, starts the IOService object that has been selected to run on the provider.
- [start_PM_idle_timer](ioservice/1811024-start_pm_idle_timer.md)
- [stop](ioservice/1811034-stop.md)
  During an IOService termination, the stop method is called in its clients before they are detached & it is destroyed.
- [stringFromReturn](ioservice/1811046-stringfromreturn.md)
  Supplies a programmer-friendly string from an IOReturn code.
- [systemWake](ioservice/1811056-systemwake.md)
  Tells every driver in the power plane that the system is waking up.
- [systemWillShutdown](ioservice/1811071-systemwillshutdown.md)
  Notifies members of the power plane of system shutdown and restart.
- [temperatureCriticalForZone](ioservice/1811087-temperaturecriticalforzone.md)
  Alerts a driver to a critical temperature in some thermal zone.
- [temporaryPowerClampOn](ioservice/1811099-temporarypowerclampon.md)
  A driver calls this method to hold itself in the highest power state until it has children.
- [terminate](ioservice/1811110-terminate.md)
  Makes an IOService object inactive and begins its destruction.
- [terminateClient](ioservice/1811121-terminateclient.md)
  Passes a termination up the stack.
- [unlockForArbitration](ioservice/1811130-unlockforarbitration.md)
  Unlocks an IOService obkect after a successful lockForArbitration.
- [unregisterInterrupt](ioservice/1811142-unregisterinterrupt.md)
  Removes a C function interrupt handler for a device supplying hardware interrupts.
- [updateReport](ioservice/1811152-updatereport.md)
  request current data for the specified channels
- [waitForMatchingService](ioservice/1811164-waitformatchingservice.md)
  Waits for a matching to service to be published.
- [waitForService](ioservice/1811172-waitforservice.md)
  Deprecated use waitForMatchingService(). Waits for a matching to service to be published.
- [waitQuiet](ioservice/1811184-waitquiet.md)
  Waits for an IOService object's `busyState` to be zero.
- [willTerminate](ioservice/1811202-willterminate.md)
  Passes a termination up the stack.
- [youAreRoot](ioservice/1811214-youareroot.md)
  Informs power management which IOService object is the power plane root.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservice/1809766-addpowerchild)*