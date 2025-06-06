# IOAudioDevice

**Framework**: Kernel  
**Kind**: cl

Abstract base class for a single piece of audio hardware. The IOAudioDevice provides the central coordination point for an audio driver.

**Availability**:
- macOS 10.1+

## Declaration

```swift
class IOAudioDevice : IOService
```

#### Overview

An audio driver is required to subclass IOAudioDevice in order to provide working audio to the system. A single driver instance will contain a single instance of the driver's IOAudioDevice subclass. The subclass is responsible for mapping all hardware device resources from the service provider nub. It must control access to the hardware so that the hardware doesn't get into an inconsistent state. It is possible that different threads may make requests of the hardware at the same time. The IOAudioDevice superclass provides an IOWorkLoop and IOCommandGate on the IOWorkLoop through which all hardware accesses may be synchronized. All entry points to all parts of the driver controlled by the IOAudioFamily will be synchronized through this one IOWorkLoop.

The IOAudioDevice subclass is responsible for creating the rest of the pieces of the driver. It must identify and create all IOAudioEngines that are not automatically created by the system (i.e. those that are not matched and instantiated by IOKit directly).

The IOAudioDevice subclass must enumerate and create all IOAudioControls to match the device capabilities.

It must also execute control value chages when requested by the system (i.e. volume adjustments).

In order to allow sleep and wake to work on the system, the IOAudioDevice subclass is responsible for performing the necessary actions to sleep and wake its hardware (and restore necessary state on wake).

The IOAudioDevice class provides timer services that allow different elements in the audio driver to receive timer notifications as needed. These services were designed with the idea that most timed events in a typical audio driver need to be done at least as often as a certain interval. Further, it is designed with the idea that being called more often than the specified interval doesn't hurt anything - and in fact may help. With this in mind, the timer services provided by the IOAudioDevice class allow different targets to register for timer callbacks at least as often as the specified interval. The actual interval will be the smallest of the intervals of all of the callbacks. This way, we avoid the overhead of having many timers in a single audio device. As an example, each output IOAudioEngine has a timer to run the erase head. It doesn't hurt to have the erase head run more often. Also, a typical IOAudioDevice subclass may need to run a timer to check for device state changes (e.g. jack insertions).

There are a number of strings passed from the driver to the CoreAudio.framework and then into applications. All of those strings should be localized by the driver. In order to do that the kext bundle should have localized string files following the macOS localization instructions. The IOAudioDevice should contain a property with the name of the bundle/kext that contains the localized string resources. To do that, the driver's personality in the bundle resources could have a property named 'IOAudioDeviceLocalizedBundle' with the path of the bundle/kext relative to '/System/Library/Extensions'. It could also be set by the IOAudioDevice subclass in its initHardware() function. To do so, call setProperty(kIOAudioDeviceLocalizedBundleKey, "Driver.kext").

In a typical driver, the IOAudioDevice subclass will implement initHardware() to perform the hardware initialization and driver construction. Within that initialization it must create at least one IOAudioEngine instance and activate it. In order to activate a new IOAudioEngine activateAudioEngine() should be called for each one. It must create the IOAudioControls matching the hardware capabilities to allow the system to set volume, mute and input selection. To add those controls to the driver, each control should be attached to the IOAudioEngine to which it applies by calling addDefaultAudioControl() on the IOAudioEngine. During initialization it should also call setDeviceName(), setDeviceShortName() and setManufacturerName() with localized strings representing each of the attributes.

If the driver is to work properly after sleep/wake, it must implement performPowerStateChange() and deal with the sleep and wake transitions. It may also deal with the idle state transitions to turn off device power when it isn't in use (especially useful for devices attached to a portable running on battery power).

## Topics

### Miscellaneous
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
- [getPowerState](ioaudiodevice/1811749-getpowerstate.md)
  Returns the current power state (the old power state if a change is in progress).
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
### Callbacks
- [TimerEvent](ioaudiodevice/timerevent.md)
  Generic timer event callback for IOAudioDevice timer targets
### Constants
- [gIOAudioPlane](ioaudiodevice/gioaudioplane.md)
### Instance Variables
- [workLoop](ioaudiodevice/workloop.md)
- [timerEventSource](ioaudiodevice/timereventsource.md)
- [timerEvents](ioaudiodevice/timerevents.md)
  The set of timer events in use by the device.
