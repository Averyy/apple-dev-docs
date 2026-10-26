# kIOMediaLiveKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

A property of IOMedia objects.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
#define kIOMediaLiveKey
```

#### Discussion

The kIOMediaLiveKey property has an OSBoolean value and is placed into an IOMedia instance created via the partition scheme. It describes whether the partition is live, that is, it is up-to-date with respect to the on-disk partition table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiomedialivekey)*