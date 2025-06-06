# sysctl

**Framework**: Installer JS  
**Kind**: instm

Provides the result of a `sysctlbyname()` call using the given selector.

## Declaration

```swift
sysctl(selector)
```

#### Return_value

Hardware data corresponding to `selector`.

#### Overview

Use `man sysctl` in the macOS Terminal application to see a list of hardware selectors.

> 💡 **Tip**: If you are using this function to screen for hardware features at install-time, consider using the “Pre-install Requirements Property List” setting of `productbuild` instead. Use `man productbuild` in the macOS Terminal application to see a list of supported requirement keys.

If you are using this function to screen for hardware features at install-time, consider using the “Pre-install Requirements Property List” setting of `productbuild` instead. Use `man productbuild` in the macOS Terminal application to see a list of supported requirement keys.

## Parameters

- `selector`: String with the hardware selector for the desired data.

## See Also

- [users.desktopSessionCount](system/1812277-users_desktopsessioncount.md)
  The number of logged-in users.
- [version](system/1812284-version.md)
  A dictionary (associative array) with information about the current system version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/installer_js/system/1812308-sysctl)*