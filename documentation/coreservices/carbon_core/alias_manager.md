# Alias Manager

**Framework**: Core Services  
**Role**: API Collection

Create and resolve alias records that describe file system objects such as files, directories, and volumes. 

> **Deprecated**: In macOS 10.8 and later, use the bookmark APIs provided by the [`NSURL`](../../Foundation/nsurl.md) class instead. For more information, see [Locating Files Using Bookmarks](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/AccessingFilesandDirectories/AccessingFilesandDirectories.html#//apple_ref/doc/uid/TP40010672-CH3-SW10) in [File System Programming Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672).

## Topics

### Creating and Updating Alias Records
- [FSNewAlias](../api-1444363-fsnewalias.md)
  Creates a new alias record, given a target file or directory.
- [FSNewAliasUnicode](../api-1444376-fsnewaliasunicode.md)
  Creates a new alias record, given the Unicode name and parent directory of the target.
- [FSNewAliasFromPath](../api-1444431-fsnewaliasfrompath.md)
  Creates a new alias record, given the pathname of the target file or directory.
- [FSNewAliasMinimal](../api-1444337-fsnewaliasminimal.md)
  Creates a new minimal alias record, given a target file or directory.
- [FSNewAliasMinimalUnicode](../api-1444409-fsnewaliasminimalunicode.md)
  Creates a minimal alias, given the Unicode name and parent directory of the target.
- [FSUpdateAlias](../api-1444399-fsupdatealias.md)
  Updates an alias record for a specified target.
### Getting Alias Size
- [GetAliasSize](../api-1444419-getaliassize.md)
  Gets the size of an alias record referenced by a handle.
- [GetAliasSizeFromPtr](../api-1444380-getaliassizefromptr.md)
  Gets the size of an alias record referenced by a pointer.
### Getting and Setting Alias User Types
- [GetAliasUserType](../api-1444311-getaliasusertype.md)
  Gets the user type for an alias record referenced by a handle.
- [SetAliasUserType](../api-1444428-setaliasusertype.md)
  Sets the user type for an alias record referenced by a handle.
- [GetAliasUserTypeFromPtr](../api-1444345-getaliasusertypefromptr.md)
  Gets the user type for the alias record referenced by a pointer.
- [SetAliasUserTypeWithPtr](../api-1444309-setaliasusertypewithptr.md)
  Sets the user type for the alias record referenced by a pointer.
### Resolving and Reading Alias Records
- [FSCopyAliasInfo](../api-1444271-fscopyaliasinfo.md)
  Returns information from an alias handle.
- [FSMatchAliasBulk](../api-1444389-fsmatchaliasbulk.md)
  Identifies a list of possible matches for an alias.
- [FSResolveAlias](../api-1444297-fsresolvealias.md)
  Returns an `FSRef` to the single most likely target of an alias record.
- [FSResolveAliasWithMountFlags](../api-1444279-fsresolvealiaswithmountflags.md)
  Returns an `FSRef` to the target of an alias.
### Working With Finder Alias Files
- [FSFollowFinderAlias](../api-1444287-fsfollowfinderalias.md)
  Resolves an alias record obtained from a Finder alias file.
- [FSIsAliasFile](../api-1444426-fsisaliasfile.md)
  Determines whether a file system object is an alias file, a data file, or a folder.
- [FSResolveAliasFile](../api-1444372-fsresolvealiasfile.md)
  Resolves an alias contained in an alias file.
- [FSResolveAliasFileWithMountFlags](../api-1444327-fsresolvealiasfilewithmountflags.md)
  Resolves an alias contained in an alias file.
### Callbacks
- [FSAliasFilterProcPtr](../fsaliasfilterprocptr.md)
  Defines a pointer to an alias filtering callback function that filters out possible targets identified by the [`FSMatchAliasBulk`](../api-1444389-fsmatchaliasbulk.md) function.
### Data Types
- [AliasInfoType](../aliasinfotype.md)
  Defines the alias record information type used in the index parameter of `GetAliasInfo`.
- [AliasRecord](../aliasrecord.md)
  Defines an alias record.
- [FSAliasInfo](../fsaliasinfo.md)
  Defines an information block passed to the `FSCopyAliasInfo` function.
### Constants
- [FSAliasInfoBitmap](../fsaliasinfobitmap.md)
  Returned by the `FSCopyAliasInfo` function to indicate which fields of the alias information structure contain valid data.
- [Volume Mount Options](../api-1444436-volume_mount_options.md)
  Specify how an alias should be resolved.
- [Matching Constants](../api-1444405-matching_constants.md)
  Specify the matching criteria for the alias matching functions.
- [Alias Resource Type](../api-1444395-alias_resource_type.md)
  Specifies the file type of an alias resource file.
- [Information Type Constants](../api-1444386-information_type_constants.md)
  The `GetAliasInfo` function uses these constants in the `index` parameter.

## See Also

### Managers
- [Component Manager](./component_manager.md)
  Find and use components in your app or add custom components to system-provided services, such as QuickTime and Core Audio. 
- [File Manager](./file_manager.md)
  Interact with files, folders, and volumes.
- [Gestalt Manager](./gestalt_manager.md)
  Investigate the operating environment of your app.
- [Text Encoding Conversion Manager](./text_encoding_conversion_manager.md)
  Handle text encoding conversion between apps and transfer text across different platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/carbon_core/alias_manager)*