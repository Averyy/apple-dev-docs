# VisionKit

**Framework**: VisionKit  
**Kind**: module

Identify and extract information in the environment using the device’s camera, or in images that your app displays.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

#### Overview

VisionKit analyzes pixel information and isolates important data such as text of a given language, URLs, street addresses, phone numbers, shipment tracking numbers, flight numbers, dates, times, durations, and barcodes of various formats. The framework provides this analysis to your app through user interfaces your app displays, which enable people to interact with the analyzed data ([`ImageAnalyzer.AnalysisTypes`](imageanalyzer/analysistypes.md)) and return the data of interest back to your app. In the interfaces, people can highlight, tap to focus, copy and extract data to the clipboard, or invoke a menu option that runs an app-defined action. VisionKit offers the following user interfaces:

[`DataScannerViewController`](datascannerviewcontroller.md) presents a camera pass-through view that enables the user to interact with any of the recognized content types ([`DataScannerViewController.RecognizedDataType`](datascannerviewcontroller/recognizeddatatype.md)) as seen in the environment, and provides captured information to the app for processing.

The Image Analysis interface ([`ImageAnalysisInteraction`](imageanalysisinteraction.md) on iOS, and [`ImageAnalysisOverlayView`](imageanalysisoverlayview.md) on macOS) displays on top of an image and enables people to interact with content types ([`ImageAnalysisInteraction.InteractionTypes`](imageanalysisinteraction/interactiontypes.md)) that the framework recognizes in the image. For example, the Live Text interface enables them to select any text present in the image ([`textSelection`](imageanalysisinteraction/interactiontypes/textselection.md)), or invoke a URL ([`dataDetectors`](imageanalysisinteraction/interactiontypes/datadetectors.md)). Also, the text selection UI offers framework-standard buttons for copying selected text, or looking up the subject on the web for more information.

![A mockup of an iPhone screen showing the Live Text button and highlighted text with its action menu.](https://docs-assets.developer.apple.com/published/c125f3997a70202dc03466ec491d07c5/visionkit-1%402x.png)

VisionKit’s Document Camera view controller ([`VNDocumentCameraViewController`](vndocumentcameraviewcontroller.md)) is a camera pass-through experience that enables users to scan physical documents. The user scans the document page by page by tapping a camera interface in the view, which provides your app with the resulting images by page number after the scan completes. With the collection of scanned images, your app can create a digital version of the physical document, such as by exporting the scanned images to PDF.

#### Interact with Image Subjects

In iOS 17 and macOS 14 and later, VisionKit identifies subjects within an image (see [`ImageAnalysisInteraction.Subject`](imageanalysisinteraction/subject.md)). A  may be the focal point of a picture, such as an object around which a photograph centers. Or, the framework may identify several objects that it recognizes in an image. VisionKit enables your app to extract, or , subjects to a separate image with the background removed (see [`image`](imageanalysisinteraction/subject/image.md)), or present a button that gives more information on the subject ([`visualLookUp`](imageanalysisinteraction/interactiontypes/visuallookup.md)).

> **Note**: In macOS 14 and later, macOS apps built with Mac Catalyst support the [`ImageAnalyzer`](imageanalyzer.md) and [`ImageAnalysisInteraction`](imageanalysisinteraction.md) classes.

## Topics

### Content recognition and interaction in images
- [Enabling Live Text interactions with images](enabling-live-text-interactions-with-images.md)
  Add a Live Text interface that enables users to perform actions with text and QR codes that appear in images.
- [class ImageAnalyzer](imageanalyzer.md)
  An object that finds items in images that people can interact with, such as subjects, text, and QR codes.
- [class ImageAnalysis](imageanalysis.md)
  An object that represents the results of analyzing an image, and provides the input for the Live Text interface object.
- [class ImageAnalysisInteraction](imageanalysisinteraction.md)
  An interface that enables people to interact with recognized text, barcodes, and other objects in an image.
- [protocol ImageAnalysisInteractionDelegate](imageanalysisinteractiondelegate.md)
  A delegate that handles image-analysis and user-interaction callbacks for an interaction object.
- [class ImageAnalysisOverlayView](imageanalysisoverlayview.md)
  A view that enables people to interact with recognized text, barcodes, and other objects in an image.
- [protocol ImageAnalysisOverlayViewDelegate](imageanalysisoverlayviewdelegate.md)
  A delegate that handles image-analysis and user-interaction callbacks for an overlay view.
- [struct CameraRegionView](cameraregionview.md)
  This view displays a stabilized region of interest within a person’s view and provides passthrough camera feed for that selected region.
### Barcode and text scanning through the camera
- [Scanning data with the camera](scanning-data-with-the-camera.md)
  Enable Live Text data scanning of text and codes that appear in the camera’s viewfinder.
- [class DataScannerViewController](datascannerviewcontroller.md)
  An object that scans the camera live video for text, data in text, and machine-readable codes.
- [protocol DataScannerViewControllerDelegate](datascannerviewcontrollerdelegate.md)
  A delegate object that responds when people interact with items that the data scanner recognizes.
- [enum RecognizedItem](recognizeditem.md)
  An item that the data scanner recognizes in the camera’s live video.
### Document scanning through the camera
- [Structuring Recognized Text on a Document](structuring_recognized_text_on_a_document.md)
  Detect, recognize, and structure text on a business card or receipt using Vision and VisionKit.
- [class VNDocumentCameraViewController](vndocumentcameraviewcontroller.md)
  An object that presents UI for a camera pass-through that helps people scan physical documents.
- [protocol VNDocumentCameraViewControllerDelegate](vndocumentcameraviewcontrollerdelegate.md)
  A delegate protocol through which the document camera returns its scanned results.
- [class VNDocumentCameraScan](vndocumentcamerascan.md)
  A single document scanned in the document camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/VisionKit)*