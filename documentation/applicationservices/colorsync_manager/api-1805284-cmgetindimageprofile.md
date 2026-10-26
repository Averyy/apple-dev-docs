# CMGetIndImageProfile

**Framework**: Application Services  
**Kind**: func

Obtains a specific embedded profile for a given image. 

## Declaration

```c
CMError CMGetIndImageProfile (
   const FSSpec *spec,
   UInt32 index,
   CMProfileRef *prof
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Parameters

- `spec`: A file specification for the image file. See the File Manager documentation for a description of the `FSSpec` data type.
- `index`: The numeric index of the profile to return. 
- `prof`: On output, points to the profile. 

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
- [CMLinkImage](./api-1805278-cmlinkimage.md)
  Matches an image file with a device link profile. 
- [CMCountImageProfiles](./api-1805281-cmcountimageprofiles.md)
  Obtains a count of the number of embedded profiles for a given image. 
- [CMSetIndImageProfile](./api-1805286-cmsetindimageprofile.md)
  Sets a specific embedded profile for a given image. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805284-cmgetindimageprofile)*