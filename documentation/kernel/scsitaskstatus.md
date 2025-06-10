# SCSITaskStatus

**Framework**: Kernel  
**Kind**: enum

Attributes for task status.

**Availability**:
- DriverKit 20.0+
- macOS 10.0+

## Declaration

```swift
typedef enum SCSITaskStatus SCSITaskStatus;
```

#### Overview

The Task Status represents the completion status of the task which provides the SCSI Application Layer with additional information about how to procede in handling a completed task.

The SCSI Architecture Model specification only defines task status values for when a task completes with a service response of either TASK_COMPLETED or LINK_COMMAND_COMPLETE.

Since additional information will aid in error recovery when a task fails to be completed by a device due to a service response of kSCSIServiceResponse_SERVICE_DELIVERY_OR_TARGET_FAILURE, additional values have been defined that can be returned by the SCSI Protocol Layer to inform the SCSI Application Layer of the cause of the delivery failure.

The Task Status can only be modified by the SCSI Protocol Layer. The SCSI Application Layer can only read the status

## Topics

### Constants
- [kSCSITaskStatus_GOOD](scsitaskstatus/kscsitaskstatus_good.md)
- [kSCSITaskStatus_CHECK_CONDITION](scsitaskstatus/kscsitaskstatus_check_condition.md)
- [kSCSITaskStatus_CONDITION_MET](scsitaskstatus/kscsitaskstatus_condition_met.md)
- [kSCSITaskStatus_BUSY](scsitaskstatus/kscsitaskstatus_busy.md)
- [kSCSITaskStatus_INTERMEDIATE](scsitaskstatus/kscsitaskstatus_intermediate.md)
- [kSCSITaskStatus_INTERMEDIATE_CONDITION_MET](scsitaskstatus/kscsitaskstatus_intermediate_condition_met.md)
- [kSCSITaskStatus_RESERVATION_CONFLICT](scsitaskstatus/kscsitaskstatus_reservation_conflict.md)
- [kSCSITaskStatus_TASK_SET_FULL](scsitaskstatus/kscsitaskstatus_task_set_full.md)
- [kSCSITaskStatus_ACA_ACTIVE](scsitaskstatus/kscsitaskstatus_aca_active.md)
- [kSCSITaskStatus_TaskTimeoutOccurred](scsitaskstatus/kscsitaskstatus_tasktimeoutoccurred.md)
- [kSCSITaskStatus_ProtocolTimeoutOccurred](scsitaskstatus/kscsitaskstatus_protocoltimeoutoccurred.md)
- [kSCSITaskStatus_DeviceNotResponding](scsitaskstatus/kscsitaskstatus_devicenotresponding.md)
- [kSCSITaskStatus_DeviceNotPresent](scsitaskstatus/kscsitaskstatus_devicenotpresent.md)
- [kSCSITaskStatus_DeliveryFailure](scsitaskstatus/kscsitaskstatus_deliveryfailure.md)
- [kSCSITaskStatus_No_Status](scsitaskstatus/kscsitaskstatus_no_status.md)
- [kSCSITaskStatus_ACA_ACTIVE](../driverkit/scsitaskstatus/kscsitaskstatus_aca_active.md)
- [kSCSITaskStatus_BUSY](../driverkit/scsitaskstatus/kscsitaskstatus_busy.md)
- [kSCSITaskStatus_CHECK_CONDITION](../driverkit/scsitaskstatus/kscsitaskstatus_check_condition.md)
- [kSCSITaskStatus_CONDITION_MET](../driverkit/scsitaskstatus/kscsitaskstatus_condition_met.md)
- [kSCSITaskStatus_DeliveryFailure](../driverkit/scsitaskstatus/kscsitaskstatus_deliveryfailure.md)
- [kSCSITaskStatus_DeviceNotPresent](../driverkit/scsitaskstatus/kscsitaskstatus_devicenotpresent.md)
- [kSCSITaskStatus_DeviceNotResponding](../driverkit/scsitaskstatus/kscsitaskstatus_devicenotresponding.md)
- [kSCSITaskStatus_GOOD](../driverkit/scsitaskstatus/kscsitaskstatus_good.md)
- [kSCSITaskStatus_INTERMEDIATE](../driverkit/scsitaskstatus/kscsitaskstatus_intermediate.md)
- [kSCSITaskStatus_INTERMEDIATE_CONDITION_MET](../driverkit/scsitaskstatus/kscsitaskstatus_intermediate_condition_met.md)
- [kSCSITaskStatus_No_Status](../driverkit/scsitaskstatus/kscsitaskstatus_no_status.md)
- [kSCSITaskStatus_ProtocolTimeoutOccurred](../driverkit/scsitaskstatus/kscsitaskstatus_protocoltimeoutoccurred.md)
- [kSCSITaskStatus_RESERVATION_CONFLICT](../driverkit/scsitaskstatus/kscsitaskstatus_reservation_conflict.md)
- [kSCSITaskStatus_TASK_SET_FULL](../driverkit/scsitaskstatus/kscsitaskstatus_task_set_full.md)
- [kSCSITaskStatus_TaskTimeoutOccurred](../driverkit/scsitaskstatus/kscsitaskstatus_tasktimeoutoccurred.md)

