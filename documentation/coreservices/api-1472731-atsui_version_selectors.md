# ATSUI Version Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify version information for Apple Type Service for Unicode Imaging.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [gestaltATSUVersion](./api-1472731-atsui_version_selectors/gestaltatsuversion.md)
  Specifies the version of ATSUI installed on the user’s system. You pass this selector to the `Gestalt` function. On return, the `Gestalt` function passes back a value that represents the version of ATSUI installed on the user’s system. 
- [gestaltOriginalATSUVersion](./api-1472731-atsui_version_selectors/gestaltoriginalatsuversion.md)
  Indicates that version 1.0 of ATSUI is installed on the user’s system.
- [gestaltATSUUpdate1](./api-1472731-atsui_version_selectors/gestaltatsuupdate1.md)
  Indicates that version 1.1 of ATSUI is installed on the user’s system.
- [gestaltATSUUpdate2](./api-1472731-atsui_version_selectors/gestaltatsuupdate2.md)
  Indicates that version 1.2 of ATSUI is installed on the user’s system.
- [gestaltATSUUpdate3](./api-1472731-atsui_version_selectors/gestaltatsuupdate3.md)
  Indicates that version 2.0 of ATSUI is installed on the user’s system.
- [gestaltATSUUpdate4](./api-1472731-atsui_version_selectors/gestaltatsuupdate4.md)
  Indicates that ATSUI for a version of macOS from 10.0.1 through 10.0.4 is installed on the user’s system.
- [gestaltATSUUpdate5](./api-1472731-atsui_version_selectors/gestaltatsuupdate5.md)
  Indicates that version 2.3 of ATSUI is installed on the user’s system. Available beginning with ATSUI 2.3, in OS X version 10.1.
- [gestaltATSUUpdate6](./api-1472731-atsui_version_selectors/gestaltatsuupdate6.md)
  Indicates that version 2.4 of ATSUI is installed on the user’s system. Available beginning with ATSUI 2.4, in OS X version 10.2.
- [gestaltATSUUpdate7](./api-1472731-atsui_version_selectors/gestaltatsuupdate7.md)
  Indicates that version 2.5 of ATSUI is installed on the user’s system. Available beginning with ATSUI 2.5, in OS X version 10.3.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472731-atsui_version_selectors)*