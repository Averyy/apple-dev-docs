# visualLookUp

**Framework**: VisionKit  
**Kind**: property  
**Role**: Type Property

An option that analyzes an image for subjects that the framework can look up for more information.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let visualLookUp: ImageAnalyzer.AnalysisTypes
```

#### Discussion

When the framework recognizes a particular type of subject in an image, it offers an interface for people to learn more about the subject. For example, if an image contains a rose, the framework recognizes a plant and enables people to tap the plant which presents a sheet with a list of additional resources on the specific type of plant — in this case, a rose.

For more information about subjects in images, see [`ImageAnalysisInteraction.Subject`](../../imageanalysisinteraction/subject.md).

## See Also

### Specifying types to find
- [static let machineReadableCode: ImageAnalyzer.AnalysisTypes](./machinereadablecode.md)
  An option that analyzes an image for machine-readable codes, such as QR codes.
- [static let text: ImageAnalyzer.AnalysisTypes](./text.md)
  An option that analyzes an image for text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalyzer/analysistypes/visuallookup)*