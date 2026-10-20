# IOSCSIParallelInterfaceController

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

Class that represents a SCSI Host Bus Adapter.

**Availability**:
- macOS 10.2+ - Deprecated in 11.0

## Declaration

```cpp
class IOSCSIParallelInterfaceController : IOService
```

#### Overview

Class that represents a SCSI Host Bus Adapter.

## Topics

### Miscellaneous
- [CompleteParallelTask](./ioscsiparallelinterfacecontroller/api-1809862-completeparalleltask.md)
  Parallel Task Completion
- [CreateDeviceInterrupt](./ioscsiparallelinterfacecontroller/api-1809876-createdeviceinterrupt.md)
  Called to create an IOInterruptEventSource for the device. Subclasses may wish to use a different interrupt index than 0 (e.g. for using PCI Message Signaled Interrupts) or might not need an interrupt at all (virtual HBA).
- [CreateTargetForID(SCSIDeviceIdentifier)](./ioscsiparallelinterfacecontroller/api-1809880-createtargetforid.md)
  Method to perform device creation.
- [CreateTargetForID(SCSIDeviceIdentifier, OSDictionary *)](./ioscsiparallelinterfacecontroller/api-1809885-createtargetforid.md)
  Method to perform device creation.
- [DestroyTargetForID](./ioscsiparallelinterfacecontroller/api-1809890-destroytargetforid.md)
  Method to perform device destruction.
- [DisableInterrupt](./ioscsiparallelinterfacecontroller/api-1809897-disableinterrupt.md)
  Disable Interrupt
- [DoesHBAPerformAutoSense](./ioscsiparallelinterfacecontroller/api-1809901-doeshbaperformautosense.md)
  Queries the HBA child class to determine if it automatically performs AutoSense and provides AutoSense data for each I/O. If the HBA allocates space for AutoSense in its HBA specific data region on a per task basis, the HBA should respond true.
- [DoesHBAPerformDeviceManagement](./ioscsiparallelinterfacecontroller/api-1809911-doeshbaperformdevicemanagement.md)
  Determine if HBA will manage devices.
- [DoesHBASupportMultiPathing](./ioscsiparallelinterfacecontroller/api-1809914-doeshbasupportmultipathing.md)
  Queries the HBA child class to determine if it supports Multi-Pathing.
- [DoesHBASupportSCSIParallelFeature](./ioscsiparallelinterfacecontroller/api-1809922-doeshbasupportscsiparallelfeatur.md)
  Queries the HBA child class to determine if it supports a specific SPI feature.
- [EnableInterrupt](./ioscsiparallelinterfacecontroller/api-1809927-enableinterrupt.md)
  Enable Interrupt
- [ExecuteParallelTask](./ioscsiparallelinterfacecontroller/api-1809933-executeparalleltask.md)
  Submit a SCSIParallelTask for execution.
- [FilterInterruptRequest](./ioscsiparallelinterfacecontroller/api-1809938-filterinterruptrequest.md)
  Filter method called at primary interrupt time.
- [FindTaskForAddress](./ioscsiparallelinterfacecontroller/api-1809945-findtaskforaddress.md)
  Find a task for a given Task Address, if one exists.
- [FindTaskForControllerIdentifier](./ioscsiparallelinterfacecontroller/api-1809955-findtaskforcontrolleridentifier.md)
  Find a task for a given Target and Controller Task Identifier
- [FreeSCSIParallelTask](./ioscsiparallelinterfacecontroller/api-1809961-freescsiparalleltask.md)
  Method to allow the client to release a SCSIParallelTask
- [GetAutoSenseData](./ioscsiparallelinterfacecontroller/api-1809967-getautosensedata.md)
  Method to retrieve auto sense data buffer associated with a request.
- [GetAutoSenseDataSize](./ioscsiparallelinterfacecontroller/api-1809971-getautosensedatasize.md)
  Method to retrieve auto sense data buffer size associated with a request.
- [GetCommandDescriptorBlock](./ioscsiparallelinterfacecontroller/api-1809978-getcommanddescriptorblock.md)
  Method to retrieve the SCSI Command Descriptor Block (CDB).
- [GetCommandDescriptorBlockSize](./ioscsiparallelinterfacecontroller/api-1809985-getcommanddescriptorblocksize.md)
  Method to retrieve the size of the SCSI Command Descriptor Block (CDB).
