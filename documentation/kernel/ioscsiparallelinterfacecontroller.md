# IOSCSIParallelInterfaceController

**Framework**: Kernel  
**Kind**: cl

Class that represents a SCSI Host Bus Adapter.

**Availability**:
- macOS 10.2+ - Deprecated in 11.0

## Declaration

```swift
class IOSCSIParallelInterfaceController : IOService
```

#### Overview

Class that represents a SCSI Host Bus Adapter.

## Topics

### Miscellaneous
- [CompleteParallelTask](ioscsiparallelinterfacecontroller/1809862-completeparalleltask.md)
  Parallel Task Completion
- [CreateDeviceInterrupt](ioscsiparallelinterfacecontroller/1809876-createdeviceinterrupt.md)
  Called to create an IOInterruptEventSource for the device. Subclasses may wish to use a different interrupt index than 0 (e.g. for using PCI Message Signaled Interrupts) or might not need an interrupt at all (virtual HBA).
- [CreateTargetForID(SCSIDeviceIdentifier)](ioscsiparallelinterfacecontroller/1809880-createtargetforid.md)
  Method to perform device creation.
- [CreateTargetForID(SCSIDeviceIdentifier, OSDictionary *)](ioscsiparallelinterfacecontroller/1809885-createtargetforid.md)
  Method to perform device creation.
- [DestroyTargetForID](ioscsiparallelinterfacecontroller/1809890-destroytargetforid.md)
  Method to perform device destruction.
- [DisableInterrupt](ioscsiparallelinterfacecontroller/1809897-disableinterrupt.md)
  Disable Interrupt
- [DoesHBAPerformAutoSense](ioscsiparallelinterfacecontroller/1809901-doeshbaperformautosense.md)
  Queries the HBA child class to determine if it automatically performs AutoSense and provides AutoSense data for each I/O. If the HBA allocates space for AutoSense in its HBA specific data region on a per task basis, the HBA should respond true.
- [DoesHBAPerformDeviceManagement](ioscsiparallelinterfacecontroller/1809911-doeshbaperformdevicemanagement.md)
  Determine if HBA will manage devices.
- [DoesHBASupportMultiPathing](ioscsiparallelinterfacecontroller/1809914-doeshbasupportmultipathing.md)
  Queries the HBA child class to determine if it supports Multi-Pathing.
- [DoesHBASupportSCSIParallelFeature](ioscsiparallelinterfacecontroller/1809922-doeshbasupportscsiparallelfeatur.md)
  Queries the HBA child class to determine if it supports a specific SPI feature.
- [EnableInterrupt](ioscsiparallelinterfacecontroller/1809927-enableinterrupt.md)
  Enable Interrupt
- [ExecuteParallelTask](ioscsiparallelinterfacecontroller/1809933-executeparalleltask.md)
  Submit a SCSIParallelTask for execution.
- [FilterInterruptRequest](ioscsiparallelinterfacecontroller/1809938-filterinterruptrequest.md)
  Filter method called at primary interrupt time.
- [FindTaskForAddress](ioscsiparallelinterfacecontroller/1809945-findtaskforaddress.md)
  Find a task for a given Task Address, if one exists.
- [FindTaskForControllerIdentifier](ioscsiparallelinterfacecontroller/1809955-findtaskforcontrolleridentifier.md)
  Find a task for a given Target and Controller Task Identifier
- [FreeSCSIParallelTask](ioscsiparallelinterfacecontroller/1809961-freescsiparalleltask.md)
  Method to allow the client to release a SCSIParallelTask
- [GetAutoSenseData](ioscsiparallelinterfacecontroller/1809967-getautosensedata.md)
  Method to retrieve auto sense data buffer associated with a request.
- [GetAutoSenseDataSize](ioscsiparallelinterfacecontroller/1809971-getautosensedatasize.md)
  Method to retrieve auto sense data buffer size associated with a request.
- [GetCommandDescriptorBlock](ioscsiparallelinterfacecontroller/1809978-getcommanddescriptorblock.md)
  Method to retrieve the SCSI Command Descriptor Block (CDB).
- [GetCommandDescriptorBlockSize](ioscsiparallelinterfacecontroller/1809985-getcommanddescriptorblocksize.md)
  Method to retrieve the size of the SCSI Command Descriptor Block (CDB).
