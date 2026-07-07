# OCRTool

**Framework**: Vision  
**Kind**: struct

A tool that recognizes text in an image.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct OCRTool
```

#### Overview

The tool returns a string containing all recognized text from the image. To enable this tool, configure your `LanguageModelSession` with an instance of `OCRTool`.

```swift
let ocrTool = OCRTool()
let session = LanguageModelSession(tools: [ocrTool])
```

You can override the default name and description to customize how the model identifies and uses the tool.

```swift
let customTool = OCRTool(
    name: "extractText",
    description: "Extract text from documents"
)
```

## Topics

### Creating a tool
- [init(name: String?, description: String?)](ocrtool/init(name:description:).md)
  Creates a tool for recognizing text in images.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Tool](../FoundationModels/Tool.md)

## See Also

- [struct BarcodeReaderTool](barcodereadertool.md)
  A tool that scans machine-readable codes in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/ocrtool)*