# setROISelector(_:)

**Framework**: Core Image  
**Kind**: instm

Sets the selector Core Image uses to query the region of interest for image processing with the kernel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setROISelector(_ method: Selector)
```

#### Discussion

> ❗ **Important**: This method is not supported in iOS, and not recommended in macOS 10.11 and later. Supply and use a block-based ROI callback instead using the [`apply(extent:roiCallback:arguments:)`](cikernel/1438243-apply.md) method. The discussion below applies only to OS X v10.10 and earlier.

This method is not supported in iOS, and not recommended in macOS 10.11 and later. Supply and use a block-based ROI callback instead using the [`apply(extent:roiCallback:arguments:)`](cikernel/1438243-apply.md) method. The discussion below applies only to OS X v10.10 and earlier.

When applying a filter kernel, the region of interest (ROI) is the area of source image pixels that must be processed to produce a given area of destination image pixels. For a more detailed definition, see [`The Region of Interest`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_advanced_concepts/ci.advanced_concepts.html#//apple_ref/doc/uid/TP30001185-CH9-SW12).

The `aMethod` argument must use the signature that is defined for the `regionOf:destRect:userInfo:` method, which is as follows:

`- (CGRect) regionOf:(int)samplerIndex destRect:(CGRect)r userInfo:obj;`

where: 

- `samplerIndex` defines the sampler to query
- `destRect` is the extent of the region, in working space coordinates, to render.
- `userInfo` is the object associated with the `kCIApplyOptionUserInfo` option when the kernel is applied to its arguments (with the [`apply(_:arguments:options:)`](cifilter/1438077-apply.md) method of a [`CIFilter`](cifilter.md) object using the kernel). The `userInfo` is important because instance variables can’t be used by the defining class. Instance variables must be passed through the `userInfo` argument.

The `regionOf:destRect:userInfo:` method of the CIFilter object is called by the framework. This method returns the rectangle that contains the region of the sampler that the kernel needs to render the specified destination rectangle. 

A sample `regionOf:destRect:userInfo:` method might look as follows:

```occ
- (CGRect)regionOf:(int)sampler destRect:(CGRect)r userInfo:params
{
  float scale = fabs ([params X]);
  return CGRectInset (r, scale * -1.3333, scale * -1.3333);
}
```

If your kernel does not need the image at `index` to produce output in the rectangle `rect`, your method should return [`null`](https://developer.apple.com/documentation/corefoundation/cgrect/null).

In the filter code, you set the selector using the following:

`[kernel setROISelector:@selector(regionOf:destRect:userInfo:)`]

Alternatively, use the [`apply(extent:roiCallback:arguments:)`](cikernel/1438243-apply.md) method to directly apply a kernel to create an output image, specifying the ROI callback as a block or closure.

## Parameters

- `aMethod`: A selector name. 

## See Also

- [func apply(extent: CGRect, roiCallback: CIKernelROICallback, arguments: [Any]) -> CIImage?](cikernel/1438243-apply.md)
  Creates a new image using the kernel and specified arguments.
- [func apply(CIKernel, arguments: [Any]?, options: [String : Any]?) -> CIImage?](cifilter/1438077-apply.md)
  Produces a  object by applying arguments to a kernel function and using options to control how the kernel function is evaluated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikernel/1437691-setroiselector)*