- [GetCommandGate](ioscsiparallelinterfacecontroller/1809991-getcommandgate.md)
  Accessor to get an IOCommandGate associated with the workloop.
- [GetDataBuffer](ioscsiparallelinterfacecontroller/1809997-getdatabuffer.md)
  Method to retrieve client buffer from the request.
- [GetDataBufferOffset](ioscsiparallelinterfacecontroller/1810001-getdatabufferoffset.md)
  Method to retrieve offset into client buffer at which to start processing.
- [GetDataTransferDirection](ioscsiparallelinterfacecontroller/1810008-getdatatransferdirection.md)
  Retrieves the data transfer direction for any data associated with the request.
- [GetDMACommand](ioscsiparallelinterfacecontroller/1810016-getdmacommand.md)
  Method to retrieve a pointer to an IODMACommand from the request.
- [GetHBADataDescriptor](ioscsiparallelinterfacecontroller/1810025-gethbadatadescriptor.md)
  Method to retrieve the IOMemoryDescriptor associated with the HBA Data.
- [GetHBADataPointer](ioscsiparallelinterfacecontroller/1810030-gethbadatapointer.md)
  Method to retrieve the HBA Data pointer.
- [GetHBADataSize](ioscsiparallelinterfacecontroller/1810042-gethbadatasize.md)
  Method to retrieve the HBA Data Size in bytes.
- [GetHBATargetDataPointer](ioscsiparallelinterfacecontroller/1810052-gethbatargetdatapointer.md)
  Method to retrieve the HBA Data pointer.
- [GetHBATargetDataSize](ioscsiparallelinterfacecontroller/1810061-gethbatargetdatasize.md)
  Method to retrieve the HBA Data Size in bytes.
- [GetLogicalUnitBytes](ioscsiparallelinterfacecontroller/1810076-getlogicalunitbytes.md)
  Method to get the logical unit bytes associated with a request.
- [GetLogicalUnitNumber](ioscsiparallelinterfacecontroller/1810082-getlogicalunitnumber.md)
  Method to get the logical unit number associated with a request.
- [GetProvider](ioscsiparallelinterfacecontroller/1810094-getprovider.md)
  Accessor method to get the IOService which is the controller's provider.
- [GetRealizedDataTransferCount](ioscsiparallelinterfacecontroller/1810102-getrealizeddatatransfercount.md)
  Retrieves the realized data transfer count for any data associated with the request.
- [GetRequestedDataTransferCount](ioscsiparallelinterfacecontroller/1810112-getrequesteddatatransfercount.md)
  Retrieves the requested data transfer count for any data associated with the request.
- [GetSCSIDomainIdentifier](ioscsiparallelinterfacecontroller/1810120-getscsidomainidentifier.md)
  Accessor method to get the SCSI Domain Identifier.
- [GetSCSIParallelFeatureNegotiation](ioscsiparallelinterfacecontroller/1810130-getscsiparallelfeaturenegotiatio.md)
  Method to retrieve the requested value for negotiation of the.
- [GetSCSIParallelFeatureNegotiationCount](ioscsiparallelinterfacecontroller/1810142-getscsiparallelfeaturenegotiatio.md)
  Method to retrieve the number of requested negotiations.
- [GetSCSIParallelFeatureNegotiationResult](ioscsiparallelinterfacecontroller/1810148-getscsiparallelfeaturenegotiatio.md)
  Method to retrieve the result of any wide transfer negotiations.
- [GetSCSIParallelFeatureNegotiationResultCount](ioscsiparallelinterfacecontroller/1810158-getscsiparallelfeaturenegotiatio.md)
  Method to retrieve the number of changed negotiations.
- [GetSCSIParallelTask](ioscsiparallelinterfacecontroller/1810170-getscsiparalleltask.md)
  Method to allow the client to get a SCSIParallelTask
- [GetSCSITaskIdentifier](ioscsiparallelinterfacecontroller/1810178-getscsitaskidentifier.md)
  Method to retrieve a SCSITaskIdentifier from a valid SCSIParallelTaskIdentifier.
