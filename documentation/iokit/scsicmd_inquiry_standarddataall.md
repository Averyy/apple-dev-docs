# SCSICmd_INQUIRY_StandardDataAll

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- DriverKit 22.0+
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
typedef struct SCSICmd_INQUIRY_StandardDataAll {
    ...
} SCSICmd_INQUIRY_StandardDataAll;
```

## Overview

This structure defines the all of the fields that can be returned in repsonse to the INQUIRy request for the standard data. There is no requirement as to how much of the additional data must be returned by a device.

## Topics

### Instance Properties
- [ADDITIONAL_LENGTH](./scsicmd_inquiry_standarddataall/api-1572885-additional_length.md)
- [PERIPHERAL_DEVICE_TYPE](./scsicmd_inquiry_standarddataall/api-1572835-peripheral_device_type.md)
- [PRODUCT_IDENTIFICATION](./scsicmd_inquiry_standarddataall/api-1572819-product_identification.md)
- [PRODUCT_REVISION_LEVEL](./scsicmd_inquiry_standarddataall/api-1572956-product_revision_level.md)
- [RESPONSE_DATA_FORMAT](./scsicmd_inquiry_standarddataall/api-1572820-response_data_format.md)
- [RMB](./scsicmd_inquiry_standarddataall/api-1572888-rmb.md)
- [Reserved1](./scsicmd_inquiry_standarddataall/api-1572928-reserved1.md)
- [Reserved2](./scsicmd_inquiry_standarddataall/api-1572918-reserved2.md)
- [SCCSReserved](./scsicmd_inquiry_standarddataall/api-1572797-sccsreserved.md)
- [VENDOR_IDENTIFICATION](./scsicmd_inquiry_standarddataall/api-1572750-vendor_identification.md)
- [VERSION](./scsicmd_inquiry_standarddataall/api-1572883-version.md)
- [VERSION_DESCRIPTOR](./scsicmd_inquiry_standarddataall/api-1572822-version_descriptor.md)
- [VendorSpecific1](./scsicmd_inquiry_standarddataall/api-1572747-vendorspecific1.md)
- [VendorSpecific2](./scsicmd_inquiry_standarddataall/api-1572910-vendorspecific2.md)
- [flags1](./scsicmd_inquiry_standarddataall/api-1572989-flags1.md)
- [flags2](./scsicmd_inquiry_standarddataall/api-1572752-flags2.md)
- [flags3](./scsicmd_inquiry_standarddataall/api-1572979-flags3.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsicmd_inquiry_standarddataall)*