# LSLaunchFlags

**Framework**: Core Services  
**Kind**: struct

The specification for launching an app.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct LSLaunchFlags
```

#### Overview

They are passed in a launch specification structure (`LSLaunchFSRefSpec` to the `LSOpenFromRefSpec` function or `LSLaunchURLSpec` to the `LSOpenFromURLSpec` function), to control the manner in which apps are launched.

## Topics

### Creating Application Launch Flags
- [init(rawValue: OptionBits)](lslaunchflags/1449893-init.md)
### Constants
- [static var defaults: LSLaunchFlags](lslaunchflags/1443121-defaults.md)
  Requests launching in the default manner (as if the only flags set were `kLSLaunchNoParams`, `kLSLaunchAsync`, and `kLSLaunchStartClassic`).
- [static var andPrint: LSLaunchFlags](lslaunchflags/1442495-andprint.md)
  Requests that documents opened in the application be printed.
- [static var andDisplayErrors: LSLaunchFlags](lslaunchflags/1443557-anddisplayerrors.md)
  Requests that launch and open failures be displayed in the UI.
- [static var dontAddToRecents: LSLaunchFlags](lslaunchflags/1442580-dontaddtorecents.md)
  Requests that the application or documents not be added to the Finder’s Recent Items menu.
- [static var dontSwitch: LSLaunchFlags](lslaunchflags/1442057-dontswitch.md)
  Requests that the application be launched without being brought to the foreground.
- [static var async: LSLaunchFlags](lslaunchflags/1445037-async.md)
  Requests that the application be launched asynchronously.
- [static var newInstance: LSLaunchFlags](lslaunchflags/1443359-newinstance.md)
  Requests that a new instance of the application be started, even if one is already running.
- [static var andHide: LSLaunchFlags](lslaunchflags/1444620-andhide.md)
  Requests that the application be hidden as soon as it completes its launch sequence.
- [static var andHideOthers: LSLaunchFlags](lslaunchflags/1448911-andhideothers.md)
  Requests that other applications be hidden as soon as the opened application completes its launch sequence.

## Relationships

### Conforms To
- [OptionSet](../swift/optionset.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lslaunchflags)*