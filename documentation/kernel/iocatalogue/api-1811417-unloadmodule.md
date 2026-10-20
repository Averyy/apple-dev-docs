# unloadModule

**Framework**: Kernel  
**Kind**: instm

Unloads the reqested module if no driver instances are currently depending on it.

## Declaration

```c
IOReturn unloadModule(
 OSString *moduleName ) const;
```

## Parameters

- `moduleName`: An OSString containing the name of the module to unload.

## See Also

### Miscellaneous
- [addDrivers](./api-1811204-adddrivers.md)
  Adds an array of driver personalities to the database.
- [findDrivers(IOService *, SInt32 *)](./api-1811225-finddrivers.md)
  This is the primary entry point for IOService.
- [findDrivers(OSDictionary *, SInt32 *)](./api-1811242-finddrivers.md)
  A more general purpose interface which allows one to retreive driver personalities based the intersection of the 'matching' dictionary and the personality's own property list.
- [free](./api-1811255-free.md)
  Cleans up the database and deallocates memory allocated at initialization. This is never called in normal operation of the system.
- [getGenerationCount](./api-1811265-getgenerationcount.md)
  Get the current generation count of the database.
- [init](./api-1811279-init.md)
  Initializes the database object.
- [initialize](./api-1811287-initialize.md)
  Creates and initializes the database object and poputates it with in-kernel driver personalities.
- [isModuleLoaded](./api-1811295-ismoduleloaded.md)
  Reports if a kernel module has been loaded for a particular personality.
- [isModuleLoaded(const char *)](./api-1811303-ismoduleloaded.md)
  Reports if a kernel module has been loaded.
- [isModuleLoaded(OSString *)](./api-1811312-ismoduleloaded.md)
  Reports if a kernel module has been loaded.
- [moduleHasLoaded(const char *)](./api-1811319-modulehasloaded.md)
  Callback function called after a IOKit dependent kernel module is loaded.
- [moduleHasLoaded(OSString *)](./api-1811324-modulehasloaded.md)
  Callback function called after a IOKit dependent kernel module is loaded.
- [removeDrivers](./api-1811332-removedrivers.md)
  Remove driver personalities from the database based on matching information provided.
- [reset](./api-1811342-reset.md)
  Return the Catalogue to its initial state.
- [resetAndAddDrivers](./api-1811349-resetandadddrivers.md)
  Replace personalities in IOCatalog with those provided.
- [serialize](./api-1811365-serialize.md)
  Serializes the catalog for transport to the user.
- [startMatching](./api-1811371-startmatching.md)
  Starts an IOService matching thread where matching keys and values are provided by the matching dictionary.
- [terminateDrivers](./api-1811385-terminatedrivers.md)
  Terminates all instances of a driver which match the contents of the matching dictionary. Does not unload module.
- [terminateDriversForModule(const char *, bool)](./api-1811392-terminatedriversformodule.md)
  Terminates all instances of a driver which depends on a particular module and unloads the module.
- [terminateDriversForModule(OSString *, bool)](./api-1811401-terminatedriversformodule.md)
  Terminates all instances of a driver which depends on a particular module and unloads the module.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocatalogue/1811417-unloadmodule)*