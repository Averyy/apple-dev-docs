# MPModifyNotification

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Adds a simple notification to a kernel notification.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPModifyNotification(MPNotificationID notificationID, MPOpaqueID anID, void *notifyParam1, void *notifyParam2, void *notifyParam3);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

#### Discussion

You specify the parameters for the simple notifications just as if you were calling the  [`MPSetTimerNotify`](./api-1585726-mpsettimernotify.md)  function.  

## Parameters

- `notificationID`: The ID of the kernel notification you want to add to.. 
- `anID`: The ID of the simple notification (semaphore, message group, or event group) you want to add to the kernel notification. 
- `notifyParam1`: If `anID` specifies an event group, this parameter should contain the flags to set in the event group when [`MPCauseNotification`](./api-1585754-mpcausenotification.md) is called. If `anID` specifies a message queue, this parameter should contain the first pointer-sized value of the message to be sent to the message queue when [`MPCauseNotification`](./api-1585754-mpcausenotification.md) is called. 
- `notifyParam2`: If `anID` specifies a message queue, this parameter should contain the second pointer-sized value of the message to be sent to the message queue when [`MPCauseNotification`](./api-1585754-mpcausenotification.md) is called. Pass `NULL` if you don’t need this parameter.
- `notifyParam3`: If `anID` specifies a message queue, this parameter should contain the third pointer-sized value of the message sent to the message queue when [`MPCauseNotification`](./api-1585754-mpcausenotification.md) is called. Pass `NULL` if you don’t need this parameter.

## See Also

### Handling Kernel Notifications
- [MPCauseNotification](./api-1585754-mpcausenotification.md)
  Signals a kernel notification. 
- [MPCreateNotification](./api-1585723-mpcreatenotification.md)
  Creates a kernel notification
- [MPDeleteNotification](./api-1585659-mpdeletenotification.md)
  Removes a kernel notification. 
- [MPModifyNotificationParameters](./api-1585668-mpmodifynotificationparameters.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585780-mpmodifynotification)*