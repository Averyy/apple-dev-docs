# CMFlattenProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

Defines a pointer to a data transfer callback function that transfers profile data from the format for embedded profiles to disk file format or vice versa.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias CMFlattenProcPtr = (Int32, UnsafeMutablePointer<Int>?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSErr
```

```c
typedef OSErr (*CMFlattenProcPtr)(SInt32 command, long *size, void *data, void *refCon);
```

## Return Value

A result code. See [Result Codes](./colorsync_manager.md#1670295).

## Discussion

IThis callback can be used, for example, by PostScript functions to transfer data from a profile to text format usable by a PostScript driver. Starting in ColorSync version 2.5, the ColorSync Manager calls your data transfer function directly, without going through the preferred, or any, CMM. So any references to the CMM in the discussion that follows are applicable only to versions of ColorSync prior to version 2.5. Where the discussion does not involve CMMs, it is applicable to all versions of ColorSync.

Your `MyCMFlattenCallback` function is called to flatten and unflatten profiles or to transfer PostScript-related data from a profile to the PostScript format to send to an application or device driver. 

The ColorSync Manager and the CMM communicate with the `MyCMFlattenCallback` function using the command parameter to identify the operation to perform. To read and write profile data, your function must support the following commands: `cmOpenReadSpool`, `cmOpenWriteSpool`, `cmReadSpool`, `cmWriteSpool`, and `cmCloseSpool`.

You determine the behavior of your `MyCMFlattenCallback` function. The following sections describe how your function might handle the flattening and unflattening processes.

Flattening a Profile:

The ColorSync Manager calls the specified profile’s preferred CMM when an application calls the `CMFlattenProfile` function to transfer profile data embedded in a graphics document. 

The ColorSync Manager determines if the CMM supports the `CMFlattenProfile` function. If so, the ColorSync Manager dispatches the `CMFlattenProfile` function to the CMM. If not, ColorSync calls the default CMM, dispatching the `CMFlattenProfile` function to it.

The CMM communicates with the `MyCMFlattenCallback` function using a command parameter to identify the operation to perform. The CMM calls your function as often as necessary, passing to it on each call any data transferred to the CMM from the `CMFlattenProfile` function’s `refCon` parameter. 

The ColorSync Manager calls your function with the following sequence of commands: `cmOpenWriteSpool`, `cmWriteSpool`, and `cmCloseSpool`. Here is how you should handle these commands:

-  When the CMM calls your function with the `cmOpenWriteSpool` command, you should perform any initialization required to write profile data you receive from the CMM to a buffer or file.  
-  The CMM will call your function with the `cmWriteSpool` command as many times as necessary to transfer all the profile data to you. Each time you are called, you should receive the data and write it to your buffer or file, returning in the `size` parameter the number of bytes of data you actually accepted. 
-  When the CMM calls your function with the `cmCloseSpool` command, you should perform any required cleanup processes.  

As part of this process, your function can embed the profile data in a graphics document, for example, a PICT file or a TIFF file. For example, your `MyCMFlattenCallback` function can call the QuickDraw `PicComment` function to embed the flattened profile in a picture.

Unflattening a Profile:

When an application calls the `CMUnflattenProfile` function to transfer a profile that is embedded in a graphics document to an independent disk file, the ColorSync Manager calls your `MyCMFlattenCallback` function with the following sequence of commands: `cmOpenReadSpool`, `cmReadSpool`, `cmCloseSpool`. Here is how you should handle these commands:

-  When the ColorSync Manager calls your function with the `cmOpenReadSpool` command, you should perform any initialization required to read from the embedded profile format. 
-  The ColorSync Manager calls your function with the `cmReadSpool` command as many times as necessary, directing your function to extract the profile data from the embedded format in the image file and return it to the ColorSync Manager in the `data` buffer. For each call, the ColorSync Manager specifies in the `size` parameter the number of bytes of data you should return. Each time your function is called it should read and return the requested data; it should also specify in the `size` parameter the actual number of bytes of data it returns. 
-  When the ColorSync Manager calls your function with the `cmCloseSpool` command, you should perform any required cleanup processes. 

## Parameters

- `command`: The command with which the `MyCMFlattenCallback` function is called. This command specifies the operation the function is to perform. 
- `size`: A pointer to a size value. On input, the size in bytes of the data to transfer. On return, the size of the data actually transferred.
- `data`: A pointer to the buffer supplied by the ColorSync Manager to use for the data transfer. 
- `refCon`: A pointer to a reference constant that holds the application data passed in from the functions [CMFlattenProfile](./colorsync_manager/api-1804897-cmflattenprofile.md), [NCMUnflattenProfile](./colorsync_manager/api-1804901-ncmunflattenprofile.md), [CMGetPS2ColorRenderingVMSize](./colorsync_manager/api-1805206-cmgetps2colorrenderingvmsize.md), [CMGetPS2ColorRenderingIntent](./colorsync_manager/api-1805196-cmgetps2colorrenderingintent.md), or [CMFlattenProfile](./colorsync_manager/api-1804897-cmflattenprofile.md). Each time the CMM calls your `MyCMFlattenCallback` function, it passes this data to the function.

  Starting in ColorSync version 2.5, the ColorSync Manager calls your function directly, without going through the preferred, or any, CMM.

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
- [CMGetImageSpaceProcPtr](./colorsync_manager/cmgetimagespaceprocptr.md)
  Defines a pointer to a function that obtains the signature of the data color space in which the color values of colors in an image are expressed.
- [CMGetIndImageProfileProcPtr](./colorsync_manager/cmgetindimageprofileprocptr.md)
  Defines a pointer to a function that obtains a specific embedded profile for a given image.
- [CMIterateDeviceInfoProcPtr](./cmiteratedeviceinfoprocptr.md)
  Defines a pointer to a function that iterates through device information available on the system.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmflattenprocptr)*