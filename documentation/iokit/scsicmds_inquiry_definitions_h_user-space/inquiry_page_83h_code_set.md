# INQUIRY Page 83h Code Set

**Framework**: IOKit  
**Kind**: enum

## Declaration

```c
enum {
   kINQUIRY_Page83_CodeSetReserved = 0x0,
   kINQUIRY_Page83_CodeSetBinaryData = 0x1,
   kINQUIRY_Page83_CodeSetASCIIData = 0x2,
   kINQUIRY_Page83_CodeSetUTF8Data = 0x3,
   // 0x4 - 0xF reserved
   kINQUIRY_Page83_CodeSetMask = 0xF
};
```

#### Overview

Definitions for the Code Set field.

## Topics

### Constants
- [kINQUIRY_Page83_CodeSetBinaryData](../../kernel/api-1643303-anonymous/kinquiry_page83_codesetbinarydata.md)
- [kINQUIRY_Page83_CodeSetASCIIData](../../kernel/api-1643303-anonymous/kinquiry_page83_codesetasciidata.md)
- [kINQUIRY_Page83_CodeSetUTF8Data](../../kernel/api-1643303-anonymous/kinquiry_page83_codesetutf8data.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsicmds_inquiry_definitions_h_user-space/inquiry_page_83h_code_set)*