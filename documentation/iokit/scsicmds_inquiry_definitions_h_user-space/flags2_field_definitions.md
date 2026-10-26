# flags2 field definitions

**Framework**: IOKit  
**Kind**: enum

## Declaration

```c
enum {
   // Byte offset
   kINQUIRY_Byte7_Offset = 7,
   // Bit definitions
   kINQUIRY_Byte7_VS_Bit = 0,
   kINQUIRY_Byte7_CMDQUE_Bit = 1,
   kINQUIRY_Byte7_TRANDIS_Bit = 2, // SPI Specific
   kINQUIRY_Byte7_LINKED_Bit = 3,
   kINQUIRY_Byte7_SYNC_Bit = 4, // SPI Specific
   kINQUIRY_Byte7_WBUS16_Bit = 5, // SPI Specific
   // Bit 6 is Obsolete
   kINQUIRY_Byte7_RELADR_Bit = 7,
   // Masks
   kINQUIRY_Byte7_VS_Mask = (
   1 << kINQUIRY_Byte7_VS_Bit),
   kINQUIRY_Byte7_CMDQUE_Mask = (
   1 << kINQUIRY_Byte7_CMDQUE_Bit),
   kINQUIRY_Byte7_TRANDIS_Mask = (
   1 << kINQUIRY_Byte7_TRANDIS_Bit),// SPI Specific
   kINQUIRY_Byte7_LINKED_Mask = (
   1 << kINQUIRY_Byte7_LINKED_Bit),
   kINQUIRY_Byte7_SYNC_Mask = (
   1 << kINQUIRY_Byte7_SYNC_Bit), // SPI Specific
   kINQUIRY_Byte7_WBUS16_Mask = (
   1 << kINQUIRY_Byte7_WBUS16_Bit), // SPI Specific
   // Bit 6 is Obsolete
   kINQUIRY_Byte7_RELADR_Mask = (
   1 << kINQUIRY_Byte7_RELADR_Bit)
};
```

#### Overview

Definitions for bits/masks in the INQUIRY flags2 field.

## Topics

### Constants
- [kINQUIRY_Byte7_VS_Bit](../../kernel/api-1643309-anonymous/kinquiry_byte7_vs_bit.md)
- [kINQUIRY_Byte7_CMDQUE_Bit](../../kernel/api-1643309-anonymous/kinquiry_byte7_cmdque_bit.md)
- [kINQUIRY_Byte7_TRANDIS_Bit](../../kernel/api-1643309-anonymous/kinquiry_byte7_trandis_bit.md)
- [kINQUIRY_Byte7_LINKED_Bit](../../kernel/api-1643309-anonymous/kinquiry_byte7_linked_bit.md)
- [kINQUIRY_Byte7_SYNC_Bit](../../kernel/api-1643309-anonymous/kinquiry_byte7_sync_bit.md)
- [kINQUIRY_Byte7_WBUS16_Bit](../../kernel/api-1643309-anonymous/kinquiry_byte7_wbus16_bit.md)
- [kINQUIRY_Byte7_RELADR_Bit](../../kernel/api-1643309-anonymous/kinquiry_byte7_reladr_bit.md)
- [kINQUIRY_Byte7_VS_Mask](../../kernel/api-1643309-anonymous/kinquiry_byte7_vs_mask.md)
- [kINQUIRY_Byte7_CMDQUE_Mask](../../kernel/api-1643309-anonymous/kinquiry_byte7_cmdque_mask.md)
- [kINQUIRY_Byte7_TRANDIS_Mask](../../kernel/api-1643309-anonymous/kinquiry_byte7_trandis_mask.md)
- [kINQUIRY_Byte7_LINKED_Mask](../../kernel/api-1643309-anonymous/kinquiry_byte7_linked_mask.md)
- [kINQUIRY_Byte7_SYNC_Mask](../../kernel/api-1643309-anonymous/kinquiry_byte7_sync_mask.md)
- [kINQUIRY_Byte7_WBUS16_Mask](../../kernel/api-1643309-anonymous/kinquiry_byte7_wbus16_mask.md)
- [kINQUIRY_Byte7_RELADR_Mask](../../kernel/api-1643309-anonymous/kinquiry_byte7_reladr_mask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsicmds_inquiry_definitions_h_user-space/flags2_field_definitions)*