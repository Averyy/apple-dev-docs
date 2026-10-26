# CMGetProfileDescriptions

**Framework**: Application Services  
**Kind**: func

Obtains the description tag data for a specified profile.

## Declaration

```c
CMError CMGetProfileDescriptions (
   CMProfileRef prof,
   char *aName,
   UInt32 *aCount,
   Str255 mName,
   ScriptCode *mCode,
   UniChar *uName,
   UniCharCount *uCount
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

Use this function to get the description tag data for a given profile. The ICC Profile Format Specification (available at [http://www.color.org](http://www.color.org) ) includes a description tag (`'desc'` ), designed to provide more information about a profile than can be contained in a file name. This is especially critical on file systems with 8.3 names. The tag data can consist of up to three separate pieces (strings) of information for a profile. These different strings are designed to allow for display in different languages or on different computer systems. Applications typically use one of the strings to show profiles in a list or a pop-up menu. 

## Parameters

- `prof`: A reference to the profile from which to obtain the description info. 
- `aName`: On output, a pointer to the profile name as a 7-bit Roman ASCII string. 
- `aCount`: On output, a pointer to a count of the number of characters returned in the `aName` field. 
- `mName`: On output, a pointer to the localized profile name string in Mac script-code format. 
- `mCode`: On output, a pointer the script code corresponding to the name string returned in the `mName` parameter. 
- `uName`: On output, a pointer to localizedUnicode profile name string. 
- `uCount`: On output, a pointer to a count of the number of Unicode (2-byte) characters returned in the `uName` parameter. 

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
- [CMSetProfileDescriptions](./api-1805039-cmsetprofiledescriptions.md)
  Sets the description tag data for a specified profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805034-cmgetprofiledescriptions)*