## See Also

- [SCSICmd_INQUIRY_PAGECx_Header](scsicmd_inquiry_pagecx_header.md)
- [SCSICmd_INQUIRY_Page00_Header_SPC_16](scsicmd_inquiry_page00_header_spc_16.md)
- [SCSICmd_INQUIRY_Page80_Header_SPC_16](scsicmd_inquiry_page80_header_spc_16.md)
- [SCSICmd_INQUIRY_PageB0_Data](scsicmd_inquiry_pageb0_data.md)
- [SCSICmd_INQUIRY_PageB2_Data](scsicmd_inquiry_pageb2_data.md)
- [SCSICmd_INQUIRY_PageB2_Provisioning_Group_Descriptor](scsicmd_inquiry_pageb2_provisioning_group_descriptor.md)
- [SCSICmd_INQUIRY_PageC0_Data](scsicmd_inquiry_pagec0_data.md)
- [SCSICmd_INQUIRY_PageC1_Data](scsicmd_inquiry_pagec1_data.md)
- [SCSICmd_INQUIRY_StandardDataPtr](scsicmd_inquiry_standarddataptr.md)
- [SCSICmd_REPORT_LUNS_Header](scsicmd_report_luns_header.md)
- [SCSICmd_REPORT_LUNS_LUN_ENTRY](scsicmd_report_luns_lun_entry.md)
- [SCSICommandDescriptorBlock](scsicommanddescriptorblock.md)
- [SCSIDeviceIdentifier](scsideviceidentifier.md)
  64-bit number to represent a SCSI Device.
- [SCSIInitiatorIdentifier](scsiinitiatoridentifier.md)
  64-bit number to represent a SCSI Initiator Device.
- [SCSILogicalUnitBytes](scsilogicalunitbytes.md)
- [SCSILogicalUnitNumber](scsilogicalunitnumber.md)
- [SCSIParallelMessages](scsiparallelmessages.md)
- [SCSIParallelTaskIdentifier](scsiparalleltaskidentifier.md)
- [SCSIPortStatus](scsiportstatus.md)
  32-bit number to represent a SCSIPortStatus.
- [SCSIProtocolFeature](scsiprotocolfeature.md)
- [SCSIProtocolPowerState](scsiprotocolpowerstate.md)
- [SCSIServiceResponse](scsiserviceresponse.md)
  Attributes for task service response.
- [SCSITaggedTaskIdentifier](scsitaggedtaskidentifier.md)
  64-bit number to represent a unique task identifier.
- [SCSITargetIdentifier](scsitargetidentifier.md)
  64-bit number to represent a SCSI Target Device.
- [SCSITaskAttribute](scsitaskattribute.md)
  Attributes for task delivery.
- [SCSITaskState](scsitaskstate.md)
  Attributes for task state.