- [GetCommandGate](./ioscsiparallelinterfacecontroller/api-1809991-getcommandgate.md)
  Accessor to get an IOCommandGate associated with the workloop.
- [GetDataBuffer](./ioscsiparallelinterfacecontroller/api-1809997-getdatabuffer.md)
  Method to retrieve client buffer from the request.
- [GetDataBufferOffset](./ioscsiparallelinterfacecontroller/api-1810001-getdatabufferoffset.md)
  Method to retrieve offset into client buffer at which to start processing.
- [GetDataTransferDirection](./ioscsiparallelinterfacecontroller/api-1810008-getdatatransferdirection.md)
  Retrieves the data transfer direction for any data associated with the request.
- [GetDMACommand](./ioscsiparallelinterfacecontroller/api-1810016-getdmacommand.md)
  Method to retrieve a pointer to an IODMACommand from the request.
- [GetHBADataDescriptor](./ioscsiparallelinterfacecontroller/api-1810025-gethbadatadescriptor.md)
  Method to retrieve the IOMemoryDescriptor associated with the HBA Data.
- [GetHBADataPointer](./ioscsiparallelinterfacecontroller/api-1810030-gethbadatapointer.md)
  Method to retrieve the HBA Data pointer.
- [GetHBADataSize](./ioscsiparallelinterfacecontroller/api-1810042-gethbadatasize.md)
  Method to retrieve the HBA Data Size in bytes.
- [GetHBATargetDataPointer](./ioscsiparallelinterfacecontroller/api-1810052-gethbatargetdatapointer.md)
  Method to retrieve the HBA Data pointer.
- [GetHBATargetDataSize](./ioscsiparallelinterfacecontroller/api-1810061-gethbatargetdatasize.md)
  Method to retrieve the HBA Data Size in bytes.
- [GetLogicalUnitBytes](./ioscsiparallelinterfacecontroller/api-1810076-getlogicalunitbytes.md)
  Method to get the logical unit bytes associated with a request.
- [GetLogicalUnitNumber](./ioscsiparallelinterfacecontroller/api-1810082-getlogicalunitnumber.md)
  Method to get the logical unit number associated with a request.
- [GetProvider](./ioscsiparallelinterfacecontroller/api-1810094-getprovider.md)
  Accessor method to get the IOService which is the controller's provider.
- [GetRealizedDataTransferCount](./ioscsiparallelinterfacecontroller/api-1810102-getrealizeddatatransfercount.md)
  Retrieves the realized data transfer count for any data associated with the request.
- [GetRequestedDataTransferCount](./ioscsiparallelinterfacecontroller/api-1810112-getrequesteddatatransfercount.md)
  Retrieves the requested data transfer count for any data associated with the request.
- [GetSCSIDomainIdentifier](./ioscsiparallelinterfacecontroller/api-1810120-getscsidomainidentifier.md)
  Accessor method to get the SCSI Domain Identifier.
- [GetSCSIParallelFeatureNegotiation](./ioscsiparallelinterfacecontroller/api-1810130-getscsiparallelfeaturenegotiatio.md)
  Method to retrieve the requested value for negotiation of the.
- [GetSCSIParallelFeatureNegotiationCount](./ioscsiparallelinterfacecontroller/api-1810142-getscsiparallelfeaturenegotiatio.md)
  Method to retrieve the number of requested negotiations.
- [GetSCSIParallelFeatureNegotiationResult](./ioscsiparallelinterfacecontroller/api-1810148-getscsiparallelfeaturenegotiatio.md)
  Method to retrieve the result of any wide transfer negotiations.
- [GetSCSIParallelFeatureNegotiationResultCount](./ioscsiparallelinterfacecontroller/api-1810158-getscsiparallelfeaturenegotiatio.md)
  Method to retrieve the number of changed negotiations.
- [GetSCSIParallelTask](./ioscsiparallelinterfacecontroller/api-1810170-getscsiparalleltask.md)
  Method to allow the client to get a SCSIParallelTask
- [GetSCSITaskIdentifier](./ioscsiparallelinterfacecontroller/api-1810178-getscsitaskidentifier.md)
  Method to retrieve a SCSITaskIdentifier from a valid SCSIParallelTaskIdentifier.
- [GetTaggedTaskIdentifier](./ioscsiparallelinterfacecontroller/api-1810189-gettaggedtaskidentifier.md)
  Method to retrieve the SCSI Tagged Task Identifier of the task. If the returned value is equal to kSCSIUntaggedTaskIdentifier, then this task is untagged.
