# apply(_:arguments:options:)

**Framework**: Core Image  
**Kind**: instm

Produces a [`CIImage`](ciimage.md) object by applying arguments to a kernel function and using options to control how the kernel function is evaluated.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func apply(_ k: CIKernel, arguments args: [Any]?, options dict: [String : Any]? = nil) -> CIImage?
```

#### Return_value

The [`CIImage`](ciimage.md) object produced by a filter.

#### Discussion

If you are implementing a custom filter, this method needs to be called from within the [`outputImage`](cifilter/1438169-outputimage.md) method in order to apply your kernel function to the [`CIImage`](ciimage.md) object. You can pass any of the keys defined in [`Options for Applying a Filter`](cifilter/options_for_applying_a_filter.md), along with appropriate values, into the options dictionary.

## Parameters

- `k`: A   object that contains a kernel function.
- `args`: The arguments that are type compatible with the function signature of the kernel function.
- `dict`: A dictionary that contains options (key-value pairs) to control how the kernel function is evaluated.

## See Also

- [- apply:](cifilter/1562058-apply.md)
  Produces a  object by applying a kernel function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/1438077-apply)*