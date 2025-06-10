# SCSI_Sense_Data

**Framework**: Kernel  
**Kind**: struct

**Availability**:
- DriverKit 20.0+
- macOS 10.0+

## Declaration

```swift
typedef struct SCSI_Sense_Data SCSI_Sense_Data;
```

#### Overview

The basic SCSI Request Sense data structure.

## Topics

### Instance Properties
- [ADDITIONAL_SENSE_CODE](scsi_sense_data/1410601-additional_sense_code.md)
- [ADDITIONAL_SENSE_CODE_QUALIFIER](scsi_sense_data/1410609-additional_sense_code_qualifier.md)
- [ADDITIONAL_SENSE_LENGTH](scsi_sense_data/1410578-additional_sense_length.md)
- [COMMAND_SPECIFIC_INFORMATION_1](scsi_sense_data/1410558-command_specific_information_1.md)
- [COMMAND_SPECIFIC_INFORMATION_2](scsi_sense_data/1410622-command_specific_information_2.md)
- [COMMAND_SPECIFIC_INFORMATION_3](scsi_sense_data/1410554-command_specific_information_3.md)
- [COMMAND_SPECIFIC_INFORMATION_4](scsi_sense_data/1410589-command_specific_information_4.md)
- [FIELD_REPLACEABLE_UNIT_CODE](scsi_sense_data/1410598-field_replaceable_unit_code.md)
- [INFORMATION_1](scsi_sense_data/1410596-information_1.md)
- [INFORMATION_2](scsi_sense_data/1410556-information_2.md)
- [INFORMATION_3](scsi_sense_data/1410605-information_3.md)
- [INFORMATION_4](scsi_sense_data/1410625-information_4.md)
- [SEGMENT_NUMBER](scsi_sense_data/1410607-segment_number.md)
- [SENSE_KEY](scsi_sense_data/1410611-sense_key.md)
- [SENSE_KEY_SPECIFIC_LSB](scsi_sense_data/1410564-sense_key_specific_lsb.md)
- [SENSE_KEY_SPECIFIC_MID](scsi_sense_data/1410587-sense_key_specific_mid.md)
- [SKSV_SENSE_KEY_SPECIFIC_MSB](scsi_sense_data/1410599-sksv_sense_key_specific_msb.md)
- [VALID_RESPONSE_CODE](scsi_sense_data/1410580-valid_response_code.md)
- [ADDITIONAL_SENSE_CODE](../driverkit/scsi_sense_data/3583320-additional_sense_code.md)
- [ADDITIONAL_SENSE_CODE_QUALIFIER](../driverkit/scsi_sense_data/3583321-additional_sense_code_qualifier.md)
- [ADDITIONAL_SENSE_LENGTH](../driverkit/scsi_sense_data/3583322-additional_sense_length.md)
- [COMMAND_SPECIFIC_INFORMATION_1](../driverkit/scsi_sense_data/3583323-command_specific_information_1.md)
- [COMMAND_SPECIFIC_INFORMATION_2](../driverkit/scsi_sense_data/3583324-command_specific_information_2.md)
- [COMMAND_SPECIFIC_INFORMATION_3](../driverkit/scsi_sense_data/3583325-command_specific_information_3.md)
- [COMMAND_SPECIFIC_INFORMATION_4](../driverkit/scsi_sense_data/3583326-command_specific_information_4.md)
- [FIELD_REPLACEABLE_UNIT_CODE](../driverkit/scsi_sense_data/3583327-field_replaceable_unit_code.md)
- [INFORMATION_1](../driverkit/scsi_sense_data/3583328-information_1.md)
- [INFORMATION_2](../driverkit/scsi_sense_data/3583329-information_2.md)
- [INFORMATION_3](../driverkit/scsi_sense_data/3583330-information_3.md)
- [INFORMATION_4](../driverkit/scsi_sense_data/3583331-information_4.md)
- [SEGMENT_NUMBER](../driverkit/scsi_sense_data/3583332-segment_number.md)
- [SENSE_KEY](../driverkit/scsi_sense_data/3583333-sense_key.md)
- [SENSE_KEY_SPECIFIC_LSB](../driverkit/scsi_sense_data/3583334-sense_key_specific_lsb.md)
- [SENSE_KEY_SPECIFIC_MID](../driverkit/scsi_sense_data/3583335-sense_key_specific_mid.md)
- [SKSV_SENSE_KEY_SPECIFIC_MSB](../driverkit/scsi_sense_data/3583336-sksv_sense_key_specific_msb.md)
- [VALID_RESPONSE_CODE](../driverkit/scsi_sense_data/3583337-valid_response_code.md)

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
- [SCSITaskStatus](scsitaskstatus.md)
  Attributes for task status.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/scsi_sense_data)*