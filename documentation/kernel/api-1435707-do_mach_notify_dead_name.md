# do_mach_notify_dead_name

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```c
kern_return_t do_mach_notify_dead_name(mach_port_t notify, mach_port_name_t name);
```

## See Also

### Notifications
- [do_mach_notify_no_senders](./api-1435685-do_mach_notify_no_senders.md)
- [do_mach_notify_port_deleted](./api-1435709-do_mach_notify_port_deleted.md)
- [do_mach_notify_port_destroyed](./api-1435680-do_mach_notify_port_destroyed.md)
- [do_mach_notify_send_once](./api-1435711-do_mach_notify_send_once.md)
- [coalition_notification](./api-1543358-coalition_notification.md)
- [coalition_notification_server](./api-1543361-coalition_notification_server.md)
- [coalition_notification_server_routine](./api-1543352-coalition_notification_server_ro.md)
- [fairplay_server](./api-3281841-fairplay_server.md)
- [fairplay_server_routine](./api-3281842-fairplay_server_routine.md)
- [fairplayd_arcade_request](./api-3281851-fairplayd_arcade_request.md)
- [receive_sysdiagnose_notification](./api-1412350-receive_sysdiagnose_notification.md)
- [receive_sysdiagnose_notification_with_audit_token](./api-3521293-receive_sysdiagnose_notification.md)
- [mach_dead_name_notification_t](./mach_dead_name_notification_t.md)
- [mach_no_senders_notification_t](./mach_no_senders_notification_t.md)
- [mach_send_once_notification_t](./mach_send_once_notification_t.md)
- [mach_send_possible_notification_t](./mach_send_possible_notification_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1435707-do_mach_notify_dead_name)*