- [GetTaggedTaskIdentifier](ioscsiparallelinterfacecontroller/1810189-gettaggedtaskidentifier.md)
  Method to retrieve the SCSI Tagged Task Identifier of the task. If the returned value is equal to kSCSIUntaggedTaskIdentifier, then this task is untagged.
- [GetTargetForID](ioscsiparallelinterfacecontroller/1810207-gettargetforid.md)
  Accessor for getting pointer to IOSCSIParallelInterfaceDevice.
- [GetTargetIdentifier](ioscsiparallelinterfacecontroller/1810218-gettargetidentifier.md)
  Method to get the SCSITargetIdentifier associated with a request.
- [GetTaskAttribute](ioscsiparallelinterfacecontroller/1810227-gettaskattribute.md)
  Method to retrieve the SCSI Task Attribute of the task
- [GetTimeoutDuration](ioscsiparallelinterfacecontroller/1810247-gettimeoutduration.md)
  Method to retrieve the timeout duration in milliseconds for a request.
- [GetWorkLoop](ioscsiparallelinterfacecontroller/1810257-getworkloop.md)
  Accessor method to get the IOWorkLoop associated with this HBA.
- [HandleInterruptRequest](ioscsiparallelinterfacecontroller/1810269-handleinterruptrequest.md)
  Handle Interrupt Request
- [HandleTimeout](ioscsiparallelinterfacecontroller/1810280-handletimeout.md)
  Method to handle command timeouts.
- [IncrementRealizedDataTransferCount](ioscsiparallelinterfacecontroller/1810290-incrementrealizeddatatransfercou.md)
  Increments the realized data transfer count. This method is helpful for when the HBA has to do multiple passes of DMA because there are more scatter-gather elements than it can process in one pass.
- [InitializeController](ioscsiparallelinterfacecontroller/1810299-initializecontroller.md)
  Called to initialize the controller
- [InitializeDMASpecification](ioscsiparallelinterfacecontroller/1810311-initializedmaspecification.md)
  Called to initialize an IODMACommand with a DMA specification.
- [InitializeTargetForID](ioscsiparallelinterfacecontroller/1810320-initializetargetforid.md)
  Called to initialize a target device.
- [NotifyClientsOfBusReset](ioscsiparallelinterfacecontroller/1810327-notifyclientsofbusreset.md)
  Method called to notify clients that a bus reset has occurred.
- [NotifyClientsOfPortStatusChange](ioscsiparallelinterfacecontroller/1810339-notifyclientsofportstatuschange.md)
  Method called to notify clients of port status change events.
- [ProcessParallelTask](ioscsiparallelinterfacecontroller/1810354-processparalleltask.md)
  Called by client to process a parallel task.
- [RemoveHBAProperty](ioscsiparallelinterfacecontroller/1810362-removehbaproperty.md)
  Accessor for removing a property for this object.
- [RemoveTargetProperty](ioscsiparallelinterfacecontroller/1810376-removetargetproperty.md)
  Accessor for removing a property from a specific target.
- [ReportHBAConstraints](ioscsiparallelinterfacecontroller/1810388-reporthbaconstraints.md)
  Called to report the I/O constraints for this controller. A list of valid keys includes: kIOMaximumSegmentCountReadKey, (required) kIOMaximumSegmentCountWriteKey, (required) kIOMaximumSegmentByteCountReadKey, (required) kIOMaximumSegmentByteCountWriteKey, (required) kIOMinimumSegmentAlignmentByteCountKey, (required) kIOMaximumSegmentAddressableBitCountKey, (required) kIOMinimumHBADataAlignmentMaskKey (required) kIOHierarchicalLogicalUnitSupportKey (optional). NB: These keys and their values are described in this header and <IOKit/IOKitKeys.h>
- [ReportHBAHighestLogicalUnitNumber](ioscsiparallelinterfacecontroller/1810401-reporthbahighestlogicalunitnumbe.md)
  Gets the Highest Logical Unit Number.
- [ReportHBASpecificDeviceDataSize](ioscsiparallelinterfacecontroller/1810414-reporthbaspecificdevicedatasize.md)
  Determine memory needed for HBA Device specific use.
