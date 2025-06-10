# apply(_:arguments:options:)

**Framework**: Core Image  
**Kind**: method

Produces a [`CIImage`](ciimage.md) object by applying arguments to a kernel function and using options to control how the kernel function is evaluated.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func apply(_ k: CIKernel, arguments args: [Any]?, options dict: [String : Any]? = nil) -> CIImage?
```

#### Return Value

The [`CIImage`](ciimage.md) object produced by a filter.

#### Discussion

If you are implementing a custom filter, this method needs to be called from within the [`outputImage`](cifilter-swift.class/outputimage.md) method in order to apply your kernel function to the [`CIImage`](ciimage.md) object. You can pass any of the keys defined in [`Options for Applying a Filter`](options-for-applying-a-filter.md), along with appropriate values, into the options dictionary.

## Parameters

- `k`: A   object that contains a kernel function.
- `args`: The arguments that are type compatible with the function signature of the kernel function.
- `dict`: A dictionary that contains options (key-value pairs) to control how the kernel function is evaluated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/apply(_:arguments:options:))*