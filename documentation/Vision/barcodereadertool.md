# BarcodeReaderTool

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

A tool that scans machine-readable codes in an image.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct BarcodeReaderTool
```

## Overview

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

> **Note**:  [`BarcodeReaderTool`](./barcodereadertool.md) isn’t available in Simulator.

## Topics

### Creating a tool
- [init(name: String?, description: String?)](./barcodereadertool/init%28name,description%29.md)
  Creates a tool for decoding machine-readable codes.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Tool](../FoundationModels/tool.md)

## See Also

### Foundation Models integration
- [struct OCRTool](./ocrtool.md)
  A tool that recognizes text in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/barcodereadertool)*