# MPSCNNPooling

**Framework**: Metal Performance Shaders  
**Kind**: class

A pooling kernel.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNPooling
```

#### Overview

Pooling is a form of non-linear sub-sampling. Pooling partitions the input image into a set of rectangles (overlapping or non-overlapping) and, for each such sub-region, outputs a value. The pooling operation is used in computer vision to reduce the dimensionality of intermediate representations.

The encode methods in the [`MPSCNNKernel`](mpscnnkernel.md) class can be used to encode an [`MPSCNNPooling`](mpscnnpooling.md) object to a [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer) object. The exact location of the pooling window for each output value is determined as follows:

- The pooling window center for the first (top left) output pixel of the clip rectangle is at spatial coordinates `(offset.x, offset.y)` in the input image.
- From this, the top left corner of the pooling window is at `(offset.x - floor(kernelWidth/2)`, `offset.y - floor(kernelHeight/2))` and extends `(kernelWidth, kernelHeight)` pixels to the right and down direction, which means that the last pixel to be included into the pooling window is at `(offset.x + floor((kernelWidth-1)/2)`, `offset.y + floor((kernelHeight-1)/2))`, so that for even kernel sizes the pooling window extends one pixel more into the left and up direction.
- The following pooling windows can be then easily deduced from the first one by simple shifting the source coordinates according to the values of the `strideInPixelsX` and `strideInPixelsY` properties.

For example,  the pooling window center `w(x,y)` for the output value at coordinate `(x,y)` of the destination clip rectangle (`(x,y)` computed with regard to clipping rectangle origin) is at `w(x,y) = (offset.x + strideInPixelsX * x , offset.y + strideInPixelsY * y)`.

Quite often it is desirable to distribute the pooling windows as evenly as possible in the input image. As explained above, if the `offset` is zero, then the center of the first pooling window is at the top left corner of the input image, which means that the left and top stripes of the pooling window are read from outside the input image boundaries (when filter size is larger than unity). Also it may mean that some values from the bottom and right stripes are not included at all in the pooling, resulting in loss of valuable information.

A scheme used in some common libraries is to shift the source `offset` according to the following formula:

- `offset.xy += {(int)ceil(((L.xy - 1) % s.xy) / 2)}`, for odd `f.xy`
- `offset.xy += {(int)floor(((L.xy - 1) % s.xy) / 2) + 1},` for even `f.xy`

Where `L` is the size of the input image (or more accurately the size corresponding to the scaled `clipRect` value in source coordinates, which commonly coincides with the source image itself), `s.xy` is `(``strideInPixelsX`, `strideInPixelsY``)` and `f.xy` is `(kernelWidth, kernelHeight)`.

This offset distributes the pooling window centers evenly in the effective source `clipRect`, when the output size is rounded up with regards to stride (`output size = ceil(input size / stride)`) and is commonly used in CNN libraries (for example  uses this offset scheme in its maximum pooling implementation `tf.nn.max_pool` with `'S``AME``'` - padding, for `'VALID'` padding one can simply set `offset.xy += floor(f.xy/2)` to get the first pooling window inside the source image completely).

For an [`MPSCNNPoolingMax`](mpscnnpoolingmax.md) object, the way the input image borders are handled can become important: if there are negative values in the source image near the borders of the image and the pooling window crosses the borders, then using a [`MPSImageEdgeMode.zero`](mpsimageedgemode/zero.md) edge modemay cause the maximum pooling operation to override the negative input data values with zeros coming from outside the source image borders, resulting in large boundary effects. A simple way to avoid this is to use a [`MPSImageEdgeMode.clamp`](mpsimageedgemode/clamp.md) edge mode, which for an [`MPSCNNPoolingMax`](mpscnnpoolingmax.md) object effectively causes all pooling windows to remain within the source image.

## Topics

### Instance Methods
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnpooling/init(coder:device:).md)
  Initializes a pooling filter.
- [convenience init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int)](mpscnnpooling/init(device:kernelwidth:kernelheight:).md)
  Initializes a pooling filter.
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int)](mpscnnpooling/init(device:kernelwidth:kernelheight:strideinpixelsx:strideinpixelsy:).md)
  Initializes a pooling filter.

## Relationships

### Inherits From
- [MPSCNNKernel](mpscnnkernel.md)
### Inherited By
- [MPSCNNDilatedPoolingMax](mpscnndilatedpoolingmax.md)
- [MPSCNNPoolingAverage](mpscnnpoolingaverage.md)
- [MPSCNNPoolingL2Norm](mpscnnpoolingl2norm.md)
- [MPSCNNPoolingMax](mpscnnpoolingmax.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPSCNNPoolingAverage](mpscnnpoolingaverage.md)
  An average pooling filter.
- [class MPSCNNPoolingAverageGradient](mpscnnpoolingaveragegradient.md)
  A gradient average pooling filter.
- [class MPSCNNPoolingL2Norm](mpscnnpoolingl2norm.md)
  An L2-norm pooling filter.
- [class MPSCNNPoolingMax](mpscnnpoolingmax.md)
  A max pooling filter.
- [class MPSCNNDilatedPoolingMax](mpscnndilatedpoolingmax.md)
  A dilated max pooling filter.
- [class MPSCNNPoolingGradient](mpscnnpoolinggradient.md)
  A gradient pooling kernel.
- [class MPSCNNDilatedPoolingMaxGradient](mpscnndilatedpoolingmaxgradient.md)
  A gradient dilated max pooling filter.
- [class MPSCNNPoolingL2NormGradient](mpscnnpoolingl2normgradient.md)
  A gradient L2-norm pooling filter.
- [class MPSCNNPoolingMaxGradient](mpscnnpoolingmaxgradient.md)
  A gradient max pooling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpooling)*