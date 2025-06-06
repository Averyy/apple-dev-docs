# LSAcceptanceFlags

**Framework**: Core Services  
**Kind**: struct

The specification that determines whether an app can accept (open) an item.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct LSAcceptanceFlags
```

#### Overview

These flags are passed to the functions `LSCanRefAcceptItem` and `LSCanURLAcceptURL`.

## Topics

### Creating Acceptance Flags
- [init(rawValue: OptionBits)](lsacceptanceflags/1443753-init.md)
  Creates a new acceptance flag from the given raw value.
### Constants
- [static var acceptDefault: LSAcceptanceFlags](lsacceptanceflags/1447965-acceptdefault.md)
  Requests the default behavior that does not require the user interface to log in be presented.
- [static var acceptAllowLoginUI: LSAcceptanceFlags](lsacceptanceflags/1443098-acceptallowloginui.md)
  Requests that the user interface to log in be presented.

## Relationships

### Conforms To
- [OptionSet](../swift/optionset.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lsacceptanceflags)*