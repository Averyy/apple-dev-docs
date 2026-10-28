# fromIdentifier

**Framework**: Installer JS  
**Kind**: instm

Provides information about running processes with a given application identifier (bundle ID).

## Declaration

```
fromIdentifier(bundleID)
```

## Return Value

An array of dictionaries (associative arrays) describing the running applications identified by `bundleID`.

## Parameters

- `bundleID`: A string with the bundle ID of the desired application, such as `com.apple.TextEdit`.

## See Also

### Getting Information About Running Applications
- [fromPID](./api-1812189-frompid.md)
  Provides information about a running application with a given process ID.
- [all](./api-1812212-all.md)
  All running applications registered with the process manager.
### Related Documentation
- [ProcessInformation](../processinformation.md)
  A dictionary (associative array) describing an application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/installer_js/applications/1812198-fromidentifier)*