- [ReportHBASpecificTaskDataSize](ioscsiparallelinterfacecontroller/1810430-reporthbaspecifictaskdatasize.md)
  Determine memory needed for HBA Task specific use.
- [ReportHighestSupportedDeviceID](ioscsiparallelinterfacecontroller/1810438-reporthighestsupporteddeviceid.md)
  Get the highest supported SCSI Device Identifier.
- [ReportInitiatorIdentifier](ioscsiparallelinterfacecontroller/1810459-reportinitiatoridentifier.md)
  Get the SCSI Device Identifier for the HBA.
- [ReportMaximumTaskCount](ioscsiparallelinterfacecontroller/1810468-reportmaximumtaskcount.md)
  Report Maximum Task Count
- [ResumeServices](ioscsiparallelinterfacecontroller/1810477-resumeservices.md)
  Called to resume controller services
- [SetAutoSenseData](ioscsiparallelinterfacecontroller/1810492-setautosensedata.md)
  Method to set the auto sense data buffer associated with a request.
- [SetControllerTaskIdentifier](ioscsiparallelinterfacecontroller/1810503-setcontrollertaskidentifier.md)
  Method to set the Controller Task Identifier.
- [SetHBAProperty](ioscsiparallelinterfacecontroller/1810516-sethbaproperty.md)
  Accessor for setting a property for this object.
- [SetRealizedDataTransferCount](ioscsiparallelinterfacecontroller/1810526-setrealizeddatatransfercount.md)
  Sets the realized data transfer count in bytes.
- [SetSCSIParallelFeatureNegotiationResult](ioscsiparallelinterfacecontroller/1810542-setscsiparallelfeaturenegotiatio.md)
  Method to set the wide data transfer negotiation result.
- [SetTargetProperty](ioscsiparallelinterfacecontroller/1810557-settargetproperty.md)
  Accessor for setting a property for a specific target.
- [SetTimeoutForTask](ioscsiparallelinterfacecontroller/1810571-settimeoutfortask.md)
  Method to set the timeout duration in milliseconds for a request.
- [SignalInterrupt](ioscsiparallelinterfacecontroller/1810589-signalinterrupt.md)
  Signals that an interrupt has occurred.
- [StartController](ioscsiparallelinterfacecontroller/1810612-startcontroller.md)
  Called to start the controller
- [StopController](ioscsiparallelinterfacecontroller/1810629-stopcontroller.md)
  Called to stop the controller
- [SuspendServices](ioscsiparallelinterfacecontroller/1810641-suspendservices.md)
  Called to suspend controller services
- [TerminateController](ioscsiparallelinterfacecontroller/1810669-terminatecontroller.md)
  Called to terminate the controller
