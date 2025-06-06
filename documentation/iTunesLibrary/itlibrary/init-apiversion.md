# init(apiVersion:)

**Framework**: iTunes Library  
**Kind**: init

Initializes an instance of [`ITLibrary`](itlibrary.md) that can retrieve media entities.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
convenience init(apiVersion requestedAPIVersion: String) throws
```

#### Return Value

An [`ITLibrary`](itlibrary.md) instance that can retrieve media entities, or `nil` if the method fails.

#### Discussion

During initialization of the [`ITLibrary`](itlibrary.md) class, the system reads and parses the default iTunes database for the current user. All media entities cache in memory until deallocation of the object occurs.

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

- `requestedAPIVersion`: The version of the iTunesLibrary API that the app is requesting. Provide   if unknown.

## See Also

- [init(apiVersion: String, options: ITLibInitOptions) throws](itlibrary/init(apiversion:options:).md)
  Initializes an instance of `ITLibrary` that can retrieve media entities.
- [enum ITLibInitOptions](itlibinitoptions.md)
  These constants describe initialization options for an iTunes library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibrary/init(apiversion:))*