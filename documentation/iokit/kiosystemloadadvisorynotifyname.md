# kIOSystemLoadAdvisoryNotifyName

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

The notification by this name fires when system "SystemLoadAdvisory" status changes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```c
#define kIOSystemLoadAdvisoryNotifyName
```

#### Discussion

Pass this string as an argument to register via notify(3). You can query SystemLoadAdvisory state via notify_get_state() when this notification fires - this is more efficient than calling IOGetSystemLoadAdvisory(), and returns an identical combined SystemLoadAdvisory value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiosystemloadadvisorynotifyname)*