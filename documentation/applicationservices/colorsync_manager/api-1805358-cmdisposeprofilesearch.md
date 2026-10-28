# CMDisposeProfileSearch

**Framework**: Application Services  
**Kind**: func

Frees the private memory allocated for a profile search after your application has completed the search. 

## Declaration

```c
void CMDisposeProfileSearch (
   CMProfileSearchRef search
);
```

## Overview

To set up a search, use the function [CMNewProfileSearch](./api-1805344-cmnewprofilesearch.md). To obtain a reference to a profile corresponding to a specific index in the list, use the function  [CMSearchGetIndProfile](./api-1805362-cmsearchgetindprofile.md). To obtain the file specification for a profile corresponding to a specific index in the list, use the function  [CMSearchGetIndProfileFileSpec](./api-1805365-cmsearchgetindprofilefilespec.md). To update the search result list, use the function  [CMUpdateProfileSearch](./api-1805356-cmupdateprofilesearch.md). 

### Version-Notes

This function is not recommended for use in ColorSync 2.5.

Starting with version 2.5, you should use the function [CMIterateColorSyncFolder](./api-1804904-cmiteratecolorsyncfolder.md) for profile searching.

## Parameters

- `search`: A reference to the profile search result list whose private memory is to be released. For a description of the `CMProfileSearchRef` private data type, see `CMProfileSearchRef`. See the QuickDraw Reference for a description of the PixMap data type.

## See Also

### Not Recommended
- [CMNewProfileSearch](./api-1805344-cmnewprofilesearch.md)
  Searches the ColorSync Profiles folder and returns a list of 2.x profiles that match the search specification.
- [CMUpdateProfileSearch](./api-1805356-cmupdateprofilesearch.md)
  Searches the ColorSync Profiles folder and updates an existing search result obtained originally from the `CMNewProfileSearch` function.
- [CMSearchGetIndProfile](./api-1805362-cmsearchgetindprofile.md)
  Opens the profile corresponding to a specific index into a specific search result list and obtains a reference to that profile. 
- [CMSearchGetIndProfileFileSpec](./api-1805365-cmsearchgetindprofilefilespec.md)
  Obtains the file specification for the profile at a specific index into a search result. 
- [CMCreateProfileIdentifier](./api-1805369-cmcreateprofileidentifier.md)
  Creates a profile identifier for a specified profile.
- [CMProfileIdentifierFolderSearch](./api-1805374-cmprofileidentifierfoldersearch.md)
  Searches the ColorSync Profiles folder and returns a list of profile references, one for each profile that matches the specified profile identifier.
- [CMProfileIdentifierListSearch](./api-1805376-cmprofileidentifierlistsearch.md)
  Searches a list of profile references and returns a list of all references that match a specified profile identifier. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805358-cmdisposeprofilesearch)*