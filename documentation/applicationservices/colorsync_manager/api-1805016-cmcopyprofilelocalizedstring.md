# CMCopyProfileLocalizedString

**Framework**: Application Services  
**Kind**: func

Gets one specific string out of a profile 

## Declaration

```c
CMError CMCopyProfileLocalizedString (
   CMProfileRef prof,
   OSType tag,
   CFStringRef reqLocale,
   CFStringRef *locale,
   CFStringRef *str
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

For example, you pass in the optional tag 'dscm' plus "enUS" for the `reqLocale` parameter, to for a U.S. English string. If a U.S. English string is not found, ColorSync falls back to a reasonable default: 

```occ
err = CMCopyProfileLocalizedString (prof, 'dscm',
                CFSTR("enUS"), nil, &theStr);
```

## Parameters

- `prof`: The profile to query. 
- `tag`: The tag type of profile to query.
- `reqLocale`: The requested locale (optional). 
- `locale`: On output, points to the locale (optional). 
- `str`: On output, points to the dictionary string (optional). 

## See Also

### Accessing Profile Descriptions
- [CMCopyProfileDescriptionString](./api-1805012-cmcopyprofiledescriptionstring.md)
  Returns the name of a profile as a CFString.
- [CMCopyProfileLocalizedStringDictionary](./api-1805020-cmcopyprofilelocalizedstringdict.md)
  Obtains a CFDictionary which contains the language locale and string for multiple localizations from a given tag.
- [CMSetProfileLocalizedStringDictionary](./api-1805025-cmsetprofilelocalizedstringdicti.md)
  Writes a dictionary of localized strings to a given tag in a profile. 
- [CMGetScriptProfileDescription](./api-1805029-cmgetscriptprofiledescription.md)
  Obtains the internal name (or description) of a profile and the script code identifying the language in which the profile name is specified from the specified profile.
- [CMGetProfileDescriptions](./api-1805034-cmgetprofiledescriptions.md)
  Obtains the description tag data for a specified profile.
- [CMSetProfileDescriptions](./api-1805039-cmsetprofiledescriptions.md)
  Sets the description tag data for a specified profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805016-cmcopyprofilelocalizedstring)*