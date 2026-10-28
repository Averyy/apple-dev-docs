# requestPowerDomainState

**Framework**: Kernel  
**Kind**: instm

Tells a driver to adjust its power state.

## Declaration

```cpp
virtual IOReturn requestPowerDomainState( 
 IOPMPowerFlags desiredState, 
 IOPowerConnection *whichChild, 
 unsigned long specificationFlags );
```

## Overview

This call is handled internally by power management. It is not intended to be overridden or called by drivers.

## See Also

### Miscellaneous
- [acknowledgePowerChange](./api-1809710-acknowledgepowerchange.md)
  Acknowledges an in-progress power state change.
- [- acknowledgeSetPowerState](./api-1532596-acknowledgesetpowerstate.md)
  Acknowledges the belated completion of a driver’s setPowerState power state change.
- [activityTickle](./api-1809731-activitytickle.md)
  Informs power management when a power-managed device is in use, so that power management can track when it is idle and adjust its power state accordingly.
- [addLocation](./api-1809740-addlocation.md)
  Adds a location matching property to an existing dictionary.
- [addMatchingNotification](./api-1809749-addmatchingnotification.md)
  Adds a persistant notification handler to be notified of IOService events.
- [addNotification](./api-1809760-addnotification.md)
  Deprecated use addMatchingNotification(). Adds a persistant notification handler to be notified of IOService events.
- [addPowerChild](./api-1809766-addpowerchild.md)
  Informs a driver that it has a new child.
- [adjustBusy](./api-1809776-adjustbusy.md)
  Adjusts the `busyState` of an IOService object.
- [attach](./api-1809786-attach.md)
  Attaches an IOService client to a provider in the I/O Registry.
- [callPlatformFunction](./api-1809795-callplatformfunction.md)
  Calls the platform function with the given name.
- [causeInterrupt](./api-1809803-causeinterrupt.md)
  Causes a device interrupt to occur.
- [changePowerStateTo](./api-1809809-changepowerstateto.md)
  Sets a driver's power state.
- [changePowerStateToPriv](./api-1809819-changepowerstatetopriv.md)
  Tells a driver's superclass to change the power state of its device.
- [clampPowerOn](./api-1809824-clamppoweron.md)
  Deprecated. Do not use.
- [close](./api-1809831-close.md)
  Releases active access to a provider.
- [command_received](./api-1809840-command_received.md)
- [compareProperties](./api-1809848-compareproperties.md)
  Compares a set of properties in a matching dictionary with an IOService object's property table.
- [compareProperty(OSDictionary *, const char *)](./api-1809855-compareproperty.md)
  Compares a property in a matching dictionary with an IOService object's property table.
- [compareProperty(OSDictionary *, const OSString *)](./api-1809861-compareproperty.md)
  Compares a property in a matching dictionary with an IOService object's property table.
- [configureReport](./api-1809870-configurereport.md)
  configure IOReporting channels
- [copyClientWithCategory](./api-1809878-copyclientwithcategory.md)
- [copyMatchingService](./api-1809887-copymatchingservice.md)
  Finds one of the current published IOService objects matching a matching dictionary.
- [currentCapability](./api-1809891-currentcapability.md)
  Finds out the capability of a device's current power state.
- [currentPowerConsumption](./api-1809899-currentpowerconsumption.md)
  Finds out the current power consumption of a device.
- [deRegisterInterestedDriver](./api-1809905-deregisterinteresteddriver.md)
  De-registers power state interest from a previous call to `registerInterestedDriver`.
- [detach](./api-1809913-detach.md)
  Detaches an IOService client from a provider in the I/O Registry.
- [didTerminate](./api-1809918-didterminate.md)
  Passes a termination up the stack.
- [didYouWakeSystem](./api-1809924-didyouwakesystem.md)
  Asks a driver if its device is the one that just woke the system from sleep.
- [disableInterrupt](./api-1809929-disableinterrupt.md)
  Synchronously disables a device interrupt.
