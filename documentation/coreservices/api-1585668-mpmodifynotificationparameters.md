# MPModifyNotificationParameters

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.1+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPModifyNotificationParameters(MPNotificationID notificationID, MPOpaqueIDClass kind, void *notifyParam1, void *notifyParam2, void *notifyParam3);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

## See Also

### Handling Kernel Notifications
- [MPCauseNotification](./api-1585754-mpcausenotification.md)
  Signals a kernel notification. 
- [MPCreateNotification](./api-1585723-mpcreatenotification.md)
  Creates a kernel notification
- [MPDeleteNotification](./api-1585659-mpdeletenotification.md)
  Removes a kernel notification. 
- [MPModifyNotification](./api-1585780-mpmodifynotification.md)
  Adds a simple notification to a kernel notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585668-mpmodifynotificationparameters)*