# SCSITaskLib.h

**Framework**: IOKit  
**Role**: API Collection

SCSITaskLib implements non-kernel task access to specific IOKit object types, namely any SCSI Peripheral Device for which there isn't an in-kernel driver and for authoring devices such as CD-R/W and DVD-R/W drives.

## Overview

### Included Headers

- <IOKit/scsi/SCSITask.h>
- <IOKit/scsi/SCSICommandDefinitions.h>
- <IOKit/scsi/SCSICmds_INQUIRY_Definitions.h>
- <IOKit/scsi/SCSICmds_REQUEST_SENSE_Defs.h>
- <CoreFoundation/CFPlugIn.h>
- <CoreFoundation/CFPlugInCOM.h>
- <IOKit/IOReturn.h>
- <IOKit/IOTypes.h>
- <IOKit/IOCFPlugIn.h>

## Topics

### Callbacks
- [SCSITaskCallbackFunction](./scsitaskcallbackfunction.md)
  Asynchronous callback routine definition.
### Constants
- [Defines](./scsitasklib_h/defines.md)
- [MMCDeviceTrayState](./api-1575419-mmcdevicetraystate.md)
  Used to identify the state of an MMCDevice's tray (if applicable).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitasklib_h)*