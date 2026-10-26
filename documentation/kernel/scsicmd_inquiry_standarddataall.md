# SCSICmd_INQUIRY_StandardDataAll

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.2+

## Declaration

```c
typedef struct SCSICmd_INQUIRY_StandardDataAll SCSICmd_INQUIRY_StandardDataAll;
```

#### Discussion

This structure defines the all of the fields that can be returned in repsonse to the INQUIRy request for the standard data. There is no requirement as to how much of the additional data must be returned by a device.

## Topics

### Instance Properties
- [ADDITIONAL_LENGTH](./scsicmd_inquiry_standarddataall/api-1429183-additional_length.md)
- [PERIPHERAL_DEVICE_TYPE](./scsicmd_inquiry_standarddataall/api-1429263-peripheral_device_type.md)
- [PRODUCT_IDENTIFICATION](./scsicmd_inquiry_standarddataall/api-1429277-product_identification.md)
- [PRODUCT_REVISION_LEVEL](./scsicmd_inquiry_standarddataall/api-1429427-product_revision_level.md)
- [RESPONSE_DATA_FORMAT](./scsicmd_inquiry_standarddataall/api-1429491-response_data_format.md)
- [RMB](./scsicmd_inquiry_standarddataall/api-1429472-rmb.md)
- [Reserved1](./scsicmd_inquiry_standarddataall/api-1429255-reserved1.md)
- [Reserved2](./scsicmd_inquiry_standarddataall/api-1429447-reserved2.md)
- [SCCSReserved](./scsicmd_inquiry_standarddataall/api-1429409-sccsreserved.md)
- [VENDOR_IDENTIFICATION](./scsicmd_inquiry_standarddataall/api-1429224-vendor_identification.md)
- [VERSION](./scsicmd_inquiry_standarddataall/api-1429432-version.md)
- [VERSION_DESCRIPTOR](./scsicmd_inquiry_standarddataall/api-1429360-version_descriptor.md)
- [VendorSpecific1](./scsicmd_inquiry_standarddataall/api-1429494-vendorspecific1.md)
- [VendorSpecific2](./scsicmd_inquiry_standarddataall/api-1429127-vendorspecific2.md)
- [flags1](./scsicmd_inquiry_standarddataall/api-1429301-flags1.md)
- [flags2](./scsicmd_inquiry_standarddataall/api-1429450-flags2.md)
- [flags3](./scsicmd_inquiry_standarddataall/api-1429157-flags3.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/scsicmd_inquiry_standarddataall)*