- [GetTargetForID](./ioscsiparallelinterfacecontroller/api-1810207-gettargetforid.md)
  Accessor for getting pointer to IOSCSIParallelInterfaceDevice.
- [GetTargetIdentifier](./ioscsiparallelinterfacecontroller/api-1810218-gettargetidentifier.md)
  Method to get the SCSITargetIdentifier associated with a request.
- [GetTaskAttribute](./ioscsiparallelinterfacecontroller/api-1810227-gettaskattribute.md)
  Method to retrieve the SCSI Task Attribute of the task
- [GetTimeoutDuration](./ioscsiparallelinterfacecontroller/api-1810247-gettimeoutduration.md)
  Method to retrieve the timeout duration in milliseconds for a request.
- [GetWorkLoop](./ioscsiparallelinterfacecontroller/api-1810257-getworkloop.md)
  Accessor method to get the IOWorkLoop associated with this HBA.
- [HandleInterruptRequest](./ioscsiparallelinterfacecontroller/api-1810269-handleinterruptrequest.md)
  Handle Interrupt Request
- [HandleTimeout](./ioscsiparallelinterfacecontroller/api-1810280-handletimeout.md)
  Method to handle command timeouts.
- [IncrementRealizedDataTransferCount](./ioscsiparallelinterfacecontroller/api-1810290-incrementrealizeddatatransfercou.md)
  Increments the realized data transfer count. This method is helpful for when the HBA has to do multiple passes of DMA because there are more scatter-gather elements than it can process in one pass.
- [InitializeController](./ioscsiparallelinterfacecontroller/api-1810299-initializecontroller.md)
  Called to initialize the controller
- [InitializeDMASpecification](./ioscsiparallelinterfacecontroller/api-1810311-initializedmaspecification.md)
  Called to initialize an IODMACommand with a DMA specification.
- [InitializeTargetForID](./ioscsiparallelinterfacecontroller/api-1810320-initializetargetforid.md)
  Called to initialize a target device.
- [NotifyClientsOfBusReset](./ioscsiparallelinterfacecontroller/api-1810327-notifyclientsofbusreset.md)
  Method called to notify clients that a bus reset has occurred.
- [NotifyClientsOfPortStatusChange](./ioscsiparallelinterfacecontroller/api-1810339-notifyclientsofportstatuschange.md)
  Method called to notify clients of port status change events.
- [ProcessParallelTask](./ioscsiparallelinterfacecontroller/api-1810354-processparalleltask.md)
  Called by client to process a parallel task.
- [RemoveHBAProperty](./ioscsiparallelinterfacecontroller/api-1810362-removehbaproperty.md)
  Accessor for removing a property for this object.
- [RemoveTargetProperty](./ioscsiparallelinterfacecontroller/api-1810376-removetargetproperty.md)
  Accessor for removing a property from a specific target.
- [ReportHBAConstraints](./ioscsiparallelinterfacecontroller/api-1810388-reporthbaconstraints.md)
  Called to report the I/O constraints for this controller. A list of valid keys includes: kIOMaximumSegmentCountReadKey, (required) kIOMaximumSegmentCountWriteKey, (required) kIOMaximumSegmentByteCountReadKey, (required) kIOMaximumSegmentByteCountWriteKey, (required) kIOMinimumSegmentAlignmentByteCountKey, (required) kIOMaximumSegmentAddressableBitCountKey, (required) kIOMinimumHBADataAlignmentMaskKey (required) kIOHierarchicalLogicalUnitSupportKey (optional). NB: These keys and their values are described in this header and <IOKit/IOKitKeys.h>
- [ReportHBAHighestLogicalUnitNumber](./ioscsiparallelinterfacecontroller/api-1810401-reporthbahighestlogicalunitnumbe.md)
  Gets the Highest Logical Unit Number.
- [ReportHBASpecificDeviceDataSize](./ioscsiparallelinterfacecontroller/api-1810414-reporthbaspecificdevicedatasize.md)
  Determine memory needed for HBA Device specific use.
- [ReportHBASpecificTaskDataSize](./ioscsiparallelinterfacecontroller/api-1810430-reporthbaspecifictaskdatasize.md)
  Determine memory needed for HBA Task specific use.
- [ReportHighestSupportedDeviceID](./ioscsiparallelinterfacecontroller/api-1810438-reporthighestsupporteddeviceid.md)
  Get the highest supported SCSI Device Identifier.
