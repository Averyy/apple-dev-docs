# init(apiVersion:)

**Framework**: iTunes Library  
**Kind**: init  
**Role**: Initializer

Initializes an instance of [`ITLibrary`](../itlibrary.md) that can retrieve media entities.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
convenience init(apiVersion requestedAPIVersion: String) throws
```

```objc
- (instancetype) initWithAPIVersion:(NSString *) requestedAPIVersion error:(NSError **) error;
```

#### Return Value

An [`ITLibrary`](../itlibrary.md) instance that can retrieve media entities, or `nil` if the method fails.

#### Discussion

During initialization of the [`ITLibrary`](../itlibrary.md) class, the system reads and parses the default iTunes database for the current user. All media entities cache in memory until deallocation of the object occurs.

Listing 1.

```objc
#import <iTunesLibrary/ITLibrary.h>
 
NSError * error = nil;
ITLibrary* library = [[ITLibrary alloc] initWithAPIVersion:@"1.0" error:&error];
if (library)
{
  NSArray playlists = library.allPlaylists; //  <- NSArray of ITLibPlaylist
  NSArray mediaItems = library.allMediaItems; //  <- NSArray of ITLibMediaItem
}
```

## Parameters

- `requestedAPIVersion`: The version of the iTunesLibrary API that the app is requesting. Provide `"1.0"` if unknown.

## See Also

### Essentials
- [init(apiVersion: String, options: ITLibInitOptions) throws](./init%28apiversion,options%29-9eorg.md)
  Initializes an instance of `ITLibrary` that can retrieve media entities.
- [enum ITLibInitOptions](../itlibinitoptions.md)
  These constants describe initialization options for an iTunes library.
- [+ libraryWithAPIVersion:error:](./librarywithapiversion_error_.md)
  Creates and initializes an instance of `ITLibrary` that can retrieve media entities.
- [+ libraryWithAPIVersion:options:error:](./librarywithapiversion_options_error_.md)
  Creates and initializes an instance of ITLibrary that can retrieve media entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibrary/init(apiversion:)-71e74)*