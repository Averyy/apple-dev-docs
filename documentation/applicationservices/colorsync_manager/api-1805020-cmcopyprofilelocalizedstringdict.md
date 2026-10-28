# CMCopyProfileLocalizedStringDictionary

**Framework**: Application Services  
**Kind**: func

Obtains a CFDictionary which contains the language locale and string for multiple localizations from a given tag.

## Declaration

```c
CMError CMCopyProfileLocalizedStringDictionary (
   CMProfileRef prof,
   OSType tag,
   CFDictionaryRef *theDict
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

This function allows you to get a CFDictionary which contains the language locale and string for multiple localizations from a given tag. 

## Parameters

- `prof`: The profile to query 
- `tag`: The tag type of profile to query 
- `theDict`: On output, points to the dictionary .See the CFDictionary documentation for a description of the `CFDictionaryRef` data type. 

## See Also

### Accessing Profile Descriptions
- [CMCopyProfileDescriptionString](./api-1805012-cmcopyprofiledescriptionstring.md)
  Returns the name of a profile as a CFString.
- [CMCopyProfileLocalizedString](./api-1805016-cmcopyprofilelocalizedstring.md)
  Gets one specific string out of a profile 
- [CMSetProfileLocalizedStringDictionary](./api-1805025-cmsetprofilelocalizedstringdicti.md)
  Writes a dictionary of localized strings to a given tag in a profile. 
- [CMGetScriptProfileDescription](./api-1805029-cmgetscriptprofiledescription.md)
  Obtains the internal name (or description) of a profile and the script code identifying the language in which the profile name is specified from the specified profile.
- [CMGetProfileDescriptions](./api-1805034-cmgetprofiledescriptions.md)
  Obtains the description tag data for a specified profile.
- [CMSetProfileDescriptions](./api-1805039-cmsetprofiledescriptions.md)
  Sets the description tag data for a specified profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805020-cmcopyprofilelocalizedstringdict)*