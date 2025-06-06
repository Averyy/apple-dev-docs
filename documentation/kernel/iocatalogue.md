# IOCatalogue

**Framework**: Kernel  
**Kind**: cl

In-kernel database for IOKit driver personalities.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class IOCatalogue : OSObject
```

#### Overview

The IOCatalogue is a database which contains all IOKit driver personalities. IOService uses this resource when matching devices to their associated drivers.

## Topics

### Miscellaneous
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
- [terminateDriversForModule(const char *, bool)](iocatalogue/1811392-terminatedriversformodule.md)
  Terminates all instances of a driver which depends on a particular module and unloads the module.
- [terminateDriversForModule(OSString *, bool)](iocatalogue/1811401-terminatedriversformodule.md)
  Terminates all instances of a driver which depends on a particular module and unloads the module.
- [unloadModule](iocatalogue/1811417-unloadmodule.md)
  Unloads the reqested module if no driver instances are currently depending on it.
### Instance Methods
- [- addDrivers](iocatalogue/3753418-adddrivers.md)
- [- addPersonality](iocatalogue/3753419-addpersonality.md)
- [- arrayForPersonality](iocatalogue/3753420-arrayforpersonality.md)
- [- exchangeDrivers](iocatalogue/3943374-exchangedrivers.md)
- [- findDrivers](iocatalogue/3753421-finddrivers.md)
- [- findDrivers](iocatalogue/3753422-finddrivers.md)
- [- free](iocatalogue/3753423-free.md)
- [- getGenerationCount](iocatalogue/3753424-getgenerationcount.md)
- [- getMetaClass](iocatalogue/3753425-getmetaclass.md)
- [- init](iocatalogue/3753426-init.md)
- [- isModuleLoaded](iocatalogue/3753428-ismoduleloaded.md)
- [- isModuleLoaded](iocatalogue/3753429-ismoduleloaded.md)
- [- moduleHasLoaded](iocatalogue/3753430-modulehasloaded.md)
- [- moduleHasLoaded](iocatalogue/3753431-modulehasloaded.md)
- [- personalityIsBoot](iocatalogue/3857659-personalityisboot.md)
- [- removeDrivers](iocatalogue/3753432-removedrivers.md)
- [- reset](iocatalogue/3753433-reset.md)
- [- resetAndAddDrivers](iocatalogue/3753434-resetandadddrivers.md)
- [- serialize](iocatalogue/3753435-serialize.md)
- [- serializeData](iocatalogue/3753436-serializedata.md)
- [- startMatching](iocatalogue/3753437-startmatching.md)
- [- startMatching](iocatalogue/3753438-startmatching.md)
- [- terminateDrivers](iocatalogue/3753439-terminatedrivers.md)
- [- terminateDriversForModule](iocatalogue/4048323-terminatedriversformodule.md)
- [- terminateDriversForModule](iocatalogue/4048324-terminatedriversformodule.md)
- [- unloadModule](iocatalogue/3753442-unloadmodule.md)
### Type Methods
- [+ initialize](iocatalogue/3753427-initialize.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocatalogue)*