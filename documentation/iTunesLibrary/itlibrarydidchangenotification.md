# ITLibraryDidChangeNotification

**Framework**: iTunes Library  
**Kind**: var  
**Role**: Global Variable

This notification is sent to NSDistributedNotificationCenter when a change has occurred in the library.

**Availability**:
- Mac Catalyst 14.0+
- macOS 13.0+

## Declaration

```c
extern NSNotificationName const ITLibraryDidChangeNotification;
```

## Overview

The client should call [`reloadData()`](./itlibrary/reloaddata%28%29.md) if it wants a new view of the library contents.

> **Note**:  This is not a fine-grained notification.  This API does not support per-object change notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibrarydidchangenotification)*