- [SCSI_Sense_Data](scsi_sense_data.md)
- [SCSICmdField10Bit](scsicmdfield10bit.md)
- [SCSICmdField11Bit](scsicmdfield11bit.md)
- [SCSICmdField12Bit](scsicmdfield12bit.md)
- [SCSICmdField13Bit](scsicmdfield13bit.md)
- [SCSICmdField14Bit](scsicmdfield14bit.md)
- [SCSICmdField15Bit](scsicmdfield15bit.md)
- [SCSICmdField17Bit](scsicmdfield17bit.md)
- [SCSICmdField18Bit](scsicmdfield18bit.md)
- [SCSICmdField19Bit](scsicmdfield19bit.md)
- [SCSICmdField1Bit](scsicmdfield1bit.md)
- [SCSICmdField1Byte](scsicmdfield1byte.md)
- [SCSICmdField20Bit](scsicmdfield20bit.md)
- [SCSICmdField21Bit](scsicmdfield21bit.md)
- [SCSICmdField22Bit](scsicmdfield22bit.md)
- [SCSICmdField23Bit](scsicmdfield23bit.md)
- [SCSICmdField25Bit](scsicmdfield25bit.md)
- [SCSICmdField26Bit](scsicmdfield26bit.md)
- [SCSICmdField27Bit](scsicmdfield27bit.md)
- [SCSICmdField28Bit](scsicmdfield28bit.md)
- [SCSICmdField29Bit](scsicmdfield29bit.md)
- [SCSICmdField2Bit](scsicmdfield2bit.md)
- [SCSICmdField2Byte](scsicmdfield2byte.md)
- [SCSICmdField30Bit](scsicmdfield30bit.md)
- [SCSICmdField31Bit](scsicmdfield31bit.md)
- [SCSICmdField33Bit](scsicmdfield33bit.md)
- [SCSICmdField34Bit](scsicmdfield34bit.md)
- [SCSICmdField35Bit](scsicmdfield35bit.md)
- [SCSICmdField36Bit](scsicmdfield36bit.md)
- [SCSICmdField37Bit](scsicmdfield37bit.md)
- [SCSICmdField38Bit](scsicmdfield38bit.md)
- [SCSICmdField39Bit](scsicmdfield39bit.md)
- [SCSICmdField3Bit](scsicmdfield3bit.md)
- [SCSICmdField3Byte](scsicmdfield3byte.md)
- [SCSICmdField41Bit](scsicmdfield41bit.md)
- [SCSICmdField42Bit](scsicmdfield42bit.md)
- [SCSICmdField43Bit](scsicmdfield43bit.md)
- [SCSICmdField44Bit](scsicmdfield44bit.md)
- [SCSICmdField45Bit](scsicmdfield45bit.md)
- [SCSICmdField46Bit](scsicmdfield46bit.md)
- [SCSICmdField47Bit](scsicmdfield47bit.md)
- [SCSICmdField49Bit](scsicmdfield49bit.md)
- [SCSICmdField4Bit](scsicmdfield4bit.md)
- [SCSICmdField4Byte](scsicmdfield4byte.md)
- [SCSICmdField50Bit](scsicmdfield50bit.md)
- [SCSICmdField51Bit](scsicmdfield51bit.md)
- [SCSICmdField52Bit](scsicmdfield52bit.md)
- [SCSICmdField53Bit](scsicmdfield53bit.md)
- [SCSICmdField54Bit](scsicmdfield54bit.md)
- [SCSICmdField55Bit](scsicmdfield55bit.md)
- [SCSICmdField57Bit](scsicmdfield57bit.md)
- [SCSICmdField58Bit](scsicmdfield58bit.md)
- [SCSICmdField59Bit](scsicmdfield59bit.md)
- [SCSICmdField5Bit](scsicmdfield5bit.md)
- [SCSICmdField5Byte](scsicmdfield5byte.md)
- [SCSICmdField60Bit](scsicmdfield60bit.md)
- [SCSICmdField61Bit](scsicmdfield61bit.md)
- [SCSICmdField62Bit](scsicmdfield62bit.md)
- [SCSICmdField63Bit](scsicmdfield63bit.md)
- [SCSICmdField6Bit](scsicmdfield6bit.md)
- [SCSICmdField6Byte](scsicmdfield6byte.md)
- [SCSICmdField7Bit](scsicmdfield7bit.md)
- [SCSICmdField7Byte](scsicmdfield7byte.md)
- [SCSICmdField8Byte](scsicmdfield8byte.md)
- [SCSICmdField9Bit](scsicmdfield9bit.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/scsitaskstatus)*