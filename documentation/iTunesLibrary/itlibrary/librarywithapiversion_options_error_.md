# libraryWithAPIVersion:options:error:

**Framework**: iTunes Library  
**Kind**: method  
**Role**: Type Method

Creates and initializes an instance of ITLibrary that can retrieve media entities.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.14+

## Declaration

```objc
+ (instancetype) libraryWithAPIVersion:(NSString *) requestedAPIVersion options:(ITLibInitOptions) options error:(NSError **) error;
```

## Return Value

An [`ITLibrary`](../itlibrary.md) instance that can retrieve media entities, or `nil` if the method fails.

## Discussion

Unless you specify the [`ITLibInitOptions.lazyLoadData`](../itlibinitoptions/lazyloaddata.md) option, the system reads and parses the default iTunes database for the current user during initialization of the [`ITLibrary`](../itlibrary.md) class. All media entities cache in memory until deallocation of the object occurs.

## Parameters

- `requestedAPIVersion`: The version of the iTunesLibrary API that the app is requesting. Provide “1.0” if unknown.
- `options`: Options that change the initialization behavior. See [`ITLibInitOptions`](../itlibinitoptions.md).
- `error`: A pointer to a variable that receives an [`NSError`](../../Foundation/nserror.md) if this method fails. Can be `nil` if the error isn’t applicable to the caller.

## See Also

### Essentials
- [convenience init(apiVersion: String) throws](./init%28apiversion%29-71e74.md)
  Initializes an instance of [`ITLibrary`](../itlibrary.md) that can retrieve media entities.
- [init(apiVersion: String, options: ITLibInitOptions) throws](./init%28apiversion,options%29-9eorg.md)
  Initializes an instance of `ITLibrary` that can retrieve media entities.
- [+ libraryWithAPIVersion:error:](./librarywithapiversion_error_.md)
  Creates and initializes an instance of `ITLibrary` that can retrieve media entities.
- [enum ITLibInitOptions](../itlibinitoptions.md)
  These constants describe initialization options for an iTunes library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibrary/librarywithapiversion:options:error:)*