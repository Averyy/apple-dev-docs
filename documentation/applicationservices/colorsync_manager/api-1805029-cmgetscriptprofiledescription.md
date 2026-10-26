# CMGetScriptProfileDescription

**Framework**: Application Services  
**Kind**: func

Obtains the internal name (or description) of a profile and the script code identifying the language in which the profile name is specified from the specified profile.

## Declaration

```c
CMError CMGetScriptProfileDescription (
   CMProfileRef prof,
   Str255 name,
   ScriptCode *code
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The element data of the text description tag (which has the signature `'desc'` or constant `cmSigProfileDescriptionType`, defined in the `CMICCProfile.h` header file) specifies the profile name and script code. The `name` parameter returns the profile name as a Pascal string. Use this function so that your application does not need to obtain and parse the element data, which contains other information. 

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) to the profile whose profile name and script code are obtained. 
- `name`: A pointer to a name string. On return, the profile name. 
- `code`: A pointer to a script code. On return, the script code. 

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
- [CMGetProfileDescriptions](./api-1805034-cmgetprofiledescriptions.md)
  Obtains the description tag data for a specified profile.
- [CMSetProfileDescriptions](./api-1805039-cmsetprofiledescriptions.md)
  Sets the description tag data for a specified profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805029-cmgetscriptprofiledescription)*