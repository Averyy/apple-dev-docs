# terminateDriversForModule(const char *, bool)

**Framework**: Kernel  
**Kind**: instm

Terminates all instances of a driver which depends on a particular module and unloads the module.

## Declaration

```swift
IOReturn terminateDriversForModule(
 const char *moduleName,
 bool unload = true);
```

## Parameters

- `moduleName`: Name of the module which is used to determine which driver instances to terminate and unload.
- `unload`: Flag to cause the actual unloading of the module.

## See Also

- [addDrivers](iocatalogue/1811204-adddrivers.md)
  Adds an array of driver personalities to the database.
- [findDrivers(IOService *, SInt32 *)](iocatalogue/1811225-finddrivers.md)
  This is the primary entry point for IOService.
- [findDrivers(OSDictionary *, SInt32 *)](iocatalogue/1811242-finddrivers.md)
  A more general purpose interface which allows one to retreive driver personalities based the intersection of the 'matching' dictionary and the personality's own property list.
- [free](iocatalogue/1811255-free.md)
  Cleans up the database and deallocates memory allocated at initialization. This is never called in normal operation of the system.
- [getGenerationCount](iocatalogue/1811265-getgenerationcount.md)
  Get the current generation count of the database.
- [init](iocatalogue/1811279-init.md)
  Initializes the database object.
- [initialize](iocatalogue/1811287-initialize.md)
  Creates and initializes the database object and poputates it with in-kernel driver personalities.
- [isModuleLoaded](iocatalogue/1811295-ismoduleloaded.md)
  Reports if a kernel module has been loaded for a particular personality.
- [isModuleLoaded(const char *)](iocatalogue/1811303-ismoduleloaded.md)
  Reports if a kernel module has been loaded.
- [isModuleLoaded(OSString *)](iocatalogue/1811312-ismoduleloaded.md)
  Reports if a kernel module has been loaded.
- [moduleHasLoaded(const char *)](iocatalogue/1811319-modulehasloaded.md)
  Callback function called after a IOKit dependent kernel module is loaded.
- [moduleHasLoaded(OSString *)](iocatalogue/1811324-modulehasloaded.md)
  Callback function called after a IOKit dependent kernel module is loaded.
- [removeDrivers](iocatalogue/1811332-removedrivers.md)
  Remove driver personalities from the database based on matching information provided.
- [reset](iocatalogue/1811342-reset.md)
  Return the Catalogue to its initial state.
- [resetAndAddDrivers](iocatalogue/1811349-resetandadddrivers.md)
  Replace personalities in IOCatalog with those provided.
- [serialize](iocatalogue/1811365-serialize.md)
  Serializes the catalog for transport to the user.
- [startMatching](iocatalogue/1811371-startmatching.md)
  Starts an IOService matching thread where matching keys and values are provided by the matching dictionary.
- [terminateDrivers](iocatalogue/1811385-terminatedrivers.md)
  Terminates all instances of a driver which match the contents of the matching dictionary. Does not unload module.
- [terminateDriversForModule(OSString *, bool)](iocatalogue/1811401-terminatedriversformodule.md)
  Terminates all instances of a driver which depends on a particular module and unloads the module.
- [unloadModule](iocatalogue/1811417-unloadmodule.md)
  Unloads the reqested module if no driver instances are currently depending on it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocatalogue/1811392-terminatedriversformodule)*