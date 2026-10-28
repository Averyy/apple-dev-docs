# SCSITask.h User-Space

**Framework**: IOKit  
**Role**: API Collection

## Overview

SCSITask typedefs and constants used inside the kernel and user space.

Note that the SCSITaskIdentifier is an opaque object and that directly casting the SCSITaskIdentifier to any other type is discouraged. The SCSITask implementation changes when necessary to accomodate architectural changes, performance improvements, and bug fixes.

Device and protocol layer drivers that need to access information contained in a SCSITask should use the appropriate accessor methods in IOSCSIPrimaryCommandsDevice.h or IOSCSIProtocolServices.h

### Included Headers

- <IOKit/IOTypes.h>
- <CoreFoundation/CoreFoundation.h>
- <libkern/c++/OSObject.h>

## Topics

### Callbacks
- [SCSITaskCompletion](../kernel/scsitaskcompletion.md)
### Data Types
- [SCSIDeviceIdentifier](./scsideviceidentifier.md)
  64-bit number to represent a SCSI Device.
- [SCSIInitiatorIdentifier](./scsiinitiatoridentifier.md)
  64-bit number to represent a SCSI Initiator Device.
- [SCSIServiceResponse](./scsiserviceresponse.md)
  Attributes for task service response.
- [SCSITaggedTaskIdentifier](./scsitaggedtaskidentifier.md)
  64-bit number to represent a unique task identifier.
- [SCSITargetIdentifier](./scsitargetidentifier.md)
  64-bit number to represent a SCSI Target Device.
- [SCSITaskAttribute](./scsitaskattribute.md)
  Attributes for task delivery.
- [SCSITaskIdentifier](../kernel/scsitaskidentifier.md)
- [SCSITaskMode](../kernel/scsitaskmode.md)
- [SCSITaskState](./scsitaskstate.md)
  Attributes for task state.
- [SCSITaskStatus](./scsitaskstatus.md)
  Attributes for task status.
### Constants
- [Command Descriptor Block Size](./api-1534764-command_descriptor_block_size.md)
- [Data Transfer Direction](./api-1534749-data_transfer_direction.md)
- [Untagged Task Identifier](./api-1534776-untagged_task_identifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitask_h_user-space)*