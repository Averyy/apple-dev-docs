# CMProofImageProcPtr

**Framework**: Application Services  
**Kind**: tdef

Defines a pointer to a function that proofs an image.

## Declaration

```c
typedef CMError (*CMProofImageProcPtr)
(
   const FSSpec * specFrom,
   const FSSpec * specInto,
   Boolean repl,
   UInt32 qual,
   CMProfileRef srcProf,
   UInt32 srcIntent,
   CMProfileRef dstProf,
   CMProfileRef prfProf
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295). 

## Parameters

- `specFrom`: See the File Manager documentation for a description of the `FSSpec` data type.
- `specInto`: See the File Manager documentation for a description of the `FSSpec` data type.
- `repl`: 
- `qual`: 
- `srcProf`: 
- `srcIntent`: 
- `dstProf`: 
- `prfProf`: 

## See Also

### Callbacks
- [CMBitmapCallBackProcPtr](../cmbitmapcallbackprocptr.md)
  Defines a pointer to a bitmap callback function that function reports on the progress of a color-matching or color-checking session being performed for a bitmap or a pixel map.
- [CMConcatCallBackProcPtr](../cmconcatcallbackprocptr.md)
  Defines a pointer to a progress-monitoring function that the ColorSync Manager calls during lengthy color world processing.
- [CMCountImageProfilesProcPtr](./cmcountimageprofilesprocptr.md)
  Defines a pointer to a function that obtains a count of the number of embedded profiles for a given image.
- [CMEmbedImageProcPtr](./cmembedimageprocptr.md)
  Defines a pointer to a function that embeds an image with an ICC profile.
- [CMFlattenProcPtr](../cmflattenprocptr.md)
  Defines a pointer to a data transfer callback function that transfers profile data from the format for embedded profiles to disk file format or vice versa.
- [CMGetImageSpaceProcPtr](./cmgetimagespaceprocptr.md)
  Defines a pointer to a function that obtains the signature of the data color space in which the color values of colors in an image are expressed.
- [CMGetIndImageProfileProcPtr](./cmgetindimageprofileprocptr.md)
  Defines a pointer to a function that obtains a specific embedded profile for a given image.
- [CMIterateDeviceInfoProcPtr](../cmiteratedeviceinfoprocptr.md)
  Defines a pointer to a function that iterates through device information available on the system.
- [CMIterateDeviceProfileProcPtr](../cmiteratedeviceprofileprocptr.md)
  Defines a pointer to a function that iterates through the device profiles available on the system.
- [CMLinkImageProcPtr](./cmlinkimageprocptr.md)
  Defines a pointer to a function that matches an image file with a device link profile.
- [CMMatchImageProcPtr](./cmmatchimageprocptr.md)
  Defines a pointer to a function that color matches an image file.
- [CMMIterateProcPtr](../cmmiterateprocptr.md)
  Defines a pointer to a function that iterates through color management modules installed on the system.
- [CMProfileIterateProcPtr](../cmprofileiterateprocptr.md)
  Defines a pointer to a profile iteration callback function that the ColorSync Manager calls for each found profile file as it iterates over the available profiles.
- [CMSetIndImageProfileProcPtr](./cmsetindimageprofileprocptr.md)
  Defines a pointer to a function that sets a specific embedded profile for a given image.
- [CMUnembedImageProcPtr](./cmunembedimageprocptr.md)
  Defines a pointer to a function that umembeds an ICC profile from an image.
- [CMValidImageProcPtr](./cmvalidimageprocptr.md)
  Defines a pointer to a function that validates a specified image file.
- [CountImageProfilesProcPtr](./countimageprofilesprocptr.md)
  Defines a pointer to a function that counts the number of embedded profiles for a given image. 
- [EmbedImageProcPtr](./embedimageprocptr.md)
  Defines a pointer to an embed-image function.
- [GetImageSpaceProcPtr](./getimagespaceprocptr.md)
  Defines a pointer to a get-image-space function.
- [GetIndImageProfileProcPtr](./getindimageprofileprocptr.md)
  Defines a pointer to a function that obtains a color profile for an individual image.
- [MatchImageProcPtr](./matchimageprocptr.md)
  Defines a pointer to a match-image function.
- [SetIndImageProfileProcPtr](./setindimageprofileprocptr.md)
  Defines a pointer to a function that sets a color profile for an individual image.
- [UnembedImageProcPtr](./unembedimageprocptr.md)
  Defines a pointer to an umembed-image function.
- [ValidateImageProcPtr](./validateimageprocptr.md)
  Defines a pointer to a validate-image function.
- [ValidateSpaceProcPtr](./validatespaceprocptr.md)
  Defines a pointer to a validate-space function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/cmproofimageprocptr)*