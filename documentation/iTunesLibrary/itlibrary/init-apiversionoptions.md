# init(apiVersion:options:)

**Framework**: iTunes Library  
**Kind**: init

Initializes an instance of `ITLibrary` that can retrieve media entities.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.14+

## Declaration

```swift
init(apiVersion requestedAPIVersion: String, options: ITLibInitOptions) throws
```

#### Return Value

An [`ITLibrary`](itlibrary.md) instance that can retrieve media entities, or `nil` if the method fails.

#### Discussion

Unless you specify the [`ITLibInitOptions.lazyLoadData`](itlibinitoptions/lazyloaddata.md) option, the system reads and parses the default iTunes database for the current user during initialization of the [`ITLibrary`](itlibrary.md) class. All media entities cache in memory until deallocation of the object occurs.

## Parameters

- `requestedAPIVersion`: The version of the iTunesLibrary API that the app is requesting. Provide   if unknown.
- `options`: Options that change the initialization behavior. See  .

## See Also

- [convenience init(apiVersion: String) throws](itlibrary/init(apiversion:).md)
  Initializes an instance of [`ITLibrary`](itlibrary.md) that can retrieve media entities.
- [enum ITLibInitOptions](itlibinitoptions.md)
  These constants describe initialization options for an iTunes library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibrary/init(apiversion:options:))*