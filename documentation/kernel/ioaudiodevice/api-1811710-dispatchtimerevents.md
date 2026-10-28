# dispatchTimerEvents

**Framework**: Kernel  
**Kind**: instm

Called by timerFired() to cause the timer event callbacks to be called.

## Declaration

```cpp
virtual void dispatchTimerEvents(
 boolforce);
```

## Overview

This method iterates through all of the timer event targets and calls the callback on each. Unless the force flag is set to true, the timer events will only be dispatched if the power state is not kIOAudioDeviceSleep. This prevents unexpected timer firings while making wake->sleep->wake transitions. This function must be called on the IOWorkLoop.

## Parameters

- `force`: A bool param to allow the timer events to be dispatched even if the device is in the kIOAudioDeviceSleep power state.

## See Also

### Miscellaneous
- [activateAudioEngine(IOAudioEngine *)](./api-1811648-activateaudioengine.md)
  This simply calls activateAudioEngine(IOAudioEngine *audioEngine, bool shouldStartAudioEngine) with a value of true for shouldStartAudioEngine.
- [activateAudioEngine(IOAudioEngine *, bool)](./api-1811655-activateaudioengine.md)
  This is called to add a new IOAudioEngine object to the IOAudioDevice.
- [addTimerEvent](./api-1811662-addtimerevent.md)
  Adds a TimerEvent callback for the given target called at least as often as specified in interval.
- [attachAudioPort](./api-1811666-attachaudioport.md)
  Adds the port to the IOAudioDevice's list of ports and attaches the port to its parent and attaches the child to the port.
- [audioEngineStarting](./api-1811673-audioenginestarting.md)
  Called by IOAudioEngine when it is starting up
- [audioEngineStopped](./api-1811679-audioenginestopped.md)
  Called by IOAudioEngine when it has stopped
- [completePowerStateChange](./api-1811685-completepowerstatechange.md)
  Called when a power state change is complete
- [completePowerStateChangeAction](./api-1811692-completepowerstatechangeaction.md)
  IOCommandGate Action which calls protectedCompletePowerStateChange() while holding the IOCommandGate.
- [deactivateAllAudioEngines](./api-1811697-deactivateallaudioengines.md)
  Deactivates all of the audio engines in the device.
- [detachAllAudioPorts](./api-1811704-detachallaudioports.md)
  Deactivates all of the ports in the device.
- [flushAudioControls](./api-1811716-flushaudiocontrols.md)
  Forces each IOAudioControl in the driver to have its value flushed out to the hardware. That will cause either the IOAudioControl's ValueChangeHandler to be called.
- [free](./api-1811723-free.md)
  Frees resources used by the IOAudioDevice instance
- [getCommandGate](./api-1811730-getcommandgate.md)
  Returns the IOCommandGate for this IOAudioDevice
- [getPendingPowerState](./api-1811740-getpendingpowerstate.md)
  Returns the pending power state if a state change is in progress. Otherwise it returns the current power state change.
- [getPowerState](./api-1811749-getpowerstate.md)
  Returns the current power state (the old power state if a change is in progress).
- [getWorkLoop](./api-1811757-getworkloop.md)
  Returns the IOWorkLoop for the driver
- [init](./api-1811765-init.md)
  Initialize a newly created instance of IOAudioDevice.
- [initHardware](./api-1811773-inithardware.md)
  This function is called by start() to provide a convenient place for the subclass to perform its initialization.
- [initiatePowerStateChange](./api-1811782-initiatepowerstatechange.md)
  Called internally to execute a power state change
- [performPowerStateChange](./api-1811791-performpowerstatechange.md)
  This function is called by the IOAudioDevice when a power state change is needed.
- [protectedCompletePowerStateChange](./api-1811798-protectedcompletepowerstatechang.md)
  Called on the IOWorkLoop when a power state change is complete.
- [protectedSetPowerState](./api-1811807-protectedsetpowerstate.md)
  Called by setPowerStateAction() to deal with a power state change from the IOService power management facility.
- [removeAllTimerEvents](./api-1811813-removealltimerevents.md)
  Removes all timer events and stops the timer
- [removeTimerEvent](./api-1811823-removetimerevent.md)
  Removes the timer event for the given target.
- [setConfigurationApplicationBundle](./api-1811829-setconfigurationapplicationbundl.md)
  This function is to be called if an external configuration application is available to set which application to launch.
- [setDeviceCanBeDefault](./api-1811833-setdevicecanbedefault.md)
  This function is to be called to tell CoreAudio if this device shouldn't be a default device.
- [setDeviceName](./api-1811841-setdevicename.md)
  Sets the name of the device
- [setDeviceShortName](./api-1811844-setdeviceshortname.md)
  Sets the short name of the device
- [setFamilyManagePower](./api-1811848-setfamilymanagepower.md)
  Called set whether or not the family should manage the device power throught the IOService power management APIs.
- [setIdleAudioSleepTime](./api-1811852-setidleaudiosleeptime.md)
  This function is to be called by a driver that doesn't want to be told about the audio going idle immediately, but at some point in the future.
- [setManufacturerName](./api-1811862-setmanufacturername.md)
  Sets the manufacturer name of the device
- [setPowerState](./api-1811867-setpowerstate.md)
  Called by the power management system in IOService when the power state of this service needs to change.
- [setPowerStateAction](./api-1811878-setpowerstateaction.md)
  IOCommandGate Action which calls protectedSetPowerState() while holding the IOCommandGate
- [start](./api-1811891-start.md)
  This function is called automatically by the system to tell the driver to start vending services to the rest of the system.
- [stop](./api-1811898-stop.md)
  This is responsible for stopping the device after the system is done with it (or if the device is removed from the system).
- [timerFired](./api-1811908-timerfired.md)
  Internal static function called when the timer fires.
- [waitForPendingPowerStateChange](./api-1811913-waitforpendingpowerstatechange.md)
  Called internally to wait until a pending power state change is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiodevice/1811710-dispatchtimerevents)*