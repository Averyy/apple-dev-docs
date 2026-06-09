# BarcodeReaderTool

**Framework**: Vision  
**Kind**: struct

A tool that scans machine-readable codes in an image.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct BarcodeReaderTool
```

#### Overview

When the model encounters an image containing machine-readable codes, it can call this tool to decode them. The tool returns an array of `Barcode` results, each containing the decoded content and the symbology type.

To enable this tool, configure your `LanguageModelSession` with an instance of `BarcodeReaderTool`.

```swift
let barcodeTool = BarcodeReaderTool()
let session = LanguageModelSession(tools: [barcodeTool])
```

You can override the default name and description to customize how the model identifies and uses the tool.

```swift
let customTool = BarcodeReaderTool(
    name: "scanQRCode",
    description: "Scan QR codes"
)
```

## Topics

### Initializers
- [init(name: String?, description: String?)](barcodereadertool/init(name:description:).md)
  Creates a tool for decoding machine-readable codes.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Tool](../FoundationModels/Tool.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/barcodereadertool)*