# Image Metadata Attribute Keys

**Framework**: Core Services

Metadata attribute keys that are common to image files.

## Topics

### Constants
- [let kMDItemPixelHeight: CFString!](kmditempixelheight.md)
  The height, in pixels, of the contents. For example, the image height or the video frame height. A CFNumber.
- [let kMDItemPixelWidth: CFString!](kmditempixelwidth.md)
  The width, in pixels, of the contents. For example, the image width or the video frame width. A CFNumber.
- [let kMDItemPixelCount: CFString!](kmditempixelcount.md)
  The total number of pixels in the contents. Same as [`kMDItemPixelWidth`](kmditempixelwidth.md) x [`kMDItemPixelHeight`](kmditempixelheight.md). A CFNumber.
- [let kMDItemColorSpace: CFString!](kmditemcolorspace.md)
  The color space model used by the document contents. For example, “RGB”, “CMYK”, “YUV”, or “YCbCr”. A CFString.
- [let kMDItemBitsPerSample: CFString!](kmditembitspersample.md)
  The number of bits per sample. For example, the bit depth of an image (8-bit, 16-bit etc...) or the bit depth per audio sample of uncompressed audio data (8, 16, 24, 32, 64, etc..). A CFNumber.
- [let kMDItemFlashOnOff: CFString!](kmditemflashonoff.md)
  Indicates if a camera flash was used. A CFNumber.
- [let kMDItemFocalLength: CFString!](kmditemfocallength.md)
  The actual focal length of the lens, in millimeters.  A CFNumber.
- [let kMDItemAcquisitionMake: CFString!](kmditemacquisitionmake.md)
  The manufacturer of the device used to aquire the document contents. A CFString.
- [let kMDItemAcquisitionModel: CFString!](kmditemacquisitionmodel.md)
  The model of the device used to aquire the document contents. For example, 100, 200, 400, etc. A CFString.
- [let kMDItemISOSpeed: CFString!](kmditemisospeed.md)
  The ISO speed used to acquire the document contents. A CFNumber.
- [let kMDItemOrientation: CFString!](kmditemorientation.md)
  The orientation of the document contents. Possible values are 0 (landscape) and 1 (portrait). A CFNumber.
- [let kMDItemLayerNames: CFString!](kmditemlayernames.md)
  The names of the layers in the file. A CFArray of CFStrings.
- [let kMDItemWhiteBalance: CFString!](kmditemwhitebalance.md)
  The white balance setting used to acquire the document contents. Possible values are 0 (auto white balance) and 1 (manual). A CFNumber.
- [let kMDItemAperture: CFString!](kmditemaperture.md)
  The aperture setting used to acquire the document contents. This unit is the APEX value. A CFNumber.
- [let kMDItemProfileName: CFString!](kmditemprofilename.md)
  The name of the color profile used by the document contents. A CFString.
- [let kMDItemResolutionWidthDPI: CFString!](kmditemresolutionwidthdpi.md)
  Resolution width, in DPI, of this image. A CFNumber.
- [let kMDItemResolutionHeightDPI: CFString!](kmditemresolutionheightdpi.md)
  Resolution height, in DPI, of this image. A CFNumber.
- [let kMDItemExposureMode: CFString!](kmditemexposuremode.md)
  The exposure mode used to acquire the document contents. A CFNumber.
- [let kMDItemExposureTimeSeconds: CFString!](kmditemexposuretimeseconds.md)
  The exposure time, in seconds, used to acquire the document contents. A CFNumber.
- [let kMDItemEXIFVersion: CFString!](kmditemexifversion.md)
  The version of the EXIF header used to generate the metadata. A CFString.
- [let kMDItemAlbum: CFString!](kmditemalbum.md)
  The title for a collection of media. This is analagous to a record album, or photo album. A CFString.
- [let kMDItemHasAlphaChannel: CFString!](kmditemhasalphachannel.md)
  Indicates if this image file has an alpha channel.  A CFBoolean.
- [let kMDItemRedEyeOnOff: CFString!](kmditemredeyeonoff.md)
  Indicates if red-eye reduction was used to take the picture. A CFBoolean.
- [let kMDItemMeteringMode: CFString!](kmditemmeteringmode.md)
  The metering mode used to take the image. A CFString.
- [let kMDItemMaxAperture: CFString!](kmditemmaxaperture.md)
  The smallest f-number of the lens. Ordinarily it is given in the range of 00.00 to 99.99. A CFNumber.
- [let kMDItemFNumber: CFString!](kmditemfnumber.md)
  The diameter of the diaphragm aperture in terms of the effective focal length of the lens.
- [let kMDItemExposureProgram: CFString!](kmditemexposureprogram.md)
  The class of the exposure program used by the camera to set exposure when the image is taken. Possible values include: Manual, Normal, and Aperture priority. A CFString.
- [let kMDItemExposureTimeString: CFString!](kmditemexposuretimestring.md)
  The time of the exposure. A CFString.
- [let kMDItemEXIFGPSVersion: CFString!](kmditemexifgpsversion.md)
   The version of GPSInfoIFD in EXIF used to generate the metadata. A CFString.
- [let kMDItemAltitude: CFString!](kmditemaltitude.md)
   The altitude of the item in meters above sea level, expressed using the WGS84 datum.  Negative values lie below sea level. A CFString.
- [let kMDItemLatitude: CFString!](kmditemlatitude.md)
   The latitude of the item in degrees north of the equator, expressed using the WGS84 datum.  Negative values lie south of the equator. A CFString.
- [let kMDItemLongitude: CFString!](kmditemlongitude.md)
   The longitude of the item in degrees east of the prime meridian,  expressed using the WGS84 datum.  Negative values lie west of the prime meridian. A CFString.
- [let kMDItemTimestamp: CFString!](kmditemtimestamp.md)
   The timestamp on the item.  This generally is used to indicate the time at which the event captured by the item took place. A CFString.
- [let kMDItemSpeed: CFString!](kmditemspeed.md)
   The speed of the item, in kilometers per hour. A CFString.
- [let kMDItemGPSTrack: CFString!](kmditemgpstrack.md)
   The direction of travel of the item, in degrees from true north. A CFString.
- [let kMDItemImageDirection: CFString!](kmditemimagedirection.md)
   The direction of the item's image, in degrees from true north. A CFString.
- [let kMDItemNamedLocation: CFString!](kmditemnamedlocation.md)
   The name of the location or point of interest associated with the item. The name may be user provided. A CFString.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/file_metadata/mditem/image_metadata_attribute_keys)*