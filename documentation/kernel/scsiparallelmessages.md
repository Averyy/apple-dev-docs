# SCSIParallelMessages

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.6+

## Declaration

```swift
enum SCSIParallelMessages : unsigned int {
    ...
};
```

## Topics

### Constants
- [kSCSIParallelMessage_ABORT_TASK](scsiparallelmessages/kscsiparallelmessage_abort_task.md)
- [kSCSIParallelMessage_ABORT_TASK_SET](scsiparallelmessages/kscsiparallelmessage_abort_task_set.md)
- [kSCSIParallelMessage_ACA](scsiparallelmessages/kscsiparallelmessage_aca.md)
- [kSCSIParallelMessage_CLEAR_ACA](scsiparallelmessages/kscsiparallelmessage_clear_aca.md)
- [kSCSIParallelMessage_CLEAR_TASK_SET](scsiparallelmessages/kscsiparallelmessage_clear_task_set.md)
- [kSCSIParallelMessage_DISCONNECT](scsiparallelmessages/kscsiparallelmessage_disconnect.md)
- [kSCSIParallelMessage_EXTENDED_MESSAGE](scsiparallelmessages/kscsiparallelmessage_extended_message.md)
- [kSCSIParallelMessage_HEAD_OF_QUEUE](scsiparallelmessages/kscsiparallelmessage_head_of_queue.md)
- [kSCSIParallelMessage_IDENTIFY](scsiparallelmessages/kscsiparallelmessage_identify.md)
- [kSCSIParallelMessage_IGNORE_WIDE_RESIDUE](scsiparallelmessages/kscsiparallelmessage_ignore_wide_residue.md)
- [kSCSIParallelMessage_INITIATOR_DETECTED_ERROR](scsiparallelmessages/kscsiparallelmessage_initiator_detected_error.md)
- [kSCSIParallelMessage_LINKED_COMMAND_COMPLETE](scsiparallelmessages/kscsiparallelmessage_linked_command_complete.md)
- [kSCSIParallelMessage_LOGICAL_UNIT_RESET](scsiparallelmessages/kscsiparallelmessage_logical_unit_reset.md)
- [kSCSIParallelMessage_MESSAGE_PARITY_ERROR](scsiparallelmessages/kscsiparallelmessage_message_parity_error.md)
- [kSCSIParallelMessage_MESSAGE_REJECT](scsiparallelmessages/kscsiparallelmessage_message_reject.md)
- [kSCSIParallelMessage_MODIFY_DATA_POINTER](scsiparallelmessages/kscsiparallelmessage_modify_data_pointer.md)
- [kSCSIParallelMessage_NO_OPERATION](scsiparallelmessages/kscsiparallelmessage_no_operation.md)
- [kSCSIParallelMessage_ORDERED](scsiparallelmessages/kscsiparallelmessage_ordered.md)
- [kSCSIParallelMessage_PARALLEL_PROTOCOL_REQUEST](scsiparallelmessages/kscsiparallelmessage_parallel_protocol_request.md)
- [kSCSIParallelMessage_QAS_REQUEST](scsiparallelmessages/kscsiparallelmessage_qas_request.md)
- [kSCSIParallelMessage_RESTORE_POINTERS](scsiparallelmessages/kscsiparallelmessage_restore_pointers.md)
- [kSCSIParallelMessage_SAVE_DATA_POINTER](scsiparallelmessages/kscsiparallelmessage_save_data_pointer.md)
- [kSCSIParallelMessage_SIMPLE](scsiparallelmessages/kscsiparallelmessage_simple.md)
- [kSCSIParallelMessage_SYNCHONOUS_DATA_TRANSFER_REQUEST](scsiparallelmessages/kscsiparallelmessage_synchonous_data_transfer_request.md)
- [kSCSIParallelMessage_TARGET_RESET](scsiparallelmessages/kscsiparallelmessage_target_reset.md)
- [kSCSIParallelMessage_TASK_COMPLETE](scsiparallelmessages/kscsiparallelmessage_task_complete.md)
- [kSCSIParallelMessage_WIDE_DATA_TRANSFER_REQUEST](scsiparallelmessages/kscsiparallelmessage_wide_data_transfer_request.md)

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
- [SCSITaskStatus](scsitaskstatus.md)
  Attributes for task status.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/scsiparallelmessages)*