- [enableInterrupt](./api-1809937-enableinterrupt.md)
  Enables a device interrupt.
- [errnoFromReturn](./api-1809942-errnofromreturn.md)
  Translates an IOReturn code to a BSD `errno`.
- [finalize](./api-1809948-finalize.md)
  Finalizes the destruction of an IOService object.
- [free](./api-1809960-free.md)
  Frees data structures that were allocated when power management was initialized on this service.
- [getAggressiveness](./api-1809962-getaggressiveness.md)
  Returns the current aggressiveness value for the given type.
- [getBusyState](./api-1809968-getbusystate.md)
  Returns the `busyState` of an IOService object.
- [getClient](./api-1809973-getclient.md)
  Returns an IOService object's primary client.
- [getClientIterator](./api-1809979-getclientiterator.md)
  Returns an iterator over an IOService object's clients.
- [getDeviceMemory](./api-1809984-getdevicememory.md)
  Returns the array of IODeviceMemory objects representing a device's memory mapped ranges.
- [getDeviceMemoryCount](./api-1809990-getdevicememorycount.md)
  Returns a count of the physical memory ranges available for a device.
- [getDeviceMemoryWithIndex](./api-1809999-getdevicememorywithindex.md)
  Returns an instance of IODeviceMemory representing one of a device's memory mapped ranges.
- [getInterruptType](./api-1810004-getinterrupttype.md)
  Returns the type of interrupt used for a device supplying hardware interrupts.
- [getMatchingServices](./api-1810011-getmatchingservices.md)
  Finds the set of current published IOService objects matching a matching dictionary.
- [getOpenClientIterator](./api-1810018-getopenclientiterator.md)
  Returns an iterator over a provider's clients that currently have opened the provider.
- [getOpenProviderIterator](./api-1810027-getopenprovideriterator.md)
  Returns an iterator over an client's providers that are currently opened by the client.
- [getPlatform](./api-1810033-getplatform.md)
  Returns a pointer to the platform expert instance for the computer.
- [getPMRootDomain](./api-1810046-getpmrootdomain.md)
  Returns a pointer to the power management root domain instance for the computer.
- [getPMworkloop](./api-1810059-getpmworkloop.md)
  Returns a pointer to the system-wide power management work loop.
- [getPowerState](./api-1810074-getpowerstate.md)
  Determines a device's power state.
- [getProvider](./api-1810088-getprovider.md)
  Returns an IOService object's primary provider.
- [getProviderIterator](./api-1810097-getprovideriterator.md)
  Returns an iterator over an IOService object's providers.
- [getResources](./api-1810107-getresources.md)
  Allocates any needed resources for a published IOService object before clients attach.
- [getResourceService](./api-1810116-getresourceservice.md)
  Returns a pointer to the IOResources service.
- [getServiceRoot](./api-1810122-getserviceroot.md)
  Returns a pointer to the root of the service plane.
- [getState](./api-1810137-getstate.md)
  Accessor for IOService state bits, not normally needed or used outside IOService.
- [getWorkLoop](./api-1810145-getworkloop.md)
  Returns the current work loop or `provider->getWorkLoop`.
- [handleClose](./api-1810153-handleclose.md)
  Controls the open / close behavior of an IOService object (overrideable by subclasses).
- [handleIsOpen](./api-1810164-handleisopen.md)
  Controls the open / close behavior of an IOService object (overrideable by subclasses).
- [handleOpen](./api-1810174-handleopen.md)
  Controls the open / close behavior of an IOService object (overrideable by subclasses).
- [initialPowerStateForDomainState](./api-1810182-initialpowerstatefordomainstate.md)
  Determines which power state a device is in, given the current power domain state.
- [isInactive](./api-1810198-isinactive.md)
  Checks if the IOService object has been terminated, and is in the process of being destroyed.
- [isOpen](./api-1810209-isopen.md)
  Determines whether a specific, or any, client has an IOService object open.
