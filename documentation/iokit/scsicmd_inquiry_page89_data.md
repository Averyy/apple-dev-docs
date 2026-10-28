# SCSICmd_INQUIRY_Page89_Data

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- DriverKit 22.0+
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```c
typedef struct SCSICmd_INQUIRY_Page89_Data {
    ...
} SCSICmd_INQUIRY_Page89_Data;
```

## Overview

INQUIRY Page 89h data as defined in the SAT 1.0 specification. This section contians all structures and definitions used by the INQUIRY command in response to a request for page 89h - ATA information VPD Page.

## Topics

### Instance Properties
- [ATA_DEVICE_SIGNATURE](./scsicmd_inquiry_page89_data/api-1572806-ata_device_signature.md)
- [COMMAND_CODE](./scsicmd_inquiry_page89_data/api-1572929-command_code.md)
- [IDENTIFY_DATA](./scsicmd_inquiry_page89_data/api-1573004-identify_data.md)
- [PAGE_CODE](./scsicmd_inquiry_page89_data/api-1572923-page_code.md)
- [PAGE_LENGTH](./scsicmd_inquiry_page89_data/api-1572970-page_length.md)
- [PERIPHERAL_DEVICE_TYPE](./scsicmd_inquiry_page89_data/api-1572907-peripheral_device_type.md)
- [Reserved](./scsicmd_inquiry_page89_data/api-1572877-reserved.md)
- [Reserved2](./scsicmd_inquiry_page89_data/api-1572982-reserved2.md)
- [SAT_PRODUCT_IDENTIFICATION](./scsicmd_inquiry_page89_data/api-1572754-sat_product_identification.md)
- [SAT_PRODUCT_REVISION_LEVEL](./scsicmd_inquiry_page89_data/api-1572921-sat_product_revision_level.md)
- [SAT_VENDOR_IDENTIFICATION](./scsicmd_inquiry_page89_data/api-1572768-sat_vendor_identification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsicmd_inquiry_page89_data)*