- [ReportInitiatorIdentifier](./ioscsiparallelinterfacecontroller/api-1810459-reportinitiatoridentifier.md)
  Get the SCSI Device Identifier for the HBA.
- [ReportMaximumTaskCount](./ioscsiparallelinterfacecontroller/api-1810468-reportmaximumtaskcount.md)
  Report Maximum Task Count
- [ResumeServices](./ioscsiparallelinterfacecontroller/api-1810477-resumeservices.md)
  Called to resume controller services
- [SetAutoSenseData](./ioscsiparallelinterfacecontroller/api-1810492-setautosensedata.md)
  Method to set the auto sense data buffer associated with a request.
- [SetControllerTaskIdentifier](./ioscsiparallelinterfacecontroller/api-1810503-setcontrollertaskidentifier.md)
  Method to set the Controller Task Identifier.
- [SetHBAProperty](./ioscsiparallelinterfacecontroller/api-1810516-sethbaproperty.md)
  Accessor for setting a property for this object.
- [SetRealizedDataTransferCount](./ioscsiparallelinterfacecontroller/api-1810526-setrealizeddatatransfercount.md)
  Sets the realized data transfer count in bytes.
- [SetSCSIParallelFeatureNegotiationResult](./ioscsiparallelinterfacecontroller/api-1810542-setscsiparallelfeaturenegotiatio.md)
  Method to set the wide data transfer negotiation result.
- [SetTargetProperty](./ioscsiparallelinterfacecontroller/api-1810557-settargetproperty.md)
  Accessor for setting a property for a specific target.
- [SetTimeoutForTask](./ioscsiparallelinterfacecontroller/api-1810571-settimeoutfortask.md)
  Method to set the timeout duration in milliseconds for a request.
- [SignalInterrupt](./ioscsiparallelinterfacecontroller/api-1810589-signalinterrupt.md)
  Signals that an interrupt has occurred.
- [StartController](./ioscsiparallelinterfacecontroller/api-1810612-startcontroller.md)
  Called to start the controller
- [StopController](./ioscsiparallelinterfacecontroller/api-1810629-stopcontroller.md)
  Called to stop the controller
- [SuspendServices](./ioscsiparallelinterfacecontroller/api-1810641-suspendservices.md)
  Called to suspend controller services
- [TerminateController](./ioscsiparallelinterfacecontroller/api-1810669-terminatecontroller.md)
  Called to terminate the controller