### Instance Methods
- [- AbortTaskRequest](ioscsiparallelinterfacecontroller/1577150-aborttaskrequest.md)
- [- AbortTaskSetRequest](ioscsiparallelinterfacecontroller/1577179-aborttasksetrequest.md)
- [- AddDeviceToTargetList](ioscsiparallelinterfacecontroller/1577174-adddevicetotargetlist.md)
- [- AllocateSCSIParallelTasks](ioscsiparallelinterfacecontroller/1577235-allocatescsiparalleltasks.md)
- [- ClearACARequest](ioscsiparallelinterfacecontroller/1577255-clearacarequest.md)
- [- ClearTaskSetRequest](ioscsiparallelinterfacecontroller/1577281-cleartasksetrequest.md)
- [- CompleteAbortTask](ioscsiparallelinterfacecontroller/1577234-completeaborttask.md)
- [- CompleteAbortTaskSet](ioscsiparallelinterfacecontroller/1577147-completeaborttaskset.md)
- [- CompleteClearACA](ioscsiparallelinterfacecontroller/1577167-completeclearaca.md)
- [- CompleteClearTaskSet](ioscsiparallelinterfacecontroller/1577203-completecleartaskset.md)
- [- CompleteLogicalUnitReset](ioscsiparallelinterfacecontroller/1577160-completelogicalunitreset.md)
- [- CompleteOutstandingTasksForTarget](ioscsiparallelinterfacecontroller/3553418-completeoutstandingtasksfortarge.md)
- [- CompleteOutstandingTasksForTargetID](ioscsiparallelinterfacecontroller/3553419-completeoutstandingtasksfortarge.md)
- [- CompleteParallelTask](ioscsiparallelinterfacecontroller/1577148-completeparalleltask.md)
- [- CompleteTargetReset](ioscsiparallelinterfacecontroller/1577252-completetargetreset.md)
- [- CreateDeviceInterrupt](ioscsiparallelinterfacecontroller/1577143-createdeviceinterrupt.md)
- [- CreateTargetForID](ioscsiparallelinterfacecontroller/1577157-createtargetforid.md)
- [- CreateTargetForID](ioscsiparallelinterfacecontroller/3516772-createtargetforid.md)
- [- CreateWorkLoop](ioscsiparallelinterfacecontroller/1577210-createworkloop.md)
- [- DeallocateSCSIParallelTasks](ioscsiparallelinterfacecontroller/1577282-deallocatescsiparalleltasks.md)
- [- DestroyTargetForID](ioscsiparallelinterfacecontroller/1577285-destroytargetforid.md)
- [- DisableInterrupt](ioscsiparallelinterfacecontroller/1577191-disableinterrupt.md)
- [- DoesHBAPerformAutoSense](ioscsiparallelinterfacecontroller/1577158-doeshbaperformautosense.md)
- [- DoesHBAPerformDeviceManagement](ioscsiparallelinterfacecontroller/1577171-doeshbaperformdevicemanagement.md)
- [- DoesHBASupportMultiPathing](ioscsiparallelinterfacecontroller/1577159-doeshbasupportmultipathing.md)
- [- DoesHBASupportSCSIParallelFeature](ioscsiparallelinterfacecontroller/1577300-doeshbasupportscsiparallelfeatur.md)
- [- EnableInterrupt](ioscsiparallelinterfacecontroller/1577214-enableinterrupt.md)
- [- ExecuteParallelTask](ioscsiparallelinterfacecontroller/1577206-executeparalleltask.md)
- [- FilterInterruptRequest](ioscsiparallelinterfacecontroller/1577268-filterinterruptrequest.md)
- [- FindTaskForAddress](ioscsiparallelinterfacecontroller/1577181-findtaskforaddress.md)
- [- FindTaskForControllerIdentifier](ioscsiparallelinterfacecontroller/1577301-findtaskforcontrolleridentifier.md)
- [- FreeSCSIParallelTask](ioscsiparallelinterfacecontroller/1577216-freescsiparalleltask.md)
- [- GetAutoSenseData](ioscsiparallelinterfacecontroller/1577227-getautosensedata.md)
- [- GetAutoSenseDataSize](ioscsiparallelinterfacecontroller/1577273-getautosensedatasize.md)
- [- GetCommandDescriptorBlock](ioscsiparallelinterfacecontroller/1577177-getcommanddescriptorblock.md)
- [- GetCommandDescriptorBlockSize](ioscsiparallelinterfacecontroller/1577280-getcommanddescriptorblocksize.md)
- [- GetCommandGate](ioscsiparallelinterfacecontroller/1577218-getcommandgate.md)
- [- GetControllerTaskIdentifier](ioscsiparallelinterfacecontroller/1577298-getcontrollertaskidentifier.md)
- [- GetDMACommand](ioscsiparallelinterfacecontroller/1577172-getdmacommand.md)
- [- GetDataBuffer](ioscsiparallelinterfacecontroller/1577162-getdatabuffer.md)
- [- GetDataBufferOffset](ioscsiparallelinterfacecontroller/1577223-getdatabufferoffset.md)
- [- GetDataTransferDirection](ioscsiparallelinterfacecontroller/1577305-getdatatransferdirection.md)
- [- GetHBADataDescriptor](ioscsiparallelinterfacecontroller/1577292-gethbadatadescriptor.md)
- [- GetHBADataPointer](ioscsiparallelinterfacecontroller/1577229-gethbadatapointer.md)
- [- GetHBADataSize](ioscsiparallelinterfacecontroller/1577213-gethbadatasize.md)
- [- GetHBATargetDataPointer](ioscsiparallelinterfacecontroller/1577271-gethbatargetdatapointer.md)
- [- GetHBATargetDataSize](ioscsiparallelinterfacecontroller/1577180-gethbatargetdatasize.md)
- [- GetLogicalUnitBytes](ioscsiparallelinterfacecontroller/1577205-getlogicalunitbytes.md)
- [- GetLogicalUnitNumber](ioscsiparallelinterfacecontroller/1577242-getlogicalunitnumber.md)
- [- GetProvider](ioscsiparallelinterfacecontroller/1577284-getprovider.md)
- [- GetRealizedDataTransferCount](ioscsiparallelinterfacecontroller/1577188-getrealizeddatatransfercount.md)
- [- GetRequestedDataTransferCount](ioscsiparallelinterfacecontroller/1577168-getrequesteddatatransfercount.md)
- [- GetSCSIDomainIdentifier](ioscsiparallelinterfacecontroller/1577156-getscsidomainidentifier.md)
- [- GetSCSIParallelFeatureNegotiation](ioscsiparallelinterfacecontroller/1577260-getscsiparallelfeaturenegotiatio.md)
- [- GetSCSIParallelFeatureNegotiationCount](ioscsiparallelinterfacecontroller/1577164-getscsiparallelfeaturenegotiatio.md)
- [- GetSCSIParallelFeatureNegotiationResult](ioscsiparallelinterfacecontroller/1577297-getscsiparallelfeaturenegotiatio.md)
- [- GetSCSIParallelFeatureNegotiationResultCount](ioscsiparallelinterfacecontroller/1577266-getscsiparallelfeaturenegotiatio.md)
- [- GetSCSIParallelTask](ioscsiparallelinterfacecontroller/1577257-getscsiparalleltask.md)
- [- GetSCSITaskIdentifier](ioscsiparallelinterfacecontroller/1577228-getscsitaskidentifier.md)
- [- GetTaggedTaskIdentifier](ioscsiparallelinterfacecontroller/1577163-gettaggedtaskidentifier.md)
- [- GetTargetForID](ioscsiparallelinterfacecontroller/1577144-gettargetforid.md)
- [- GetTargetIdentifier](ioscsiparallelinterfacecontroller/1577302-gettargetidentifier.md)
- [- GetTaskAttribute](ioscsiparallelinterfacecontroller/1577175-gettaskattribute.md)
- [- GetTimeoutDuration](ioscsiparallelinterfacecontroller/1577250-gettimeoutduration.md)
- [- GetWorkLoop](ioscsiparallelinterfacecontroller/1577217-getworkloop.md)
- [- HandleInterruptRequest](ioscsiparallelinterfacecontroller/1577221-handleinterruptrequest.md)
- [- HandleTimeout](ioscsiparallelinterfacecontroller/1577232-handletimeout.md)
- [- IncrementRealizedDataTransferCount](ioscsiparallelinterfacecontroller/1577246-incrementrealizeddatatransfercou.md)
- [- InitializeController](ioscsiparallelinterfacecontroller/1577152-initializecontroller.md)
- [- InitializeDMASpecification](ioscsiparallelinterfacecontroller/1577193-initializedmaspecification.md)
- [- InitializeDeviceList](ioscsiparallelinterfacecontroller/1577289-initializedevicelist.md)
- [- InitializeTargetForID](ioscsiparallelinterfacecontroller/1577224-initializetargetforid.md)
- [- LogicalUnitResetRequest](ioscsiparallelinterfacecontroller/1577189-logicalunitresetrequest.md)
- [- NotifyClientsOfBusReset](ioscsiparallelinterfacecontroller/1577253-notifyclientsofbusreset.md)
- [- NotifyClientsOfPortStatusChange](ioscsiparallelinterfacecontroller/1577258-notifyclientsofportstatuschange.md)
- [- ProcessParallelTask](ioscsiparallelinterfacecontroller/1577165-processparalleltask.md)
- [- ReleaseWorkLoop](ioscsiparallelinterfacecontroller/1577275-releaseworkloop.md)
- [- RemoveDeviceFromTargetList](ioscsiparallelinterfacecontroller/1577296-removedevicefromtargetlist.md)
- [- RemoveHBAProperty](ioscsiparallelinterfacecontroller/1577295-removehbaproperty.md)
- [- RemoveTargetProperty](ioscsiparallelinterfacecontroller/1577247-removetargetproperty.md)
- [- ReportHBAConstraints](ioscsiparallelinterfacecontroller/1577267-reporthbaconstraints.md)
- [- ReportHBAHighestLogicalUnitNumber](ioscsiparallelinterfacecontroller/1577192-reporthbahighestlogicalunitnumbe.md)
- [- ReportHBASpecificDeviceDataSize](ioscsiparallelinterfacecontroller/1577212-reporthbaspecificdevicedatasize.md)
- [- ReportHBASpecificTaskDataSize](ioscsiparallelinterfacecontroller/1577256-reporthbaspecifictaskdatasize.md)
- [- ReportHighestSupportedDeviceID](ioscsiparallelinterfacecontroller/1577145-reporthighestsupporteddeviceid.md)
- [- ReportInitiatorIdentifier](ioscsiparallelinterfacecontroller/1577230-reportinitiatoridentifier.md)
- [- ReportMaximumTaskCount](ioscsiparallelinterfacecontroller/1577169-reportmaximumtaskcount.md)
- [- ResumeServices](ioscsiparallelinterfacecontroller/1577183-resumeservices.md)
- [- SetAutoSenseData](ioscsiparallelinterfacecontroller/1577161-setautosensedata.md)
- [- SetControllerTaskIdentifier](ioscsiparallelinterfacecontroller/1577186-setcontrollertaskidentifier.md)
- [- SetHBAProperty](ioscsiparallelinterfacecontroller/1577208-sethbaproperty.md)
- [- SetRealizedDataTransferCount](ioscsiparallelinterfacecontroller/1577142-setrealizeddatatransfercount.md)
- [- SetSCSIParallelFeatureNegotiationResult](ioscsiparallelinterfacecontroller/1577231-setscsiparallelfeaturenegotiatio.md)
- [- SetTargetProperty](ioscsiparallelinterfacecontroller/1577276-settargetproperty.md)
- [- SetTimeoutForTask](ioscsiparallelinterfacecontroller/1577248-settimeoutfortask.md)
- [- SignalInterrupt](ioscsiparallelinterfacecontroller/1577239-signalinterrupt.md)
- [- StartController](ioscsiparallelinterfacecontroller/1577166-startcontroller.md)
- [- StopController](ioscsiparallelinterfacecontroller/1577243-stopcontroller.md)
- [- SuspendServices](ioscsiparallelinterfacecontroller/1577304-suspendservices.md)
- [- TargetResetRequest](ioscsiparallelinterfacecontroller/1577270-targetresetrequest.md)
- [- TerminateController](ioscsiparallelinterfacecontroller/1577155-terminatecontroller.md)
- [- didTerminate](ioscsiparallelinterfacecontroller/1577263-didterminate.md)
- [- free](ioscsiparallelinterfacecontroller/1577225-free.md)
- [- getMetaClass](ioscsiparallelinterfacecontroller/1577254-getmetaclass.md)
- [- getWorkLoop](ioscsiparallelinterfacecontroller/1577197-getworkloop.md)
- [- handleClose](ioscsiparallelinterfacecontroller/1577154-handleclose.md)
- [- handleIsOpen](ioscsiparallelinterfacecontroller/1577303-handleisopen.md)
- [- handleOpen](ioscsiparallelinterfacecontroller/1577182-handleopen.md)
- [- start](ioscsiparallelinterfacecontroller/1577220-start.md)
- [- stop](ioscsiparallelinterfacecontroller/1577287-stop.md)
- [- willTerminate](ioscsiparallelinterfacecontroller/1577238-willterminate.md)
### Type Methods
- [+ FilterInterrupt](ioscsiparallelinterfacecontroller/1577283-filterinterrupt.md)
- [+ ServiceInterrupt](ioscsiparallelinterfacecontroller/1577240-serviceinterrupt.md)
- [+ TimeoutOccurred](ioscsiparallelinterfacecontroller/1577190-timeoutoccurred.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IOSCSILogicalUnitNub](ioscsilogicalunitnub.md)
- [IOSCSIPeripheralDeviceType05](ioscsiperipheraldevicetype05.md)
- [IOSCSIMultimediaCommandsDevice](ioscsimultimediacommandsdevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiparallelinterfacecontroller)*