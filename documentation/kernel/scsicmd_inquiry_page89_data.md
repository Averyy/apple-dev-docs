# SCSICmd_INQUIRY_Page89_Data

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.4+

## Declaration

```c
typedef struct SCSICmd_INQUIRY_Page89_Data SCSICmd_INQUIRY_Page89_Data;
```

#### Discussion

INQUIRY Page 89h data as defined in the SAT 1.0 specification. This section contians all structures and definitions used by the INQUIRY command in response to a request for page 89h - ATA information VPD Page.

## Topics

### Instance Properties
- [ATA_DEVICE_SIGNATURE](./scsicmd_inquiry_page89_data/api-1429226-ata_device_signature.md)
- [COMMAND_CODE](./scsicmd_inquiry_page89_data/api-1429260-command_code.md)
- [IDENTIFY_DATA](./scsicmd_inquiry_page89_data/api-1429261-identify_data.md)
- [PAGE_CODE](./scsicmd_inquiry_page89_data/api-1429489-page_code.md)
- [PAGE_LENGTH](./scsicmd_inquiry_page89_data/api-1429352-page_length.md)
- [PERIPHERAL_DEVICE_TYPE](./scsicmd_inquiry_page89_data/api-1429259-peripheral_device_type.md)
- [Reserved](./scsicmd_inquiry_page89_data/api-1429400-reserved.md)
- [Reserved2](./scsicmd_inquiry_page89_data/api-1429358-reserved2.md)
- [SAT_PRODUCT_IDENTIFICATION](./scsicmd_inquiry_page89_data/api-1429462-sat_product_identification.md)
- [SAT_PRODUCT_REVISION_LEVEL](./scsicmd_inquiry_page89_data/api-1429488-sat_product_revision_level.md)
- [SAT_VENDOR_IDENTIFICATION](./scsicmd_inquiry_page89_data/api-1429421-sat_vendor_identification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/scsicmd_inquiry_page89_data)*