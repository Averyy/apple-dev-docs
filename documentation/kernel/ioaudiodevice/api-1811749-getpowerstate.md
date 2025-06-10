# getPowerState

**Framework**: Kernel  
**Kind**: instm

Returns the current power state (the old power state if a change is in progress).

## Declaration

```swift
virtual IOAudioDevicePowerState getPowerState();
```

#### Return_value

The current power state

## See Also

- [activateAudioEngine(IOAudioEngine *)](ioaudiodevice/1811648-activateaudioengine.md)
  This simply calls activateAudioEngine(IOAudioEngine *audioEngine, bool shouldStartAudioEngine) with a value of true for shouldStartAudioEngine.
- [activateAudioEngine(IOAudioEngine *, bool)](ioaudiodevice/1811655-activateaudioengine.md)
  This is called to add a new IOAudioEngine object to the IOAudioDevice.
- [addTimerEvent](ioaudiodevice/1811662-addtimerevent.md)
  Adds a TimerEvent callback for the given target called at least as often as specified in interval.
- [attachAudioPort](ioaudiodevice/1811666-attachaudioport.md)
  Adds the port to the IOAudioDevice's list of ports and attaches the port to its parent and attaches the child to the port.
- [audioEngineStarting](ioaudiodevice/1811673-audioenginestarting.md)
  Called by IOAudioEngine when it is starting up
- [audioEngineStopped](ioaudiodevice/1811679-audioenginestopped.md)
  Called by IOAudioEngine when it has stopped
- [completePowerStateChange](ioaudiodevice/1811685-completepowerstatechange.md)
  Called when a power state change is complete
- [completePowerStateChangeAction](ioaudiodevice/1811692-completepowerstatechangeaction.md)
  IOCommandGate Action which calls protectedCompletePowerStateChange() while holding the IOCommandGate.
- [deactivateAllAudioEngines](ioaudiodevice/1811697-deactivateallaudioengines.md)
  Deactivates all of the audio engines in the device.
- [detachAllAudioPorts](ioaudiodevice/1811704-detachallaudioports.md)
  Deactivates all of the ports in the device.
- [dispatchTimerEvents](ioaudiodevice/1811710-dispatchtimerevents.md)
  Called by timerFired() to cause the timer event callbacks to be called.
- [flushAudioControls](ioaudiodevice/1811716-flushaudiocontrols.md)
  Forces each IOAudioControl in the driver to have its value flushed out to the hardware. That will cause either the IOAudioControl's ValueChangeHandler to be called.
- [free](ioaudiodevice/1811723-free.md)
  Frees resources used by the IOAudioDevice instance
- [getCommandGate](ioaudiodevice/1811730-getcommandgate.md)
  Returns the IOCommandGate for this IOAudioDevice
- [getPendingPowerState](ioaudiodevice/1811740-getpendingpowerstate.md)
  Returns the pending power state if a state change is in progress. Otherwise it returns the current power state change.
- [getWorkLoop](ioaudiodevice/1811757-getworkloop.md)
  Returns the IOWorkLoop for the driver
- [init](ioaudiodevice/1811765-init.md)
  Initialize a newly created instance of IOAudioDevice.
- [initHardware](ioaudiodevice/1811773-inithardware.md)
  This function is called by start() to provide a convenient place for the subclass to perform its initialization.
- [initiatePowerStateChange](ioaudiodevice/1811782-initiatepowerstatechange.md)
  Called internally to execute a power state change
- [performPowerStateChange](ioaudiodevice/1811791-performpowerstatechange.md)
  This function is called by the IOAudioDevice when a power state change is needed.
- [protectedCompletePowerStateChange](ioaudiodevice/1811798-protectedcompletepowerstatechang.md)
  Called on the IOWorkLoop when a power state change is complete.
- [protectedSetPowerState](ioaudiodevice/1811807-protectedsetpowerstate.md)
  Called by setPowerStateAction() to deal with a power state change from the IOService power management facility.
- [removeAllTimerEvents](ioaudiodevice/1811813-removealltimerevents.md)
  Removes all timer events and stops the timer
- [removeTimerEvent](ioaudiodevice/1811823-removetimerevent.md)
  Removes the timer event for the given target.
- [setConfigurationApplicationBundle](ioaudiodevice/1811829-setconfigurationapplicationbundl.md)
  This function is to be called if an external configuration application is available to set which application to launch.
- [setDeviceCanBeDefault](ioaudiodevice/1811833-setdevicecanbedefault.md)
  This function is to be called to tell CoreAudio if this device shouldn't be a default device.
- [setDeviceName](ioaudiodevice/1811841-setdevicename.md)
  Sets the name of the device
- [setDeviceShortName](ioaudiodevice/1811844-setdeviceshortname.md)
  Sets the short name of the device
- [setFamilyManagePower](ioaudiodevice/1811848-setfamilymanagepower.md)
  Called set whether or not the family should manage the device power throught the IOService power management APIs.
- [setIdleAudioSleepTime](ioaudiodevice/1811852-setidleaudiosleeptime.md)
  This function is to be called by a driver that doesn't want to be told about the audio going idle immediately, but at some point in the future.
- [setManufacturerName](ioaudiodevice/1811862-setmanufacturername.md)
  Sets the manufacturer name of the device
- [setPowerState](ioaudiodevice/1811867-setpowerstate.md)
  Called by the power management system in IOService when the power state of this service needs to change.
- [setPowerStateAction](ioaudiodevice/1811878-setpowerstateaction.md)
  IOCommandGate Action which calls protectedSetPowerState() while holding the IOCommandGate
- [start](ioaudiodevice/1811891-start.md)
  This function is called automatically by the system to tell the driver to start vending services to the rest of the system.
- [stop](ioaudiodevice/1811898-stop.md)
  This is responsible for stopping the device after the system is done with it (or if the device is removed from the system).
- [timerFired](ioaudiodevice/1811908-timerfired.md)
  Internal static function called when the timer fires.
- [waitForPendingPowerStateChange](ioaudiodevice/1811913-waitforpendingpowerstatechange.md)
  Called internally to wait until a pending power state change is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiodevice/1811749-getpowerstate)*