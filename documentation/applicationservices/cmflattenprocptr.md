# CMFlattenProcPtr

**Framework**: Application Services  
**Kind**: tdef

Defines a pointer to a data transfer callback function that transfers profile data from the format for embedded profiles to disk file format or vice versa.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias CMFlattenProcPtr = (Int32, UnsafeMutablePointer<Int>?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](colorsync_manager#1670295.md).

#### Discussion

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

- `command`: The command with which the   function is called. This command specifies the operation the function is to perform. 
- `size`: A pointer to a size value. On input, the size in bytes of the data to transfer. On return, the size of the data actually transferred.
- `data`: A pointer to the buffer supplied by the ColorSync Manager to use for the data transfer. 
- `refCon`: Starting in ColorSync version 2.5, the ColorSync Manager calls your function directly, without going through the preferred, or any, CMM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmflattenprocptr)*