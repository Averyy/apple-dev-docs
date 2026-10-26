# SCSIServiceResponse

**Framework**: IOKit  
**Kind**: enum  
**Role**: Enumeration

Attributes for task service response.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typedef enum SCSIServiceResponse : unsigned int {
    ...
} SCSIServiceResponse;
```

#### Overview

The Service Response represents the execution status of a service request made to a Protocol Services Driver. The Service Response can only be modified by the SCSI Protocol Layer. The SCSI Application Layer can only read the state.

## Topics

### Constants
- [kSCSIServiceResponse_Request_In_Process](./scsiserviceresponse/kscsiserviceresponse_request_in_process.md)
- [kSCSIServiceResponse_SERVICE_DELIVERY_OR_TARGET_FAILURE](./scsiserviceresponse/kscsiserviceresponse_service_delivery_or_target_failure.md)
- [kSCSIServiceResponse_TASK_COMPLETE](./scsiserviceresponse/kscsiserviceresponse_task_complete.md)
- [kSCSIServiceResponse_LINK_COMMAND_COMPLETE](./scsiserviceresponse/kscsiserviceresponse_link_command_complete.md)
- [kSCSIServiceResponse_FUNCTION_COMPLETE](./scsiserviceresponse/kscsiserviceresponse_function_complete.md)
- [kSCSIServiceResponse_FUNCTION_REJECTED](./scsiserviceresponse/kscsiserviceresponse_function_rejected.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsiserviceresponse)*