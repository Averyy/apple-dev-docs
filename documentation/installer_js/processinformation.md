# ProcessInformation

**Framework**: Installer JS  
**Kind**: uid

A dictionary (associative array) describing an application.

#### Overview

[`Table 1`](processinformation#2556489.md) describes the items available in the dictionary.

| Key | Description |
| --- | --- |
| `'PSN'` | The process serial number. See ProcessSerialNumber. |
| `'Parent PSN'` | The process serial number of the application that launched the application in question. |
| `‘FileType'` | The file type (if any) of the executable. |
| `‘FileCreator'` | The creator type (if any) of the executable. |
| `'BundlePath'` | The path to the application bundle (if the application is bundled). |
| `'pid'` | The UNIX PID for the program in question. |
| `'LSBackgroundOnly'` | `true` when the application is a background-only application; `false` otherwise. |
| `'LSUIElement'` | `true` when the application is an accessibility UIElement; `false` otherwise. |
| `'IsHiddenAttr'` | `true` if the application is currently hidden; `false` otherwise. |
| `'RequiresClassic'` | `true` if the application’s Info.plist file indicates that it requires Classic; `false` otherwise. |
| `'RequiresCarbon'` | `true` if the application’s Info.plist file indicates that it is a Carbon application; `false` otherwise. |

## See Also

- [Installer JS](installer_js.md)
  Manage and customize the installation and distribution experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/installer_js/processinformation)*