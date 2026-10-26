# CMLinkImage

**Framework**: Application Services  
**Kind**: func

Matches an image file with a device link profile. 

## Declaration

```c
CMError CMLinkImage (
   const FSSpec *specFrom,
   const FSSpec *specInto,
   Boolean repl,
   UInt32 qual,
   CMProfileRef lnkProf,
   UInt32 lnkIntent
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Parameters

- `specFrom`: A file specification for the image file. See the File Manager documentation for a description of the `FSSpec` data type.
- `specInto`: If this parameter is a file, it specifies the resulting image. If this parameter is a folder, it specifies the location of the resulting image which will have the same name as the original file. If this parameter is not provided, the original file is modified. See the File Manager documentation for a description of the `FSSpec` data type.
- `repl`: If a file with the same name already exists, it will be replaced if this parameter is set to true. 
- `qual`: The optional quality for the match—normal, draft or best (`cmNormalMode`, `cmDraftMode`, or `cmBestMode`). 
- `lnkProf`: The device link profile for the match. 
- `lnkIntent`: The rendering intent for the match—perceptual intent, relative colorimetric intent, saturation intent , or absolute colorimetric intent                   (`cmPerceptual`, `cmRelativecolorimetric`, `cmSaturation`, or `cmAbsoluteColorimetric` ). 

## See Also

### Working With Image Files
- [CMValidImage](./api-1805264-cmvalidimage.md)
  Validates the specified image file.
- [CMGetImageSpace](./api-1805267-cmgetimagespace.md)
  Returns the signature of the data color space in which the color values of colors in an image are expressed. 
- [CMEmbedImage](./api-1805269-cmembedimage.md)
  Embeds an image with an ICC profile. 
- [CMUnembedImage](./api-1805271-cmunembedimage.md)
  Removes any ICC profiles embedded in an image.
- [CMMatchImage](./api-1805273-cmmatchimage.md)
  Color matches an image file.
- [CMProofImage](./api-1805276-cmproofimage.md)
  Proofs an image.
- [CMCountImageProfiles](./api-1805281-cmcountimageprofiles.md)
  Obtains a count of the number of embedded profiles for a given image. 
- [CMGetIndImageProfile](./api-1805284-cmgetindimageprofile.md)
  Obtains a specific embedded profile for a given image. 
- [CMSetIndImageProfile](./api-1805286-cmsetindimageprofile.md)
  Sets a specific embedded profile for a given image. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805278-cmlinkimage)*