# CIDetectorFocalLength

**Framework**: Core Image  
**Kind**: data

An option identifying the focal length in pixels used in capturing images to be processed by the detector.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let CIDetectorFocalLength: String
```

#### Discussion

The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object whose value is a floating-point number. Use this option with the [`CIDetectorTypeRectangle`](cidetectortyperectangle.md) detector type to control the effect of the [`CIDetectorAspectRatio`](cidetectoraspectratio.md) option on feature detection.

This option’s value can be `0.0`, `-1.0`, or any positive value:

- The special value of `-1.0` (the default) disables the aspect ratio test for the returned rectangle.
- The special value of `0.0` enables a less precise test of aspect ratio that approximates an orthographic (non-perspective) projection. Use this value if you want to specify the aspect ratio of the rectangle via the [`CIDetectorAspectRatio`](cidetectoraspectratio.md) option, but have no means of determining the value for the focal length in pixels. See below for a method to compute an approximate value for the focal length in pixels.
- Any other value specifies the camera focal length, in pixels, allowing the aspect ratio specification to account for perspective distortion of rectangles in the input image.

If you know the diagonal field of view of the camera (the scene angle subtended by the diagonal corners of an image), you can use the following formula to compute an approximate focal length in pixels:

`focal_length_pixels = (image_diagonal_pixels/2)/tan(FOV/2)`

In this formula, `image_diagonal_pixels` is the length (in pixels) of the image diagonal of the maximum resolution of the camera sensor. (For example, this value is 4080 pixels for a 3264 x 2448 (8 megapixel) sensor, and 5000 pixels for a 4096x3024 (12 megapixel) sensor.)

To measure diagonal field of view, put the camera on a tripod so that it is perpendicular to a surface and the center of the image is oriented on a mark on the surface. Measure the distance from the mark to one of the corner points of the image (`Y`). Measure the distance from the camera to the surface (`Z`).  The field of view is then `2*arctan(Y/Z)`.

You must specify this value in terms of the maximum sensor resolution. If the supplied [`CIImage`](ciimage.md) has been scaled relative relative to the maximum sensor resolution, the supplied focal length must also be similarly scaled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetectorfocallength)*