# SCSICmd_INQUIRY_StandardData

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- DriverKit 22.0+
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typedef struct SCSICmd_INQUIRY_StandardData {
    ...
} SCSICmd_INQUIRY_StandardData;
```

## Overview

This structure defines the format of the required standard data that is returned for the INQUIRY command. This is the data that is required to be returned from all devices.

## Topics

### Instance Properties
- [ADDITIONAL_LENGTH](./scsicmd_inquiry_standarddata/api-1572999-additional_length.md)
- [PERIPHERAL_DEVICE_TYPE](./scsicmd_inquiry_standarddata/api-1572933-peripheral_device_type.md)
- [PRODUCT_IDENTIFICATION](./scsicmd_inquiry_standarddata/api-1572860-product_identification.md)
- [PRODUCT_REVISION_LEVEL](./scsicmd_inquiry_standarddata/api-1572912-product_revision_level.md)
- [RESPONSE_DATA_FORMAT](./scsicmd_inquiry_standarddata/api-1572816-response_data_format.md)
- [RMB](./scsicmd_inquiry_standarddata/api-1572998-rmb.md)
- [SCCSReserved](./scsicmd_inquiry_standarddata/api-1572939-sccsreserved.md)
- [VENDOR_IDENTIFICATION](./scsicmd_inquiry_standarddata/api-1572748-vendor_identification.md)
- [VERSION](./scsicmd_inquiry_standarddata/api-1573008-version.md)
- [flags1](./scsicmd_inquiry_standarddata/api-1572993-flags1.md)
- [flags2](../kernel/scsicmd_inquiry_standarddata/api-1429411-flags2.md)
- [flags2](./scsicmd_inquiry_standarddata/api-1572967-flags2.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsicmd_inquiry_standarddata)*