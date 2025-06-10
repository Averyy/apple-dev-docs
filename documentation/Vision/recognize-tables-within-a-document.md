# Recognizing tables within a document

**Framework**: Vision

Scan a document containing a contact table and extract the content within the table in a formatted way.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Xcode 26.0+ (Beta)

#### Overview

> **Note**: This sample code project is associated with WWDC25 session 272: [`Reading documents using Vision`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/272).

##### Configure the Sample Code Project

Because this sample app requires camera access, you’ll need to build and run this sample on a device. The first time you run this sample on device, you need to grant the app access to the camera. In the sample project’s `assets` folder, open the `sampleDocuments.png` file and use the rear camera on iPad or iPhone. Optionally, if you have access to a printer, print this file and try scanning it with your device.

## See Also

- [Locating and displaying recognized text](locating-and-displaying-recognized-text.md)
  Perform text recognition on a photo using the Vision framework’s text-recognition request.
- [struct RecognizeDocumentsRequest](recognizedocumentsrequest.md)
  An image-analysis request to scan an image of a document and provide information about its structure.
- [struct DocumentObservation](documentobservation.md)
  Information about the sections of content that an image-analysis request detects in a document.
- [struct DetectTextRectanglesRequest](detecttextrectanglesrequest.md)
  An image-analysis request that finds regions of visible text in an image.
- [struct RecognizeTextRequest](recognizetextrequest.md)
  An image-analysis request that recognizes text in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognize-tables-within-a-document)*