# flags1 field definitions

**Framework**: IOKit  
**Kind**: enum

## Declaration

```c
enum {
   // Byte offset
   kINQUIRY_Byte6_Offset = 6,
   // Bit definitions
   kINQUIRY_Byte6_ADDR16_Bit = 0, // SPI Specific
   // Bit 1 is Obsolete
   // Bit 2 is Obsolete
   kINQUIRY_Byte6_MCHNGR_Bit = 3,
   kINQUIRY_Byte6_MULTIP_Bit = 4,
   kINQUIRY_Byte6_VS_Bit = 5,
   kINQUIRY_Byte6_ENCSERV_Bit = 6,
   kINQUIRY_Byte6_BQUE_Bit = 7,
   // Masks
   kINQUIRY_Byte6_ADDR16_Mask = (
   1 << kINQUIRY_Byte6_ADDR16_Bit), // SPI Specific
   // Bit 1 is Obsolete
   // Bit 2 is Obsolete
   kINQUIRY_Byte6_MCHNGR_Mask = (
   1 << kINQUIRY_Byte6_MCHNGR_Bit),
   kINQUIRY_Byte6_MULTIP_Mask = (
   1 << kINQUIRY_Byte6_MULTIP_Bit),
   kINQUIRY_Byte6_VS_Mask = (
   1 << kINQUIRY_Byte6_VS_Bit),
   kINQUIRY_Byte6_ENCSERV_Mask = (
   1 << kINQUIRY_Byte6_ENCSERV_Bit),
   kINQUIRY_Byte6_BQUE_Mask = (
   1 << kINQUIRY_Byte6_BQUE_Bit)
};
```

#### Overview

Definitions for bits/masks in the INQUIRY flags1 field.

## Topics

### Constants
- [kINQUIRY_Byte6_ADDR16_Bit](../../kernel/api-1643288-anonymous/kinquiry_byte6_addr16_bit.md)
- [kINQUIRY_Byte6_MCHNGR_Bit](../../kernel/api-1643288-anonymous/kinquiry_byte6_mchngr_bit.md)
- [kINQUIRY_Byte6_MULTIP_Bit](../../kernel/api-1643288-anonymous/kinquiry_byte6_multip_bit.md)
- [kINQUIRY_Byte6_VS_Bit](../../kernel/api-1643288-anonymous/kinquiry_byte6_vs_bit.md)
- [kINQUIRY_Byte6_ENCSERV_Bit](../../kernel/api-1643288-anonymous/kinquiry_byte6_encserv_bit.md)
- [kINQUIRY_Byte6_BQUE_Bit](../../kernel/api-1643288-anonymous/kinquiry_byte6_bque_bit.md)
- [kINQUIRY_Byte6_ADDR16_Mask](../../kernel/api-1643288-anonymous/kinquiry_byte6_addr16_mask.md)
- [kINQUIRY_Byte6_MCHNGR_Mask](../../kernel/api-1643288-anonymous/kinquiry_byte6_mchngr_mask.md)
- [kINQUIRY_Byte6_MULTIP_Mask](../../kernel/api-1643288-anonymous/kinquiry_byte6_multip_mask.md)
- [kINQUIRY_Byte6_VS_Mask](../../kernel/api-1643288-anonymous/kinquiry_byte6_vs_mask.md)
- [kINQUIRY_Byte6_ENCSERV_Mask](../../kernel/api-1643288-anonymous/kinquiry_byte6_encserv_mask.md)
- [kINQUIRY_Byte6_BQUE_Mask](../../kernel/api-1643288-anonymous/kinquiry_byte6_bque_mask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsicmds_inquiry_definitions_h_user-space/flags1_field_definitions)*