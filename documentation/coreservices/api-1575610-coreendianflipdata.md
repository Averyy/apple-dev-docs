# CoreEndianFlipData

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Calls the flipper callback associated with the specifieddata type.

**Availability**:
- macOS 10.3+ - Deprecated in 10.8

## Declaration

```c
OSStatus CoreEndianFlipData(OSType dataDomain, OSType dataType, SInt16 id, void *data, ByteCount dataLen, Boolean currentlyNative);
```

#### Return Value

A result code. Returns `noErr` ifthe data is byte swapped and `handlerNotFound` ifthe data is not byte swapped. Note that data is only byte swappedif it needs to be byte swapped.

## Parameters

- `dataDomain`: An `OSType` value that specifies the domain of the flipper callback you want to invoke. Pass [`kCoreEndianResourceManagerDomain`](./api-1575588-domain_types/kcoreendianresourcemanagerdomain.md)	if your callback applies to resource data. Pass [`kCoreEndianAppleEventManagerDomain`](./api-1575588-domain_types/kcoreendianappleeventmanagerdomain.md) if your callback applies to Apple event data. See [Domain Types](./api-1575588-domain_types.md) for more information.
- `dataType`: An `OSType` value that specifies the type of data that needs to be byte-swapped. This is the four character code of the resource type or Apple event. This never needs to be byte-swapped even though GDB and Xcode display the resource in byte-swapped order.
- `id`: The resource ID of the data type. The Resource Manager byte-swaps this for you so you can compare the resource ID against constants in your code. If the data is not a resource, pass `0`. 
- `data`: A pointer to the first byte of the data to be byte swapped.
- `dataLen`: The length of the data (in bytes) to be byte swapped.
- `currentlyNative`: A Boolean value that indicates the direction to byte swap. Pass `true` when the data specified by the `data` parameter uses the byte ordering of the currently executing code. On a PowerPC system, `true` specifies that the data is in big-endian format. On an x86 system, `true` specifies that the data is in little-endian format. 

## See Also

### Working With Flippers
- [CoreEndianInstallFlipper](./api-1575602-coreendianinstallflipper.md)
  Installs a flipper callback for the specified data type.
- [CoreEndianGetFlipper](./api-1575564-coreendiangetflipper.md)
  Obtains the flipper callback that is installed for thespecified data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1575610-coreendianflipdata)*