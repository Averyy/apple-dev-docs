# CMSetProfileDescriptions

**Framework**: Application Services  
**Kind**: func

Sets the description tag data for a specified profile.

## Declaration

```c
CMError CMSetProfileDescriptions (
   CMProfileRef prof,
   const char *aName,
   UInt32 aCount,
   ConstStr255Param mName,
   ScriptCode mCode,
   const UniChar *uName,
   UniCharCount uCount
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

Use this function to set the description tag data for a given profile. The ICC Profile Format Specification (available at [http://www.color.org](http://www.color.org)) includes a description tag (` 'desc'` ), designed to provide more information about a profile than can be contained in a file name. This is especially critical on file systems with 8.3 names. The tag data can consist of up to three separate pieces (strings) of information for a profile. These different strings are designed to allow for display in different languages or on different computer systems. Applications typically use one of the strings to show profiles in a list or a pop-up menu. 

## Parameters

- `prof`: A reference to the profile into which to set the description tag data. 
- `aName`: A pointer to a 7-bit Roman ASCII profile name string to be set for the profile. This string must be null-terminated. 
- `aCount`: A count of the number of characters in the string specified in the `aName` parameter
- `mName`: A pointer to the localized profile name string in Mac script-code format which is to be set for the profile. This string must be                   null-terminated.
- `mCode`: The script code corresponding to the string specified by the `mName` parameter.
- `uName`: A pointer to the localized Unicode profile name string which is to be set for the profile. This string must be null-terminated 
- `uCount`: A count of the number of Unicode characters in string specified by the `uName` parameter. Do not confuse this with a byte count, because each Unicode character requires two bytes. 

## See Also

### Accessing Profile Descriptions
- [CMCopyProfileDescriptionString](./api-1805012-cmcopyprofiledescriptionstring.md)
  Returns the name of a profile as a CFString.
- [CMCopyProfileLocalizedString](./api-1805016-cmcopyprofilelocalizedstring.md)
  Gets one specific string out of a profile 
- [CMCopyProfileLocalizedStringDictionary](./api-1805020-cmcopyprofilelocalizedstringdict.md)
  Obtains a CFDictionary which contains the language locale and string for multiple localizations from a given tag.
- [CMSetProfileLocalizedStringDictionary](./api-1805025-cmsetprofilelocalizedstringdicti.md)
  Writes a dictionary of localized strings to a given tag in a profile. 
- [CMGetScriptProfileDescription](./api-1805029-cmgetscriptprofiledescription.md)
  Obtains the internal name (or description) of a profile and the script code identifying the language in which the profile name is specified from the specified profile.
- [CMGetProfileDescriptions](./api-1805034-cmgetprofiledescriptions.md)
  Obtains the description tag data for a specified profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805039-cmsetprofiledescriptions)*