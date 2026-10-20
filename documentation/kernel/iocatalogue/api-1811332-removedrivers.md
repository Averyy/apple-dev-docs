# removeDrivers

**Framework**: Kernel  
**Kind**: instm

Remove driver personalities from the database based on matching information provided.

## Declaration

```c
bool removeDrivers(
 OSDictionary *matching,
 bool doNubMatching = true );
```

#### Return Value

Returns true if personality was removed successfully. Failure is due to a memory allocation failure.

## Parameters

- `matching`: A dictionary whose keys and values are used for matching personalities in the database. For example, a matching dictionary containing a 'IOProviderClass' key with the value 'IOPCIDevice' will remove all personalities which have the key 'IOProviderClass' equal to 'IOPCIDevice'.
- `doNubMatchng`: Start matching process after personalities have been removed. Matching criteria is based on IOProviderClass of those personalities which were removed. This is to allow drivers which haven't been matched to match against NUB's which were blocked by the previous personalities.

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
- [unloadModule](./api-1811417-unloadmodule.md)
  Unloads the reqested module if no driver instances are currently depending on it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocatalogue/1811332-removedrivers)*