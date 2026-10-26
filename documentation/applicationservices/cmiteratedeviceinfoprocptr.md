# CMIterateDeviceInfoProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

Defines a pointer to a function that iterates through device information available on the system.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef OSErr (*CMIterateDeviceInfoProcPtr)(const CMDeviceInfo *deviceInfo, void *refCon);
```

#### Return Value

An `OSErr` value. 

## Parameters

- `deviceData`: 
- `refCon`: 

## See Also

### Callbacks
- [CMBitmapCallBackProcPtr](./cmbitmapcallbackprocptr.md)
  Defines a pointer to a bitmap callback function that function reports on the progress of a color-matching or color-checking session being performed for a bitmap or a pixel map.
- [CMConcatCallBackProcPtr](./cmconcatcallbackprocptr.md)
  Defines a pointer to a progress-monitoring function that the ColorSync Manager calls during lengthy color world processing.
- [CMCountImageProfilesProcPtr](./colorsync_manager/cmcountimageprofilesprocptr.md)
  Defines a pointer to a function that obtains a count of the number of embedded profiles for a given image.
- [CMEmbedImageProcPtr](./colorsync_manager/cmembedimageprocptr.md)
  Defines a pointer to a function that embeds an image with an ICC profile.
- [CMFlattenProcPtr](./cmflattenprocptr.md)
  Defines a pointer to a data transfer callback function that transfers profile data from the format for embedded profiles to disk file format or vice versa.
- [CMGetImageSpaceProcPtr](./colorsync_manager/cmgetimagespaceprocptr.md)
  Defines a pointer to a function that obtains the signature of the data color space in which the color values of colors in an image are expressed.
- [CMGetIndImageProfileProcPtr](./colorsync_manager/cmgetindimageprofileprocptr.md)
  Defines a pointer to a function that obtains a specific embedded profile for a given image.
- [CMIterateDeviceProfileProcPtr](./cmiteratedeviceprofileprocptr.md)
  Defines a pointer to a function that iterates through the device profiles available on the system.
- [CMLinkImageProcPtr](./colorsync_manager/cmlinkimageprocptr.md)
  Defines a pointer to a function that matches an image file with a device link profile.
- [CMMatchImageProcPtr](./colorsync_manager/cmmatchimageprocptr.md)
  Defines a pointer to a function that color matches an image file.
- [CMMIterateProcPtr](./cmmiterateprocptr.md)
  Defines a pointer to a function that iterates through color management modules installed on the system.
- [CMProofImageProcPtr](./colorsync_manager/cmproofimageprocptr.md)
  Defines a pointer to a function that proofs an image.
- [CMProfileIterateProcPtr](./cmprofileiterateprocptr.md)
  Defines a pointer to a profile iteration callback function that the ColorSync Manager calls for each found profile file as it iterates over the available profiles.
- [CMSetIndImageProfileProcPtr](./colorsync_manager/cmsetindimageprofileprocptr.md)
  Defines a pointer to a function that sets a specific embedded profile for a given image.
- [CMUnembedImageProcPtr](./colorsync_manager/cmunembedimageprocptr.md)
  Defines a pointer to a function that umembeds an ICC profile from an image.
- [CMValidImageProcPtr](./colorsync_manager/cmvalidimageprocptr.md)
  Defines a pointer to a function that validates a specified image file.
- [CountImageProfilesProcPtr](./colorsync_manager/countimageprofilesprocptr.md)
  Defines a pointer to a function that counts the number of embedded profiles for a given image. 
- [EmbedImageProcPtr](./colorsync_manager/embedimageprocptr.md)
  Defines a pointer to an embed-image function.
- [GetImageSpaceProcPtr](./colorsync_manager/getimagespaceprocptr.md)
  Defines a pointer to a get-image-space function.
- [GetIndImageProfileProcPtr](./colorsync_manager/getindimageprofileprocptr.md)
  Defines a pointer to a function that obtains a color profile for an individual image.
- [MatchImageProcPtr](./colorsync_manager/matchimageprocptr.md)
  Defines a pointer to a match-image function.
- [SetIndImageProfileProcPtr](./colorsync_manager/setindimageprofileprocptr.md)
  Defines a pointer to a function that sets a color profile for an individual image.
- [UnembedImageProcPtr](./colorsync_manager/unembedimageprocptr.md)
  Defines a pointer to an umembed-image function.
- [ValidateImageProcPtr](./colorsync_manager/validateimageprocptr.md)
  Defines a pointer to a validate-image function.
- [ValidateSpaceProcPtr](./colorsync_manager/validatespaceprocptr.md)
  Defines a pointer to a validate-space function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmiteratedeviceinfoprocptr)*