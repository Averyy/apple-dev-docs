# Gestalt Manager

**Framework**: Core Services  
**Role**: API Collection

Investigate the operating environment of your app.

> **Deprecated**: In macOS 10.8 and later, use [`ProcessInfo`](../../Foundation/processinfo.md) or `sysctl` instead.

## Topics

### Result Codes
- [var gestaltUnknownErr: Int](../gestaltunknownerr.md)
  Specifies an unknown error.
- [var gestaltUndefSelectorErr: Int](../gestaltundefselectorerr.md)
  Specifies an undefined selector was passed to the Gestalt Manager.
- [var gestaltDupSelectorErr: Int](../gestaltdupselectorerr.md)
  Specifies you tried to add an entry that already existed.
- [var gestaltLocationErr: Int](../gestaltlocationerr.md)
  Specifies the gestalt function ptr was not in the system heap.

## See Also

### Managers
- [Component Manager](./component_manager.md)
  Find and use components in your app or add custom components to system-provided services, such as QuickTime and Core Audio. 
- [Text Encoding Conversion Manager](./text_encoding_conversion_manager.md)
  Handle text encoding conversion between apps and transfer text across different platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/carbon_core/gestalt_manager)*