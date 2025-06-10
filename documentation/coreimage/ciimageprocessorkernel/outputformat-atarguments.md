# outputFormat(at:arguments:)

**Framework**: Core Image  
**Kind**: method

Override this class method if your processor has more than one output and you want your processor’s output to be in a specific supported `CIPixelFormat`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class func outputFormat(at outputIndex: Int32, arguments: [String : Any]?) -> CIFormat
```

#### Return Value

 Return the desired `CIPixelFormat`

#### Discussion

The format must be one of `kCIFormatBGRA8`, `kCIFormatRGBAh`, `kCIFormatRGBAf` or `kCIFormatR8`. On iOS 12 and macOS 10.14, the formats `kCIFormatRh` and `kCIFormatRf` are also supported.

If the outputFormat is `0`, then the output will be a supported format that best matches the rendering context’s [`workingFormat`](cicontext/workingformat.md).

## Parameters

- `outputIndex`: The index that tells you which processor output for which to return the desired 
- `arguments`: The arguments dictionary that was passed to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/outputformat(at:arguments:))*