### Instance Methods
- [- AbortTaskRequest](./ioscsiparallelinterfacecontroller/api-1577150-aborttaskrequest.md)
- [- AbortTaskSetRequest](./ioscsiparallelinterfacecontroller/api-1577179-aborttasksetrequest.md)
- [- AddDeviceToTargetList](./ioscsiparallelinterfacecontroller/api-1577174-adddevicetotargetlist.md)
- [- AllocateSCSIParallelTasks](./ioscsiparallelinterfacecontroller/api-1577235-allocatescsiparalleltasks.md)
- [- ClearACARequest](./ioscsiparallelinterfacecontroller/api-1577255-clearacarequest.md)
- [- ClearTaskSetRequest](./ioscsiparallelinterfacecontroller/api-1577281-cleartasksetrequest.md)
- [- CompleteAbortTask](./ioscsiparallelinterfacecontroller/api-1577234-completeaborttask.md)
- [- CompleteAbortTaskSet](./ioscsiparallelinterfacecontroller/api-1577147-completeaborttaskset.md)
- [- CompleteClearACA](./ioscsiparallelinterfacecontroller/api-1577167-completeclearaca.md)
- [- CompleteClearTaskSet](./ioscsiparallelinterfacecontroller/api-1577203-completecleartaskset.md)
- [- CompleteLogicalUnitReset](./ioscsiparallelinterfacecontroller/api-1577160-completelogicalunitreset.md)
- [- CompleteOutstandingTasksForTarget](./ioscsiparallelinterfacecontroller/api-3553418-completeoutstandingtasksfortarge.md)
- [- CompleteOutstandingTasksForTargetID](./ioscsiparallelinterfacecontroller/api-3553419-completeoutstandingtasksfortarge.md)
- [- CompleteParallelTask](./ioscsiparallelinterfacecontroller/api-1577148-completeparalleltask.md)
- [- CompleteTargetReset](./ioscsiparallelinterfacecontroller/api-1577252-completetargetreset.md)
- [- CreateDeviceInterrupt](./ioscsiparallelinterfacecontroller/api-1577143-createdeviceinterrupt.md)
- [- CreateTargetForID](./ioscsiparallelinterfacecontroller/api-1577157-createtargetforid.md)
- [- CreateTargetForID](./ioscsiparallelinterfacecontroller/api-3516772-createtargetforid.md)
- [- CreateWorkLoop](./ioscsiparallelinterfacecontroller/api-1577210-createworkloop.md)
- [- DeallocateSCSIParallelTasks](./ioscsiparallelinterfacecontroller/api-1577282-deallocatescsiparalleltasks.md)
- [- DestroyTargetForID](./ioscsiparallelinterfacecontroller/api-1577285-destroytargetforid.md)
- [- DisableInterrupt](./ioscsiparallelinterfacecontroller/api-1577191-disableinterrupt.md)
- [- DoesHBAPerformAutoSense](./ioscsiparallelinterfacecontroller/api-1577158-doeshbaperformautosense.md)
- [- DoesHBAPerformDeviceManagement](./ioscsiparallelinterfacecontroller/api-1577171-doeshbaperformdevicemanagement.md)
- [- DoesHBASupportMultiPathing](./ioscsiparallelinterfacecontroller/api-1577159-doeshbasupportmultipathing.md)
- [- DoesHBASupportSCSIParallelFeature](./ioscsiparallelinterfacecontroller/api-1577300-doeshbasupportscsiparallelfeatur.md)
- [- EnableInterrupt](./ioscsiparallelinterfacecontroller/api-1577214-enableinterrupt.md)
- [- ExecuteParallelTask](./ioscsiparallelinterfacecontroller/api-1577206-executeparalleltask.md)
- [- FilterInterruptRequest](./ioscsiparallelinterfacecontroller/api-1577268-filterinterruptrequest.md)
- [- FindTaskForAddress](./ioscsiparallelinterfacecontroller/api-1577181-findtaskforaddress.md)
- [- FindTaskForControllerIdentifier](./ioscsiparallelinterfacecontroller/api-1577301-findtaskforcontrolleridentifier.md)
- [- FreeSCSIParallelTask](./ioscsiparallelinterfacecontroller/api-1577216-freescsiparalleltask.md)
- [- GetAutoSenseData](./ioscsiparallelinterfacecontroller/api-1577227-getautosensedata.md)
- [- GetAutoSenseDataSize](./ioscsiparallelinterfacecontroller/api-1577273-getautosensedatasize.md)
- [- GetCommandDescriptorBlock](./ioscsiparallelinterfacecontroller/api-1577177-getcommanddescriptorblock.md)
- [- GetCommandDescriptorBlockSize](./ioscsiparallelinterfacecontroller/api-1577280-getcommanddescriptorblocksize.md)
- [- GetCommandGate](./ioscsiparallelinterfacecontroller/api-1577218-getcommandgate.md)
- [- GetControllerTaskIdentifier](./ioscsiparallelinterfacecontroller/api-1577298-getcontrollertaskidentifier.md)
- [- GetDMACommand](./ioscsiparallelinterfacecontroller/api-1577172-getdmacommand.md)
- [- GetDataBuffer](./ioscsiparallelinterfacecontroller/api-1577162-getdatabuffer.md)
- [- GetDataBufferOffset](./ioscsiparallelinterfacecontroller/api-1577223-getdatabufferoffset.md)
- [- GetDataTransferDirection](./ioscsiparallelinterfacecontroller/api-1577305-getdatatransferdirection.md)
- [- GetHBADataDescriptor](./ioscsiparallelinterfacecontroller/api-1577292-gethbadatadescriptor.md)
- [- GetHBADataPointer](./ioscsiparallelinterfacecontroller/api-1577229-gethbadatapointer.md)
- [- GetHBADataSize](./ioscsiparallelinterfacecontroller/api-1577213-gethbadatasize.md)
- [- GetHBATargetDataPointer](./ioscsiparallelinterfacecontroller/api-1577271-gethbatargetdatapointer.md)
- [- GetHBATargetDataSize](./ioscsiparallelinterfacecontroller/api-1577180-gethbatargetdatasize.md)
- [- GetLogicalUnitBytes](./ioscsiparallelinterfacecontroller/api-1577205-getlogicalunitbytes.md)
- [- GetLogicalUnitNumber](./ioscsiparallelinterfacecontroller/api-1577242-getlogicalunitnumber.md)
- [- GetProvider](./ioscsiparallelinterfacecontroller/api-1577284-getprovider.md)
- [- GetRealizedDataTransferCount](./ioscsiparallelinterfacecontroller/api-1577188-getrealizeddatatransfercount.md)
- [- GetRequestedDataTransferCount](./ioscsiparallelinterfacecontroller/api-1577168-getrequesteddatatransfercount.md)
- [- GetSCSIDomainIdentifier](./ioscsiparallelinterfacecontroller/api-1577156-getscsidomainidentifier.md)
- [- GetSCSIParallelFeatureNegotiation](./ioscsiparallelinterfacecontroller/api-1577260-getscsiparallelfeaturenegotiatio.md)
- [- GetSCSIParallelFeatureNegotiationCount](./ioscsiparallelinterfacecontroller/api-1577164-getscsiparallelfeaturenegotiatio.md)
- [- GetSCSIParallelFeatureNegotiationResult](./ioscsiparallelinterfacecontroller/api-1577297-getscsiparallelfeaturenegotiatio.md)
- [- GetSCSIParallelFeatureNegotiationResultCount](./ioscsiparallelinterfacecontroller/api-1577266-getscsiparallelfeaturenegotiatio.md)
- [- GetSCSIParallelTask](./ioscsiparallelinterfacecontroller/api-1577257-getscsiparalleltask.md)
- [- GetSCSITaskIdentifier](./ioscsiparallelinterfacecontroller/api-1577228-getscsitaskidentifier.md)
- [- GetTaggedTaskIdentifier](./ioscsiparallelinterfacecontroller/api-1577163-gettaggedtaskidentifier.md)
- [- GetTargetForID](./ioscsiparallelinterfacecontroller/api-1577144-gettargetforid.md)
- [- GetTargetIdentifier](./ioscsiparallelinterfacecontroller/api-1577302-gettargetidentifier.md)
- [- GetTaskAttribute](./ioscsiparallelinterfacecontroller/api-1577175-gettaskattribute.md)
- [- GetTimeoutDuration](./ioscsiparallelinterfacecontroller/api-1577250-gettimeoutduration.md)
- [- GetWorkLoop](./ioscsiparallelinterfacecontroller/api-1577217-getworkloop.md)
- [- HandleInterruptRequest](./ioscsiparallelinterfacecontroller/api-1577221-handleinterruptrequest.md)
- [- HandleTimeout](./ioscsiparallelinterfacecontroller/api-1577232-handletimeout.md)
- [- IncrementRealizedDataTransferCount](./ioscsiparallelinterfacecontroller/api-1577246-incrementrealizeddatatransfercou.md)
- [- InitializeController](./ioscsiparallelinterfacecontroller/api-1577152-initializecontroller.md)
- [- InitializeDMASpecification](./ioscsiparallelinterfacecontroller/api-1577193-initializedmaspecification.md)
- [- InitializeDeviceList](./ioscsiparallelinterfacecontroller/api-1577289-initializedevicelist.md)
- [- InitializeTargetForID](./ioscsiparallelinterfacecontroller/api-1577224-initializetargetforid.md)
- [- LogicalUnitResetRequest](./ioscsiparallelinterfacecontroller/api-1577189-logicalunitresetrequest.md)
- [- NotifyClientsOfBusReset](./ioscsiparallelinterfacecontroller/api-1577253-notifyclientsofbusreset.md)
- [- NotifyClientsOfPortStatusChange](./ioscsiparallelinterfacecontroller/api-1577258-notifyclientsofportstatuschange.md)
- [- ProcessParallelTask](./ioscsiparallelinterfacecontroller/api-1577165-processparalleltask.md)
- [- ReleaseWorkLoop](./ioscsiparallelinterfacecontroller/api-1577275-releaseworkloop.md)
- [- RemoveDeviceFromTargetList](./ioscsiparallelinterfacecontroller/api-1577296-removedevicefromtargetlist.md)
- [- RemoveHBAProperty](./ioscsiparallelinterfacecontroller/api-1577295-removehbaproperty.md)
- [- RemoveTargetProperty](./ioscsiparallelinterfacecontroller/api-1577247-removetargetproperty.md)
- [- ReportHBAConstraints](./ioscsiparallelinterfacecontroller/api-1577267-reporthbaconstraints.md)
- [- ReportHBAHighestLogicalUnitNumber](./ioscsiparallelinterfacecontroller/api-1577192-reporthbahighestlogicalunitnumbe.md)
- [- ReportHBASpecificDeviceDataSize](./ioscsiparallelinterfacecontroller/api-1577212-reporthbaspecificdevicedatasize.md)
- [- ReportHBASpecificTaskDataSize](./ioscsiparallelinterfacecontroller/api-1577256-reporthbaspecifictaskdatasize.md)
- [- ReportHighestSupportedDeviceID](./ioscsiparallelinterfacecontroller/api-1577145-reporthighestsupporteddeviceid.md)
- [- ReportInitiatorIdentifier](./ioscsiparallelinterfacecontroller/api-1577230-reportinitiatoridentifier.md)
- [- ReportMaximumTaskCount](./ioscsiparallelinterfacecontroller/api-1577169-reportmaximumtaskcount.md)
- [- ResumeServices](./ioscsiparallelinterfacecontroller/api-1577183-resumeservices.md)
- [- SetAutoSenseData](./ioscsiparallelinterfacecontroller/api-1577161-setautosensedata.md)
- [- SetControllerTaskIdentifier](./ioscsiparallelinterfacecontroller/api-1577186-setcontrollertaskidentifier.md)
- [- SetHBAProperty](./ioscsiparallelinterfacecontroller/api-1577208-sethbaproperty.md)
- [- SetRealizedDataTransferCount](./ioscsiparallelinterfacecontroller/api-1577142-setrealizeddatatransfercount.md)
- [- SetSCSIParallelFeatureNegotiationResult](./ioscsiparallelinterfacecontroller/api-1577231-setscsiparallelfeaturenegotiatio.md)
- [- SetTargetProperty](./ioscsiparallelinterfacecontroller/api-1577276-settargetproperty.md)
- [- SetTimeoutForTask](./ioscsiparallelinterfacecontroller/api-1577248-settimeoutfortask.md)
- [- SignalInterrupt](./ioscsiparallelinterfacecontroller/api-1577239-signalinterrupt.md)
- [- StartController](./ioscsiparallelinterfacecontroller/api-1577166-startcontroller.md)
- [- StopController](./ioscsiparallelinterfacecontroller/api-1577243-stopcontroller.md)
- [- SuspendServices](./ioscsiparallelinterfacecontroller/api-1577304-suspendservices.md)
- [- TargetResetRequest](./ioscsiparallelinterfacecontroller/api-1577270-targetresetrequest.md)
- [- TerminateController](./ioscsiparallelinterfacecontroller/api-1577155-terminatecontroller.md)
- [- didTerminate](./ioscsiparallelinterfacecontroller/api-1577263-didterminate.md)
- [- free](./ioscsiparallelinterfacecontroller/api-1577225-free.md)
- [- getMetaClass](./ioscsiparallelinterfacecontroller/api-1577254-getmetaclass.md)
- [- getWorkLoop](./ioscsiparallelinterfacecontroller/api-1577197-getworkloop.md)
- [- handleClose](./ioscsiparallelinterfacecontroller/api-1577154-handleclose.md)
- [- handleIsOpen](./ioscsiparallelinterfacecontroller/api-1577303-handleisopen.md)
- [- handleOpen](./ioscsiparallelinterfacecontroller/api-1577182-handleopen.md)
- [- start](./ioscsiparallelinterfacecontroller/api-1577220-start.md)
- [- stop](./ioscsiparallelinterfacecontroller/api-1577287-stop.md)
- [- willTerminate](./ioscsiparallelinterfacecontroller/api-1577238-willterminate.md)
### Type Methods
- [+ FilterInterrupt](./ioscsiparallelinterfacecontroller/api-1577283-filterinterrupt.md)
- [+ ServiceInterrupt](./ioscsiparallelinterfacecontroller/api-1577240-serviceinterrupt.md)
- [+ TimeoutOccurred](./ioscsiparallelinterfacecontroller/api-1577190-timeoutoccurred.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

## See Also

### Multimedia Devices
- [IOSCSILogicalUnitNub](./ioscsilogicalunitnub.md)
- [IOSCSIPeripheralDeviceType05](./ioscsiperipheraldevicetype05.md)
- [IOSCSIMultimediaCommandsDevice](./ioscsimultimediacommandsdevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsiparallelinterfacecontroller)*