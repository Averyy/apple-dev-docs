# CMSearchGetIndProfileFileSpec

**Framework**: Application Services  
**Kind**: func

Obtains the file specification for the profile at a specific index into a search result. 

## Declaration

```c
CMError CMSearchGetIndProfileFileSpec (
   CMProfileSearchRef search,
   UInt32 index,
   FSSpec *spec
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

Before your application can call the `CMSearchGetIndProfileFileSpec` function, it must call the function [CMNewProfileSearch](./api-1805344-cmnewprofilesearch.md) to perform a profile search and produce a search result list. The search result list is a private data structure maintained by ColorSync. 

The `CMSearchGetIndProfileFileSpec` function obtains the Macintosh file system file specification for a profile at a specific index in the search result list. 

### Version-Notes

This function is not recommended for use in ColorSync 2.5.

Starting with version 2.5, you should use the function [CMIterateColorSyncFolder](./api-1804904-cmiteratecolorsyncfolder.md) for profile searching.

## Parameters

- `search`: A reference to the profile search result containing the profile whose file specification you want to obtain. For a description of the `CMProfileSearchRef` private data type, see `CMProfileSearchRef`. See the QuickDraw Reference for a description of the PixMap data type.
- `index`: The index of the profile whose file specification you want to obtain. This is a one-based index into a set of profiles in the search result list. The index must be less than or equal to the value returned as the `count` parameter of the `CMNewProfileSearch` function or the `CMUpdateProfileSearch` function; otherwise `CMSearchGetIndProfile` returns a result code of `cmIndexRangeErr`. 
- `profileFile`: A pointer to a file specification. On return, this parameter points to a file specification for the profile at the location specified by `index`. See the QuickDraw Reference for a description of the PixMap data type.

## See Also

### Not Recommended
- [CMNewProfileSearch](./api-1805344-cmnewprofilesearch.md)
  Searches the ColorSync Profiles folder and returns a list of 2.x profiles that match the search specification.
- [CMUpdateProfileSearch](./api-1805356-cmupdateprofilesearch.md)
  Searches the ColorSync Profiles folder and updates an existing search result obtained originally from the `CMNewProfileSearch` function.
- [CMDisposeProfileSearch](./api-1805358-cmdisposeprofilesearch.md)
  Frees the private memory allocated for a profile search after your application has completed the search. 
- [CMSearchGetIndProfile](./api-1805362-cmsearchgetindprofile.md)
  Opens the profile corresponding to a specific index into a specific search result list and obtains a reference to that profile. 
- [CMCreateProfileIdentifier](./api-1805369-cmcreateprofileidentifier.md)
  Creates a profile identifier for a specified profile.
- [CMProfileIdentifierFolderSearch](./api-1805374-cmprofileidentifierfoldersearch.md)
  Searches the ColorSync Profiles folder and returns a list of profile references, one for each profile that matches the specified profile identifier.
- [CMProfileIdentifierListSearch](./api-1805376-cmprofileidentifierlistsearch.md)
  Searches a list of profile references and returns a list of all references that match a specified profile identifier. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805365-cmsearchgetindprofilefilespec)*