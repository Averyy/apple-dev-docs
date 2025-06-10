# IOSCSIProtocolInterface

**Framework**: Kernel  
**Kind**: cl

This class defines the public SCSI Protocol Layer API for any class that provides Protocol services or needs to provide the Protocol Service API for passing service requests to a Protocol Service driver.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class IOSCSIProtocolInterface : IOService
```

## Topics

### Miscellaneous
- [AbortCommand](ioscsiprotocolinterface/1810020-abortcommand.md)
  Obsolete. Do not use this method.
- [AbortTask](ioscsiprotocolinterface/1810034-aborttask.md)
  Aborts a task based on the Logical Unit and tagged task identifier.
- [AbortTaskSet](ioscsiprotocolinterface/1810053-aborttaskset.md)
  Aborts a task set based on the Logical Unit.
- [CheckPowerState](ioscsiprotocolinterface/1810067-checkpowerstate.md)
  Called by clients to ensure device is in correct power state before issuing I/O.
- [ClearACA](ioscsiprotocolinterface/1810087-clearaca.md)
  Clears an Auto-Contingent Allegiance (ACA) for the specified Logical Unit.
- [ClearTaskSet](ioscsiprotocolinterface/1810108-cleartaskset.md)
  Clears a task set for the specified Logical Unit.
- [ExecuteCommand](ioscsiprotocolinterface/1810126-executecommand.md)
  Called to send a SCSITask and transport it across the physical wire(s) to the device.
- [finalize](ioscsiprotocolinterface/1810146-finalize.md)
  Finalizes the destruction of an IOService object.
- [free](ioscsiprotocolinterface/1810163-free.md)
  Called to release all resources held by the object.
- [GetCommandGate](ioscsiprotocolinterface/1810184-getcommandgate.md)
  Accessor method to obtain the IOCommandGate.
- [GetInitialPowerState](ioscsiprotocolinterface/1810205-getinitialpowerstate.md)
  This method is called to obtain the initial power state of the device (usually the highest).
- [GetUserClientExclusivityState](ioscsiprotocolinterface/1810233-getuserclientexclusivitystate.md)
  Gets the current exclusivity state of the user client.
- [HandleCheckPowerState()](ioscsiprotocolinterface/1810265-handlecheckpowerstate.md)
  The HandleCheckPowerState (void) method is on the serialized side of the command gate and can change member variables safely without multi-threading issues. It's main purpose is to call the superclass' HandleCheckPowerState ( UInt32 maxPowerState ) with the max power state the class registered with.
- [HandleCheckPowerState(UInt32)](ioscsiprotocolinterface/1810294-handlecheckpowerstate.md)
  The HandleCheckPowerState(UInt32 maxPowerState) method is called by the subclasses and is passed the maxPowerState number given to the power manager at initialization time. This guarantees the threads block until that power state has been achieved.
- [HandleCheckPowerState(void)](ioscsiprotocolinterface/1810368-handlecheckpowerstate.md)
  The HandleCheckPowerState (void) method is on the serialized side of the command gate and can change member variables safely without multi-threading issues. It's main purpose is to call the superclass' HandleCheckPowerState ( UInt32 maxPowerState ) with the max power state the class registered with.
- [HandleGetUserClientExclusivityState](ioscsiprotocolinterface/1810391-handlegetuserclientexclusivityst.md)
  Gets the current exclusivity state of the user client.
- [HandlePowerChange](ioscsiprotocolinterface/1810424-handlepowerchange.md)
  The HandlePowerChange method is pure virtual and is left to each protocol or application layer driver to implement. It is guaranteed to be called on its own thread of execution and can make synchronous or asynchronous calls.
- [HandleProtocolServiceFeature](ioscsiprotocolinterface/1810462-handleprotocolservicefeature.md)
  This method is called to enact support of a protocol specific service feature.
- [HandleSetPowerState](ioscsiprotocolinterface/1810510-handlesetpowerstate.md)
  The HandleSetPowerState method is called by the glue code and is on the serialized side of the command gate.
- [HandleSetUserClientExclusivityState](ioscsiprotocolinterface/1810570-handlesetuserclientexclusivityst.md)
  Sets the current exclusivity state of the user client.
- [InitializePowerManagement](ioscsiprotocolinterface/1810624-initializepowermanagement.md)
  This method is called to initialize power management.
- [initialPowerStateForDomainState](ioscsiprotocolinterface/1810676-initialpowerstatefordomainstate.md)
  Determines which power state a device is in, given the current power domain state.
- [IsPowerManagementIntialized](ioscsiprotocolinterface/1810727-ispowermanagementintialized.md)
  Called to determine if power management is initialized.
- [IsProtocolServiceSupported](ioscsiprotocolinterface/1810761-isprotocolservicesupported.md)
  This method is called to query for support of a protocol specific service feature.
- [LogicalUnitReset](ioscsiprotocolinterface/1810795-logicalunitreset.md)
  Resets the specified Logical Unit.
- [setPowerState](ioscsiprotocolinterface/1810826-setpowerstate.md)
  Requests a power managed driver to change the power state of its device.
- [SetUserClientExclusivityState](ioscsiprotocolinterface/1810852-setuserclientexclusivitystate.md)
  Sets the current exclusivity state of the user client.
- [sGetPowerTransistionInProgress](ioscsiprotocolinterface/1810884-sgetpowertransistioninprogress.md)
  The sGetPowerTransistionInProgress method is a static function used as C->C++ glue for going behind the command gate.
- [sGetUserClientExclusivityState](ioscsiprotocolinterface/1810914-sgetuserclientexclusivitystate.md)
  The sGetUserClientExclusivityState method is a static function used as C->C++ glue for going behind the command gate.
- [sHandleCheckPowerState](ioscsiprotocolinterface/1810945-shandlecheckpowerstate.md)
  The sHandleCheckPowerState method is a static function used as C->C++ glue for going behind the command gate.
- [sHandleSetPowerState](ioscsiprotocolinterface/1810965-shandlesetpowerstate.md)
  The sHandleSetPowerState method is a static function used as C->C++ glue for going behind the command gate.
- [sPowerManagement](ioscsiprotocolinterface/1810988-spowermanagement.md)
  The sPowerManagement method is a static C-function which is called using mach's thread_call API. It guarantees us a thread of execution which is different than the power management thread and the workloop thread on which we can issue commands to the device synchronously or asynchronously without worrying about deadlocks. It calls through to HandlePowerChange, which is a state machine used to direct power management.
- [sSetUserClientExclusivityState](ioscsiprotocolinterface/1811011-ssetuserclientexclusivitystate.md)
  The sSetUserClientExclusivityState method is a static function used as C->C++ glue for going behind the command gate.
- [start](ioscsiprotocolinterface/1811044-start.md)
  During an IOService object's instantiation, starts the IOService object that has been selected to run on the provider.
- [TargetReset](ioscsiprotocolinterface/1811073-targetreset.md)
  Resets the target device.
- [TicklePowerManager()](ioscsiprotocolinterface/1811095-ticklepowermanager.md)
  The TicklePowerManager(void) method is called by CheckPowerState and sends an activity tickle to the power manager so that the idle timer is reset.
- [TicklePowerManager(UInt32)](ioscsiprotocolinterface/1811118-ticklepowermanager.md)
  The TicklePowerManager(UInt32 maxPowerState) method is a convenience function which can be called by subclasses in TicklePowerManager (void) in order to tell the power manager to reset idle timer or bring the device into the requested state. It returns whatever is returned by activityTickle (true if device is in the requested state, false if it is not).
- [TicklePowerManager(void)](ioscsiprotocolinterface/1811187-ticklepowermanager.md)
  The TicklePowerManager(void) method is called by CheckPowerState and sends an activity tickle to the power manager so that the idle timer is reset.
- [willTerminate](ioscsiprotocolinterface/1811210-willterminate.md)
  Passes a termination up the stack.
### Instance Methods
- [- AbortCommand](ioscsiprotocolinterface/1571702-abortcommand.md)
- [- AbortTask](ioscsiprotocolinterface/1571657-aborttask.md)
- [- AbortTaskSet](ioscsiprotocolinterface/1571691-aborttaskset.md)
- [- CheckForSufficientTimeForPMCommand](ioscsiprotocolinterface/3727927-checkforsufficienttimeforpmcomma.md)
- [- CheckPowerState](ioscsiprotocolinterface/1571711-checkpowerstate.md)
- [- ClearACA](ioscsiprotocolinterface/1571655-clearaca.md)
- [- ClearTaskSet](ioscsiprotocolinterface/1571694-cleartaskset.md)
- [- ExecuteCommand](ioscsiprotocolinterface/1571682-executecommand.md)
- [- GetCommandGate](ioscsiprotocolinterface/1571674-getcommandgate.md)
- [- GetInitialPowerState](ioscsiprotocolinterface/1571659-getinitialpowerstate.md)
- [- GetUserClientExclusivityState](ioscsiprotocolinterface/1571707-getuserclientexclusivitystate.md)
- [- HandleCheckPowerState](ioscsiprotocolinterface/1571718-handlecheckpowerstate.md)
- [- HandleCheckPowerState](ioscsiprotocolinterface/3516767-handlecheckpowerstate.md)
- [- HandleGetUserClientExclusivityState](ioscsiprotocolinterface/1571677-handlegetuserclientexclusivityst.md)
- [- HandlePowerChange](ioscsiprotocolinterface/1571671-handlepowerchange.md)
- [- HandleProtocolServiceFeature](ioscsiprotocolinterface/1571701-handleprotocolservicefeature.md)
- [- HandleSetPowerState](ioscsiprotocolinterface/1571683-handlesetpowerstate.md)
- [- HandleSetUserClientExclusivityState](ioscsiprotocolinterface/1571652-handlesetuserclientexclusivityst.md)
- [- InitializePowerManagement](ioscsiprotocolinterface/1571688-initializepowermanagement.md)
- [- IsPowerManagementIntialized](ioscsiprotocolinterface/1571720-ispowermanagementintialized.md)
- [- IsProtocolServiceSupported](ioscsiprotocolinterface/1571658-isprotocolservicesupported.md)
- [- LogicalUnitReset](ioscsiprotocolinterface/1571680-logicalunitreset.md)
- [- ResetPowerStateChangeTimer](ioscsiprotocolinterface/3727928-resetpowerstatechangetimer.md)
- [- SetUserClientExclusivityState](ioscsiprotocolinterface/1571661-setuserclientexclusivitystate.md)
- [- TargetReset](ioscsiprotocolinterface/1571689-targetreset.md)
- [- TicklePowerManager](ioscsiprotocolinterface/1571698-ticklepowermanager.md)
- [- TicklePowerManager](ioscsiprotocolinterface/3516768-ticklepowermanager.md)
- [- finalize](ioscsiprotocolinterface/1571710-finalize.md)
- [- free](ioscsiprotocolinterface/1571704-free.md)
- [- getMetaClass](ioscsiprotocolinterface/1571709-getmetaclass.md)
- [- init](ioscsiprotocolinterface/1571678-init.md)
- [- initialPowerStateForDomainState](ioscsiprotocolinterface/1571696-initialpowerstatefordomainstate.md)
- [- setPowerState](ioscsiprotocolinterface/1571679-setpowerstate.md)
- [- start](ioscsiprotocolinterface/1571715-start.md)
- [- willTerminate](ioscsiprotocolinterface/1571699-willterminate.md)
### Type Methods
- [+ sGetPowerTransistionInProgress](ioscsiprotocolinterface/1571653-sgetpowertransistioninprogress.md)
- [+ sGetUserClientExclusivityState](ioscsiprotocolinterface/1571675-sgetuserclientexclusivitystate.md)
- [+ sHandleCheckPowerState](ioscsiprotocolinterface/1571676-shandlecheckpowerstate.md)
- [+ sHandleSetPowerState](ioscsiprotocolinterface/1571681-shandlesetpowerstate.md)
- [+ sPowerManagement](ioscsiprotocolinterface/1571656-spowermanagement.md)
- [+ sSetUserClientExclusivityState](ioscsiprotocolinterface/1571690-ssetuserclientexclusivitystate.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IOReducedBlockServices](ioreducedblockservices.md)
- [IOSCSIPeripheralDeviceNub](ioscsiperipheraldevicenub.md)
- [IOSCSIPrimaryCommandsDevice](ioscsiprimarycommandsdevice.md)
- [IOSCSIProtocolServices](ioscsiprotocolservices.md)
  This class defines the public SCSI Protocol Services Layer API for any class that implements SCSI protocol services. A protocol services layer driver is responsible for taking incoming SCSITaskIdentifier objects and translating them to the native command type for the native protocol interface (e.g. SBP-2 ORB on FireWire).


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiprotocolinterface)*