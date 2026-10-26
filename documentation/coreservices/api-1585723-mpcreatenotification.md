# MPCreateNotification

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a kernel notification

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPCreateNotification(MPNotificationID *notificationID);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

#### Discussion

After creating the kernel notification object, you can add simple notifications by calling the function  [`MPModifyNotification`](./api-1585780-mpmodifynotification.md).

Also see the function  [`MPDeleteNotification`](./api-1585659-mpdeletenotification.md). 

## Parameters

- `notificationID`: On return, `notificationID` points to the newly created kernel notification. 

## See Also

### Handling Kernel Notifications
- [MPCauseNotification](./api-1585754-mpcausenotification.md)
  Signals a kernel notification. 
- [MPDeleteNotification](./api-1585659-mpdeletenotification.md)
  Removes a kernel notification. 
- [MPModifyNotification](./api-1585780-mpmodifynotification.md)
  Adds a simple notification to a kernel notification.
- [MPModifyNotificationParameters](./api-1585668-mpmodifynotificationparameters.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585723-mpcreatenotification)*