# receive_sysdiagnose_notification

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.11+

## Declaration

```swift
kern_return_t receive_sysdiagnose_notification(mach_port_t sysdiagnose_port, uint32_t flags);
```

## See Also

- [do_mach_notify_dead_name](1435707-do_mach_notify_dead_name.md)
- [do_mach_notify_no_senders](1435685-do_mach_notify_no_senders.md)
- [do_mach_notify_port_deleted](1435709-do_mach_notify_port_deleted.md)
- [do_mach_notify_port_destroyed](1435680-do_mach_notify_port_destroyed.md)
- [do_mach_notify_send_once](1435711-do_mach_notify_send_once.md)
- [coalition_notification](1543358-coalition_notification.md)
- [coalition_notification_server](1543361-coalition_notification_server.md)
- [coalition_notification_server_routine](1543352-coalition_notification_server_ro.md)
- [fairplay_server](3281841-fairplay_server.md)
- [fairplay_server_routine](3281842-fairplay_server_routine.md)
- [fairplayd_arcade_request](3281851-fairplayd_arcade_request.md)
- [receive_sysdiagnose_notification_with_audit_token](3521293-receive_sysdiagnose_notification.md)
- [mach_dead_name_notification_t](mach_dead_name_notification_t.md)
- [mach_no_senders_notification_t](mach_no_senders_notification_t.md)
- [mach_send_once_notification_t](mach_send_once_notification_t.md)
- [mach_send_possible_notification_t](mach_send_possible_notification_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1412350-receive_sysdiagnose_notification)*