# process(with:arguments:output:)

**Framework**: Core Image  
**Kind**: clm

Method to override for customizing the kernel's image processing.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func process(with inputs: [any CIImageProcessorInput]?, arguments: [String : Any]?, output: any CIImageProcessorOutput) throws
```

#### Return_value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if processing succeeded, and [`false`](https://developer.apple.com/documentation/swift/false) if processing failed.

#### Discussion

Override this method to perform custom image processing. 

## Parameters

- `inputs`: Inputs to this processor stage.
- `arguments`: Dictionary of arguments mapping keys such as   to their values.
- `output`: The output image following processing.
- `error`: Pointer to the NSError object into which processing errors will be written.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/2138290-process)*