- [joinPMtree](./api-1810216-joinpmtree.md)
  Joins the driver into the power plane of the I/O Registry.
- [lockForArbitration](./api-1810228-lockforarbitration.md)
  Locks an IOService object against changes in state or ownership.
- [makeUsable](./api-1810246-makeusable.md)
  Requests that a device become usable.
- [mapDeviceMemoryWithIndex](./api-1810261-mapdevicememorywithindex.md)
  Maps a physical range of a device.
- [matchLocation](./api-1810275-matchlocation.md)
  Allows a registered IOService object to direct location matching.
- [matchPropertyTable](./api-1810286-matchpropertytable.md)
  Allows a registered IOService object to implement family specific matching.
- [maxCapabilityForDomainState](./api-1810302-maxcapabilityfordomainstate.md)
  Determines a driver's highest power state possible for a given power domain state.
- [message](./api-1810323-message.md)
  Receives a generic message delivered from an attached provider.
- [messageClient](./api-1810334-messageclient.md)
  Sends a generic message to an attached client.
- [messageClients](./api-1810353-messageclients.md)
  Sends a generic message to all attached clients.
- [nameMatching(const char *, OSDictionary *)](./api-1810365-namematching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify an IOService name match.
- [nameMatching(const OSString *, OSDictionary *)](./api-1810383-namematching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify an IOService name match.
- [newTemperature](./api-1810402-newtemperature.md)
  Tells a power managed driver that the temperature in the thermal zone has changed.
- [newUserClient](./api-1810417-newuserclient.md)
  Creates a connection for a non kernel client.
- [nextIdleTimeout](./api-1810435-nextidletimeout.md)
  Allows subclasses to customize idle power management behavior.
- [open](./api-1810450-open.md)
  Requests active access to a provider.
- [PM_Clamp_Timer_Expired](./api-1810463-pm_clamp_timer_expired.md)
- [PM_idle_timer_expiration](./api-1810474-pm_idle_timer_expiration.md)
- [PMinit](./api-1810486-pminit.md)
  Initializes power management for a driver.
- [PMstop](./api-1810502-pmstop.md)
  Stop power managing the driver.
- [powerChangeDone](./api-1810518-powerchangedone.md)
  Tells a driver when a power state change is complete.
- [powerOverrideOffPriv](./api-1810533-poweroverrideoffpriv.md)
  Allows a driver to disable a power override.
- [powerOverrideOnPriv](./api-1810549-poweroverrideonpriv.md)
  Allows a driver to ignore its children's power management requests and only use changePowerStateToPriv to define its own power state.
- [powerStateDidChangeTo](./api-1810564-powerstatedidchangeto.md)
  Informs interested parties that a device has changed to a different power state.
- [powerStateForDomainState](./api-1810576-powerstatefordomainstate.md)
  Determines what power state the device would be in for a given power domain state.
- [powerStateWillChangeTo](./api-1810597-powerstatewillchangeto.md)
  Informs interested parties that a device is about to change its power state.
- [probe](./api-1810605-probe.md)
  During an IOService object's instantiation, probes a matched service to see if it can be used.
- [propertyMatching](./api-1810622-propertymatching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify an IOService phandle match.
- [publishResource(const char *, OSObject *)](./api-1810642-publishresource.md)
  Uses the resource service to publish a property.
- [publishResource(const OSSymbol *, OSObject *)](./api-1810661-publishresource.md)
  Uses the resource service to publish a property.
- [registerInterestedDriver](./api-1810675-registerinteresteddriver.md)
  Allows an IOService object to register interest in the changing power state of a power-managed IOService object.
- [registerInterrupt](./api-1810691-registerinterrupt.md)
  Registers a C function interrupt handler for a device supplying interrupts.
- [registerPowerDriver](./api-1810706-registerpowerdriver.md)
  Registers a set of power states that the driver supports.
- [registerService](./api-1810726-registerservice.md)
  Starts the registration process for a newly discovered IOService object.
- [registryEntryIDMatching](./api-1810750-registryentryidmatching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify a IORegistryEntryID match.
- [removePowerChild](./api-1810770-removepowerchild.md)
  Informs a power managed driver that one of its power plane childen is disappearing.
- [requestProbe](./api-1810804-requestprobe.md)
  Requests that hardware be re-scanned for devices.
- [requestTerminate](./api-1810819-requestterminate.md)
  Passes a termination up the stack.
- [resourceMatching(const char *, OSDictionary *)](./api-1810840-resourcematching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify a resource service match.
- [resourceMatching(const OSString *, OSDictionary *)](./api-1810857-resourcematching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify a resource service match.
- [serviceMatching(const char *, OSDictionary *)](./api-1810880-servicematching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify an IOService class match.
- [serviceMatching(const OSString *, OSDictionary *)](./api-1810901-servicematching.md)
  Creates a matching dictionary, or adds matching properties to an existing dictionary, that specify an IOService class match.
- [setAggressiveness](./api-1810925-setaggressiveness.md)
  Broadcasts an aggressiveness factor from the parent of a driver to the driver.
- [setDeviceMemory](./api-1810946-setdevicememory.md)
  Sets the array of IODeviceMemory objects representing a device's memory mapped ranges.
- [setIdleTimerPeriod](./api-1810962-setidletimerperiod.md)
  Sets or changes the idle timer period.
- [setPowerParent](./api-1810987-setpowerparent.md)
  This call is handled internally by power management. It is not intended to be overridden or called by drivers.
- [- setPowerState](./api-1532866-setpowerstate.md)
  Requests a power managed driver to change the power state of its device.
- [start](./api-1811009-start.md)
  During an IOService object's instantiation, starts the IOService object that has been selected to run on the provider.
- [start_PM_idle_timer](./api-1811024-start_pm_idle_timer.md)
- [stop](./api-1811034-stop.md)
  During an IOService termination, the stop method is called in its clients before they are detached & it is destroyed.
- [stringFromReturn](./api-1811046-stringfromreturn.md)
  Supplies a programmer-friendly string from an IOReturn code.
- [systemWake](./api-1811056-systemwake.md)
  Tells every driver in the power plane that the system is waking up.
- [systemWillShutdown](./api-1811071-systemwillshutdown.md)
  Notifies members of the power plane of system shutdown and restart.
- [temperatureCriticalForZone](./api-1811087-temperaturecriticalforzone.md)
  Alerts a driver to a critical temperature in some thermal zone.
- [temporaryPowerClampOn](./api-1811099-temporarypowerclampon.md)
  A driver calls this method to hold itself in the highest power state until it has children.
- [terminate](./api-1811110-terminate.md)
  Makes an IOService object inactive and begins its destruction.
- [terminateClient](./api-1811121-terminateclient.md)
  Passes a termination up the stack.
- [unlockForArbitration](./api-1811130-unlockforarbitration.md)
  Unlocks an IOService obkect after a successful lockForArbitration.
- [unregisterInterrupt](./api-1811142-unregisterinterrupt.md)
  Removes a C function interrupt handler for a device supplying hardware interrupts.
- [updateReport](./api-1811152-updatereport.md)
  request current data for the specified channels
- [waitForMatchingService](./api-1811164-waitformatchingservice.md)
  Waits for a matching to service to be published.
- [waitForService](./api-1811172-waitforservice.md)
  Deprecated use waitForMatchingService(). Waits for a matching to service to be published.
- [waitQuiet](./api-1811184-waitquiet.md)
  Waits for an IOService object's `busyState` to be zero.
- [willTerminate](./api-1811202-willterminate.md)
  Passes a termination up the stack.
- [youAreRoot](./api-1811214-youareroot.md)
  Informs power management which IOService object is the power plane root.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservice/1810786-requestpowerdomainstate)*