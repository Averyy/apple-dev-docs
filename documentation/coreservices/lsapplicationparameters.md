# LSApplicationParameters

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

The specification that defines the app, launch flags, and additional parameters that control how an app launches.

**Availability**:
- macOS 10.4+ - Deprecated in 10.10

## Declaration

```swift
struct LSApplicationParameters
```

```c
typedef struct LSApplicationParameters {
    ...
} LSApplicationParameters;
```

#### Overview

This structure is passed as a parameter to [`LSOpenApplication(_:_:)`](./api-1447930-lsopenapplication.md), [`LSOpenItemsWithRole(_:_:_:_:_:_:_:)`](./api-1449783-lsopenitemswithrole.md), and [`LSOpenURLsWithRole(_:_:_:_:_:_:)`](./api-1448184-lsopenurlswithrole.md).

## Topics

### Initializers
- [init()](./lsapplicationparameters/api-1441947-init.md)
- [init(version: CFIndex, flags: LSLaunchFlags, application: UnsafePointer<FSRef>!, asyncLaunchRefCon: UnsafeMutableRawPointer!, environment: Unmanaged<CFDictionary>!, argv: Unmanaged<CFArray>!, initialEvent: UnsafeMutablePointer<AppleEvent>!)](./lsapplicationparameters/api-1446779-init.md)
### Instance Properties
- [var application: UnsafePointer<FSRef>!](./lsapplicationparameters/api-1447460-application.md)
  The `FSRef` ofthe application to open.
- [var argv: Unmanaged<CFArray>!](./lsapplicationparameters/api-1445515-argv.md)
  An array of values of type [`CFString`](../CoreFoundation/cfstring.md) that specify the arguments that are to be passed to `main()` in the launched process. The value of this field can be `NULL`. This field is ignored in macOS 10.4.
- [var asyncLaunchRefCon: UnsafeMutableRawPointer!](./lsapplicationparameters/api-1444464-asynclaunchrefcon.md)
  The client `refCon` thatis to appear in subsequent launch notifications.
- [var environment: Unmanaged<CFDictionary>!](./lsapplicationparameters/api-1449247-environment.md)
  A dictionary of `CFStringRef` keysand values for environment variables to set in the launched process.The value of this field can be `NULL`.
- [var flags: LSLaunchFlags](./lsapplicationparameters/api-1450209-flags.md)
  Launch flags. For possible values, see [`LSLaunchFlags`](./lslaunchflags.md).
- [var initialEvent: UnsafeMutablePointer<AppleEvent>!](./lsapplicationparameters/api-1446633-initialevent.md)
  The first Apple Event to send to the launchedprocess. The value of this field can be `NULL`.
- [var version: CFIndex](./lsapplicationparameters/api-1441822-version.md)
  The version of the structure. The value of thisfield must be `0`.

## See Also

### Deprecated Structures
- [struct LSLaunchFSRefSpec](./lslaunchfsrefspec.md)
  The specification that defines, by file-system reference, an app to launch, items to open, or both, along with related information.
- [struct LSItemInfoRecord](./lsiteminforecord.md)
  The specification that contains requested information about an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lsapplicationparameters)*