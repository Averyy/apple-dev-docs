# CoreEndianInstallFlipper

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Installs a flipper callback for the specified data type.

**Availability**:
- macOS 10.3+ - Deprecated in 10.8

## Declaration

```c
OSStatus CoreEndianInstallFlipper(OSType dataDomain, OSType dataType, CoreEndianFlipProc proc, void *refcon);
```

## Return Value

A result code. Returns `noErr` ifyour flipper callback is installed.

## Discussion

You should install the callback by calling the function `CoreEndianInstallFlipper` when yourapplication calls its initialization routine or when you open yourresource file. 

## Parameters

- `dataDomain`: An `OSType` value that specifies the domain to which the flipper callback applies. Pass [`kCoreEndianResourceManagerDomain`](./api-1575588-domain_types/kcoreendianresourcemanagerdomain.md)if your callback applies to resource data. Pass [`kCoreEndianAppleEventManagerDomain`](./api-1575588-domain_types/kcoreendianappleeventmanagerdomain.md) if your callback applies to Apple event data. See [Domain Types](./api-1575588-domain_types.md) for more information.
- `dataType`: An `OSType` value that specifies the type of data for which you want your flipper callback installed. This is the four character code of the resource type or Apple event.
- `proc`: A pointer to your flipper callback. The flipper callback is installed into a per-process table that is searched before the system table.
- `refCon`: A 32-bit value containing or referring to data needed by the callback.

## See Also

### Working With Flippers
- [CoreEndianGetFlipper](./api-1575564-coreendiangetflipper.md)
  Obtains the flipper callback that is installed for thespecified data type.
- [CoreEndianFlipData](./api-1575610-coreendianflipdata.md)
  Calls the flipper callback associated with the specifieddata type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1575602-coreendianinstallflipper)*