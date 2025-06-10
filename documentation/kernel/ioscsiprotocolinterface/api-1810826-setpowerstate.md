# setPowerState

**Framework**: Kernel  
**Kind**: instm

Requests a power managed driver to change the power state of its device.

## Declaration

```swift
virtual IOReturn setPowerState (
 unsigned longpowerStateOrdinal,
 IOService *whichDevice );
```

#### Return_value

See IOService.h for details.

#### Overview

Requests a power managed driver to change the power state of its device. Most subclasses of IOSCSIProtocolInterface have class-specific mechanisms and should not override this routine. See IOSCSIProtocolServices.h, IOSCSIBlockCommandsDevice.h, IOSCSIReducedBlockCommandsDevice.h, and IOSCSIMultimediaCommandsDevice.h for more information about power management changes. Subclasses should not need to override this method.

## Parameters

- `powerStateOrdinal`: The number in the power state array to which the drive is being instructed to change.
- `whichDevice`: A pointer to the power management object which registered to manage power for this device. The whichDevice field is not pertinent to us since the driver is both the "policy maker" for the device, and the "policy implementor" for the device.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiprotocolinterface/1810826-setpowerstate)*