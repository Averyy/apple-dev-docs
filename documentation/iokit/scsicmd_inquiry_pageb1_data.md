# SCSICmd_INQUIRY_PageB1_Data

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- DriverKit 22.0+
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
typedef struct SCSICmd_INQUIRY_PageB1_Data {
    ...
} SCSICmd_INQUIRY_PageB1_Data;
```

## Overview

INQUIRY Page B1h data as defined in the SBC specification. This section contians all structures and definitions used by the INQUIRY command in response to a request for page B1h - Block Device Characteristics VPD Page.

## Topics

### Instance Properties
- [MEDIUM_ROTATION_RATE](../kernel/scsicmd_inquiry_pageb1_data/api-1429339-medium_rotation_rate.md)
- [MEDIUM_ROTATION_RATE](./scsicmd_inquiry_pageb1_data/api-1572818-medium_rotation_rate.md)
- [PAGE_CODE](./scsicmd_inquiry_pageb1_data/api-1572798-page_code.md)
- [PAGE_LENGTH](./scsicmd_inquiry_pageb1_data/api-1572920-page_length.md)
- [PERIPHERAL_DEVICE_TYPE](./scsicmd_inquiry_pageb1_data/api-1572887-peripheral_device_type.md)
- [Reserved](./scsicmd_inquiry_pageb1_data/api-1572882-reserved.md)
- [Reserved2](./scsicmd_inquiry_pageb1_data/api-1573012-reserved2.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsicmd_inquiry_pageb1_data)*