- [pendingPowerState](ioaudiodevice/pendingpowerstate.md)
- [numRunningAudioEngines](ioaudiodevice/numrunningaudioengines.md)
- [minimumInterval](ioaudiodevice/minimuminterval.md)
- [familyManagePower](ioaudiodevice/familymanagepower.md)
- [duringStartup](ioaudiodevice/duringstartup.md)
- [currentPowerState](ioaudiodevice/currentpowerstate.md)
- [commandGate](ioaudiodevice/commandgate.md)
- [audioPorts](ioaudiodevice/audioports.md)
- [audioEngines](ioaudiodevice/audioengines.md)
- [asyncPowerStateChangeInProgress](ioaudiodevice/asyncpowerstatechangeinprogress.md)
### Instance Methods
- [- activateAudioEngine](ioaudiodevice/1557038-activateaudioengine.md)
- [- activateAudioEngine](ioaudiodevice/3516521-activateaudioengine.md)
- [- addTimerEvent](ioaudiodevice/1557039-addtimerevent.md)
- [- attachAudioPort](ioaudiodevice/1557022-attachaudioport.md)
- [- audioEngineStarting](ioaudiodevice/1557054-audioenginestarting.md)
- [- audioEngineStopped](ioaudiodevice/1557033-audioenginestopped.md)
- [- completePowerStateChange](ioaudiodevice/1557032-completepowerstatechange.md)
- [- deactivateAllAudioEngines](ioaudiodevice/1557057-deactivateallaudioengines.md)
- [- detachAllAudioPorts](ioaudiodevice/1557020-detachallaudioports.md)
- [- dispatchTimerEvents](ioaudiodevice/1557025-dispatchtimerevents.md)
- [- flushAudioControls](ioaudiodevice/1557024-flushaudiocontrols.md)
- [- free](ioaudiodevice/1557026-free.md)
- [- getCommandGate](ioaudiodevice/1557056-getcommandgate.md)
- [- getMetaClass](ioaudiodevice/1557042-getmetaclass.md)
- [- getPendingPowerState](ioaudiodevice/1557015-getpendingpowerstate.md)
- [- getPowerState](ioaudiodevice/1557055-getpowerstate.md)
- [- getWorkLoop](ioaudiodevice/1557016-getworkloop.md)
- [- init](ioaudiodevice/1557036-init.md)
- [- initHardware](ioaudiodevice/1557012-inithardware.md)
- [- initiatePowerStateChange](ioaudiodevice/1557053-initiatepowerstatechange.md)
- [- performPowerStateChange](ioaudiodevice/1557035-performpowerstatechange.md)
- [- protectedCompletePowerStateChange](ioaudiodevice/1557045-protectedcompletepowerstatechang.md)
- [- protectedSetPowerState](ioaudiodevice/1557029-protectedsetpowerstate.md)
- [- removeAllTimerEvents](ioaudiodevice/1557021-removealltimerevents.md)
- [- removeTimerEvent](ioaudiodevice/1557047-removetimerevent.md)
- [- scheduleIdleAudioSleep](ioaudiodevice/1557059-scheduleidleaudiosleep.md)
- [- setAggressiveness](ioaudiodevice/1557048-setaggressiveness.md)
- [- setConfigurationApplicationBundle](ioaudiodevice/1557037-setconfigurationapplicationbundl.md)
- [- setDeviceCanBeDefault](ioaudiodevice/1557030-setdevicecanbedefault.md)
- [- setDeviceModelName](ioaudiodevice/1557034-setdevicemodelname.md)
- [- setDeviceName](ioaudiodevice/1557041-setdevicename.md)
- [- setDeviceShortName](ioaudiodevice/1557028-setdeviceshortname.md)
- [- setDeviceTransportType](ioaudiodevice/1557051-setdevicetransporttype.md)
- [- setFamilyManagePower](ioaudiodevice/1557050-setfamilymanagepower.md)
- [- setIdleAudioSleepTime](ioaudiodevice/1557044-setidleaudiosleeptime.md)
- [- setManufacturerName](ioaudiodevice/1557019-setmanufacturername.md)
- [- setPowerState](ioaudiodevice/1557040-setpowerstate.md)
- [- start](ioaudiodevice/1557018-start.md)
- [- stop](ioaudiodevice/1557013-stop.md)
- [- waitForPendingPowerStateChange](ioaudiodevice/1557043-waitforpendingpowerstatechange.md)
- [- willTerminate](ioaudiodevice/1557049-willterminate.md)
### Type Methods
- [+ completePowerStateChangeAction](ioaudiodevice/1557052-completepowerstatechangeaction.md)
- [+ idleAudioSleepHandlerTimer](ioaudiodevice/1557058-idleaudiosleephandlertimer.md)
- [+ setPowerStateAction](ioaudiodevice/1557023-setpowerstateaction.md)
- [+ timerFired](ioaudiodevice/1557046-timerfired.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiodevice)*