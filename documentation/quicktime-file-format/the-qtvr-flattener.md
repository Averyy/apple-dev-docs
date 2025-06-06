# The QTVR flattener

**Framework**: Quicktime File Format

Optimize a movie for delivery over the web.

#### Overview

The QTVR Flattener is a movie export component that converts an existing QuickTime VR single node movie into a new movie that is optimized for the Web. Not only does the flattener reorder the media samples, but for panoramas it also creates a small preview of the panorama. When viewed on the Web, this preview appears after 5% to 10% of the movie data has been downloaded, allowing users to see a lower-resolution version of the panorama.

Using the QTVR flattener from your application is quite easy. After you have created the QuickTime VR movie, you simply open the QTVR Flattener component and call the `MovieExportToFile` routine as shown in the following listing.

```c
ComponentDescription desc;
Component flattener;
ComponentInstance qtvrExport = nil;
desc.componentType = MovieExportType;
desc.componentSubType = MovieFileType;
desc.componentManufacturer = QTVRFlattenerType;
flattener = FindNextComponent(nil, &desc);
if (flattener) qtvrExport = OpenComponent (flattener);
if (qtvrExport)
    MovieExportToFile (qtvrExport, &myFileSpec, myQTVRMovie,  nil, 0, 0);
```

The code fragment shown in the preceeding listing creates a flattened movie file specified by the `myFileSpec` parameter. If your QuickTime VR movie is a panorama, the flattened movie file includes a quarter size, blurred JPEG, compressed preview of the panorama image.

> **Note**: The constants `MovieExportType` and `MovieFileType` used in the preceeding listing are defined in header files QuickTimeComponents.h and Movies.h respectively and are defined as `'spit'` and `'MooV'`.

You can present users with the QTVR Flattener’s own dialog box to allow them to choose options such as how to compress the preview image or to select a separate preview image file. Use the following code to show the dialog box:

```c
err = MovieExportDoUserDialog (qtvrExport, myQTVRMovie,  nil, 0, 0,  &cancel);
```

If the user cancels the dialog box, then the Boolean cancel is set to `true`.

If you do not want to present the user with the flattener’s dialog box, you can communicate directly with the component by using the `MovieExportSetSettingsFromAtomContainer` routine as described in the following paragraphs.

If you want to specify a preview image other than the default, you need to create a special atom container and then call `MovieExportSetSettingsFromAtomContainer` before calling `MovieExportToFile`. You can specify how to compress the image, what resolution to use, and you can even specify your own preview image file to be used. The atom container you pass in can have various atoms that specify certain export options. These atoms must all be children of a flattener settings parent atom.

The preview resolution atom is a 16-bit value that allows you to specify the resolution of the preview image. This value, which defaults to `kQTVRQuarterRes`, indicates how much to reduce the preview image.

The blur preview atom is a Boolean value that indicates whether to blur the image before compressing. Blurring usually results in a much more highly compressed image. The default value is `true`.

The create preview atom is a Boolean value that indicates whether a preview image should be created. The default value is `true`.

The import preview atom is a Boolean value that is used to indicate that the preview image should be imported from an external file rather than generated from the image in the panorama file itself. This allows you to have any image you want as the preview for the panorama. You can specify which file to use by also including the import specification atom, which is an `FSSpec` data structure that identifies the image file. If you do not include this atom, then the flattener presents the user with a dialog box asking the user to select a file. The default for import preview is `false`. If an import file is used, the image is used at its natural size and the resolution setting is ignored.

## See Also

- [Sample atom container for the QTVR flattener](sample_atom_container_for_the_qtvr_flattener.md)
  Specify an import preview file for the flattener with atoms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/the_qtvr_flattener)*