# fromPID

**Framework**: Installer JS  
**Kind**: instm

Provides information about a running application with a given process ID.

## Declaration

```swift
fromPID(processID)
```

#### Return_value

A dictionary (associative array) describing the application identified by `processID`.

## Parameters

- `processID`: A string with the process ID of the desired application.

## See Also

- [fromIdentifier](applications/1812198-fromidentifier.md)
  Provides information about running processes with a given application identifier (bundle ID).
- [all](applications/1812212-all.md)
  All running applications registered with the process manager.
- [ProcessInformation](processinformation.md)
  A dictionary (associative array) describing an application.
- [Installer JS](installer_js.md)
  Manage and customize the installation and distribution experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/installer_js/applications/1812189-frompid)*