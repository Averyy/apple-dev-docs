# Byte 56 features field definitions

**Framework**: IOKit  
**Kind**: enum

## Declaration

```c
enum {
   // Byte offset
   kINQUIRY_Byte56_Offset = 56,
   // Bit definitions
   kINQUIRY_Byte56_IUS_Bit = 0,
   kINQUIRY_Byte56_QAS_Bit = 1,
   // Bits 2 and 3 are the CLOCKING bits
   // All other bits are reserved
   kINQUIRY_Byte56_IUS_Mask = (
   1 << kINQUIRY_Byte56_IUS_Bit),
   kINQUIRY_Byte56_QAS_Mask = (
   1 << kINQUIRY_Byte56_QAS_Bit),
   kINQUIRY_Byte56_CLOCKING_Mask = 0x0C,
   // Definitions for the CLOCKING bits
   kINQUIRY_Byte56_CLOCKING_ONLY_ST = 0x00,
   kINQUIRY_Byte56_CLOCKING_ONLY_DT = 0x04,
   // kINQUIRY_Byte56_CLOCKING_RESERVED        = 0x08,
   kINQUIRY_Byte56_CLOCKING_ST_AND_DT = 0x0C
};
```

#### Overview

Definitions for bits/masks in the INQUIRY Byte 56 field. Inquiry Byte 56 features (for devices that report an ANSI VERSION of kINQUIRY_ANSI_VERSION_SCSI_SPC_Compliant or later). These are SPI-3 Specific.

## Topics

### Constants
- [kINQUIRY_Byte56_IUS_Bit](../../kernel/api-1643292-anonymous/kinquiry_byte56_ius_bit.md)
- [kINQUIRY_Byte56_QAS_Bit](../../kernel/api-1643292-anonymous/kinquiry_byte56_qas_bit.md)
- [kINQUIRY_Byte56_IUS_Mask](../../kernel/api-1643292-anonymous/kinquiry_byte56_ius_mask.md)
- [kINQUIRY_Byte56_QAS_Mask](../../kernel/api-1643292-anonymous/kinquiry_byte56_qas_mask.md)
- [kINQUIRY_Byte56_CLOCKING_Mask](../../kernel/api-1643292-anonymous/kinquiry_byte56_clocking_mask.md)
- [kINQUIRY_Byte56_CLOCKING_ONLY_ST](../../kernel/api-1643292-anonymous/kinquiry_byte56_clocking_only_st.md)
- [kINQUIRY_Byte56_CLOCKING_ONLY_DT](../../kernel/api-1643292-anonymous/kinquiry_byte56_clocking_only_dt.md)
- [kINQUIRY_Byte56_CLOCKING_ST_AND_DT](../../kernel/api-1643292-anonymous/kinquiry_byte56_clocking_st_and_dt.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsicmds_inquiry_definitions_h_user-space/byte_56_features_field_definitions)*